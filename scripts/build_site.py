#!/usr/bin/env python3
"""Render the EIP-8038 repricing site from archived runs into ``docs/``.

A *run* is one fit, snapshotted by ``scripts/archive_run.py`` into
``data/runs/<run_id>/`` (``gasfit/`` report bundle + ``raw_meta.json`` +
``fit.yaml``). This script renders **every** archived run and wires a
run-selector dropdown (rendered in ``base.html``) that switches between them:

* latest run        → ``docs/{index,new-gas,runtime,glue,methodology}.html`` + ``docs/figs/``
* every older run   → ``docs/runs/<run_id>/<page>.html`` + ``docs/runs/<run_id>/figs/``

Each older run's pages sit beside their own ``figs/``, so the relative
``figs/...`` image paths baked into the reports resolve with no rewriting.
Shared assets (CSS/JS) live once at the docs root; older pages reach them via a
``root_prefix`` of ``../../``. Runs beyond the newest 5 have their runtime/glue
figures pruned at archive time — those pages still render the text/tables, just
without plots (flagged via ``figs_pruned``).

When ``data/runs/`` is empty (e.g. before the first ``make gasfit`` archive),
the script falls back to a single synthetic run built straight from
``data/gasfit/`` so ``make site`` still works.

Data sources per run (all produced by ``make fetch`` + ``make gasfit``):

* ``raw_meta.json``                     — reproducibility footer (suites, fork, run window)
* ``gasfit/new_gas_proposal.md``        — rendered wholesale for the new-gas page
* ``gasfit/*_report.md``                — parsed into filterable per-fit sections
* ``gasfit/glue_results.csv``           — per (client, glue_opcode) glue headline stats
* ``gasfit/figs/{proposal,runtime,glue}/`` — copied into the run's output ``figs/``
"""
from __future__ import annotations

import json
import math
import re
import shutil
import subprocess
from importlib.metadata import PackageNotFoundError, version as pkg_version
from pathlib import Path

import markdown
import pandas as pd
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
GASFIT = ROOT / "data" / "gasfit"
RUNS = ROOT / "data" / "runs"
FIT = ROOT / "fit.yaml"
SRC = ROOT / "site_src"
TEMPLATES = SRC / "templates"
ASSETS = SRC / "assets"
OUT = ROOT / "docs"

# Keep in sync with archive_run.KEEP_FULL_FIGS: runs past this many (newest-first)
# have had their runtime/glue figs pruned, so their pages flag plots as omitted.
KEEP_FULL_FIGS = 5

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "md_in_html", "toc"]

# Page key -> output filename. A run's pages all share one directory, so these
# bare names double as the in-run nav hrefs.
PAGES = {
    "index": "index.html",
    "new-gas": "new-gas.html",
    "runtime": "runtime.html",
    "glue": "glue.html",
    "methodology": "methodology.html",
}


# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #
def md_to_html(text: str) -> str:
    # The generated reports wrap markdown tables inside raw <details> blocks. Without
    # a `markdown` attribute, md_in_html would leave that inner markdown unprocessed,
    # so tag the collapsibles before rendering.
    text = text.replace("<details>", '<details markdown="1">')
    text = text.replace("<summary>", '<summary markdown="span">')
    return markdown.markdown(text, extensions=MD_EXTENSIONS)


def strip_first_h1(text: str) -> str:
    return re.sub(r"^# .*\n", "", text, count=1)


def drop_section(text: str, heading: str) -> str:
    """Remove a ``## heading`` section up to (but not including) the next ``## ``."""
    pattern = rf"^{re.escape(heading)}\n.*?(?=^## )"
    return re.sub(pattern, "", text, count=1, flags=re.S | re.M)


def package_version(dist_name: str, fallback: str) -> str:
    try:
        return pkg_version(dist_name)
    except PackageNotFoundError:
        return fallback


def git_commit() -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


# --------------------------------------------------------------------------- #
# Reproducibility metadata (footer)
# --------------------------------------------------------------------------- #
def load_meta(raw_meta_path: Path) -> dict:
    raw = json.loads(raw_meta_path.read_text())
    return {
        "suites": [s["suite_hash"] for s in raw["suites"]],
        "fork": raw["query"]["fork"],
        "run_timestamp": raw["data_window"]["end"],
        "fetch_version": package_version("benchmarkoor-fetch", raw.get("package_version", "?")),
        "gasfit_version": package_version("evm-gasfit", "?"),
        "commit": git_commit(),
    }


def run_label(raw_meta_path: Path) -> str:
    """Human-friendly ``YYYY-MM-DD HH:MM`` label from the data-window end."""
    end = json.loads(raw_meta_path.read_text())["data_window"]["end"]
    m = re.match(r"(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2})", end)
    return f"{m.group(1)} {m.group(2)}" if m else end


# --------------------------------------------------------------------------- #
# Proposal table (used by the landing page for the headline takeaway)
# --------------------------------------------------------------------------- #
def parse_proposed_table(gasfit: Path) -> list[dict]:
    """Parse the ``## Proposed gas parameters`` table into rows."""
    text = (gasfit / "new_gas_proposal.md").read_text()
    block = re.search(r"## Proposed gas parameters\n(.*?)(?=^## )", text, re.S | re.M)
    rows: list[dict] = []
    if not block:
        return rows
    for line in block.group(1).splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= set("| -"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells[0] in ("Gas param", ""):
            continue
        rows.append({
            "param": cells[0],
            "current": cells[1],
            "proposed": cells[2],
            "diff": cells[3],
            "diff_pct": cells[4],
        })
    return rows


def _heat_cell_style(t: float) -> str:
    """Inline background/text style for one heatmap cell. ``t`` ∈ [-1, 1]:
    negative = cheaper than current (green), positive = pricier (red), 0 = blank.
    Alpha rides over a transparent base, so it reads in both themes; saturated
    cells flip to white text. Mirrors the site's delta green/red.

    A *linear* alpha buries small changes near-transparent — a +0.3 and a -0.3
    log2 ratio both look blank, so faint red and faint green are indistinguishable.
    A gamma curve plus a floor lifts small magnitudes into a clearly visible tint
    while keeping the big movers saturated, so hue (not just intensity) carries
    the increase-vs-decrease signal."""
    mag = min(abs(t), 1.0)
    a = 0.0 if mag == 0 else max(0.25, mag ** 0.45)
    r, g, b = (201, 42, 42) if t > 0 else (43, 138, 62)
    fg = "#fff" if a > 0.6 else "inherit"
    return f"background: rgba({r},{g},{b},{a:.3f}); color: {fg};"


def winning_fits(ap: pd.DataFrame) -> pd.DataFrame:
    """The selected (winning) fit per (param, client) in ``new_gas_all_params.csv``.

    evm-gasfit >=0.0.3 emits *every* candidate fit and flags the chosen one with
    ``is_winner``; pre-0.0.3 output carried only the winners (where the row's own
    test/opcode/coef equalled the ``selected_*`` triple, which is no longer unique
    now that losing candidates share it). Prefer the flag, fall back to the triple
    match so older archives still render."""
    if "is_winner" in ap.columns:
        mask = ap["is_winner"].astype(str).str.strip().str.lower().isin(("true", "1"))
        return ap[mask]
    return ap[
        (ap["test_name"] == ap["selected_test"])
        & (ap["target_opcode"] == ap["selected_opcode"])
        & (ap["model_coef_name"] == ap["selected_model_coef_name"])
    ]


def build_proposal_heatmap(gasfit: Path, current_by_param: dict[str, str]) -> str | None:
    """Themed HTML replacement for evm-gasfit's ``heatmap.png``.

    Per-client proposed gas (the selected fits in ``new_gas_all_params.csv``) for
    each estimated parameter, cells tinted by ``log2(proposed / current)`` on a
    symmetric green→red scale. Estimated params only — derived params (empty
    ``client_name``) have no per-client series. Returns ``None`` if the source
    CSV is absent or carries no per-client rows, so the caller can keep the PNG."""
    csv = gasfit / "new_gas_all_params.csv"
    if not csv.exists():
        return None
    ap = pd.read_csv(csv)
    sel = winning_fits(ap)
    value: dict[str, dict[str, int]] = {}
    clients: set[str] = set()
    for _, row in sel.iterrows():
        client = row["client_name"]
        if not isinstance(client, str) or not client:
            continue
        value.setdefault(row["gas_param"], {})[client] = int(row["new_gas_rounded"])
        clients.add(client)
    if not value:
        return None
    ordered_clients = sorted(clients)
    params = [p for p in current_by_param if p in value]  # proposal-table order

    def log2ratio(param: str, client: str) -> float | None:
        cur = current_by_param.get(param, "")
        cur_n = int(cur) if cur.lstrip("-").isdigit() else None
        v = value[param].get(client)
        return math.log2(v / cur_n) if cur_n and v else None

    all_lr = [lr for p in params for c in ordered_clients if (lr := log2ratio(p, c)) is not None]
    vmax = max((abs(x) for x in all_lr), default=1.0) or 1.0

    head = "".join(f"<th scope='col'>{c}</th>" for c in ordered_clients)
    body = ""
    for p in params:
        cells = f"<th scope='row'>{p}</th>"
        for c in ordered_clients:
            v = value[p].get(c)
            if v is None:
                cells += '<td class="empty">—</td>'
                continue
            lr = log2ratio(p, c)
            style = _heat_cell_style((lr / vmax) if lr is not None else 0.0)
            title = "" if lr is None else f" title='log2(proposed/current) = {lr:+.2f}'"
            cells += f"<td style='{style}'{title}>{v:,}</td>"
        body += f"<tr>{cells}</tr>"
    return (
        '<table class="heatmap">'
        f"<thead><tr><th scope='col'></th>{head}</tr></thead>"
        f"<tbody>{body}</tbody></table>"
    )


# Combo identity for a provenance candidate: the source regression triple plus
# the model_by factors. Order matches evm-gasfit's M1…Mn legend (and the CSV's
# first-appearance order, which we rely on below).
_PROV_COMBO_COLS = [
    "test_name", "target_opcode", "model_coef_name",
    "param_account_mode", "param_existing_slots", "param_opcode",
]


def _prov_short(col: str, val) -> str:
    """Compact rendering of one combo component for a descriptive row label
    (used when the report emits no ``M#`` legend for the parameter)."""
    s = str(val)
    if col == "param_account_mode":
        return s.replace("AccountMode.", "")
    if col == "param_existing_slots":
        return f"slots={s}"
    return s


def build_provenance_heatmap(
    gasfit: Path, param: str, current_by_param: dict[str, str], mlabels: bool
) -> str | None:
    """Themed HTML replacement for evm-gasfit's ``provenance__<param>.png``.

    Same palette as :func:`build_proposal_heatmap`, but rows are the candidate
    model combos the worst-case selector saw (first-appearance order, matching
    the report's ``M1…Mn`` legend) and columns are clients. Each cell carries
    that candidate's proposed gas, tinted by ``log2(proposed / current)`` on a
    *per-parameter* symmetric scale; the cell the selector picked
    (``is_winner``) gets a ``sel`` outline. When ``mlabels`` is false (the
    report has no legend table for this param, i.e. few combos) rows are
    labelled by their varying combo components instead of ``M#``. Returns
    ``None`` if the CSV is absent or has no per-client rows for ``param``, so
    the caller can keep the PNG."""
    csv = gasfit / "new_gas_all_params.csv"
    if not csv.exists():
        return None
    ap = pd.read_csv(csv)
    g = ap[(ap["gas_param"] == param) & ap["client_name"].notna()
           & (ap["client_name"].astype(str) != "")]
    if g.empty:
        return None

    combo_cols = [c for c in _PROV_COMBO_COLS if c in g.columns]
    varying = [c for c in combo_cols if g[c].astype(str).nunique() > 1]

    # Combos in first-appearance order → M1…Mn (matches the report legend);
    # cells keyed by (combo, client) → (proposed gas, is_winner). The CSV emits
    # each candidate more than once (identical combo + value); collapse to one
    # cell per (combo, client) and OR the winner flag so a later non-winner
    # duplicate can't unset the selected outline.
    combos: list[tuple] = []
    cell: dict[tuple, dict[str, tuple[int, bool]]] = {}
    for _, r in g.iterrows():
        key = tuple(r[c] for c in combo_cols)
        if key not in cell:
            combos.append(key)
        win = str(r.get("is_winner", "")).strip().lower() in ("true", "1")
        prev = cell.setdefault(key, {}).get(r["client_name"])
        cell[key][r["client_name"]] = (int(r["new_gas_rounded"]), win or bool(prev and prev[1]))
    clients = sorted(c for c in g["client_name"].unique() if isinstance(c, str) and c)

    cur = current_by_param.get(param, "")
    cur_n = int(cur) if cur.lstrip("-").isdigit() else None

    def log2ratio(v: int) -> float | None:
        return math.log2(v / cur_n) if cur_n and v else None

    all_lr = [lr for combo in combos for c in clients
              if (cv := cell[combo].get(c)) and (lr := log2ratio(cv[0])) is not None]
    vmax = max((abs(x) for x in all_lr), default=1.0) or 1.0

    def row_label(i: int, combo: tuple) -> str:
        if mlabels:
            return f"M{i}"
        descr = " · ".join(
            _prov_short(c, v) for c, v in zip(combo_cols, combo)
            if c in varying and pd.notna(v)
        )
        return descr or f"M{i}"

    head = "".join(f"<th scope='col'>{c}</th>" for c in clients)
    body = ""
    for i, combo in enumerate(combos, 1):
        full = " / ".join(f"{c}={v}" for c, v in zip(combo_cols, combo) if pd.notna(v))
        cells = f'<th scope="row" title="{full}">{row_label(i, combo)}</th>'
        for c in clients:
            cv = cell[combo].get(c)
            if cv is None:
                cells += '<td class="empty">—</td>'
                continue
            v, win = cv
            lr = log2ratio(v)
            style = _heat_cell_style((lr / vmax) if lr is not None else 0.0)
            cls = " class='sel'" if win else ""
            title = "" if lr is None else f" title='log2(proposed/current) = {lr:+.2f}'"
            cells += f"<td{cls} style='{style}'{title}>{v:,}</td>"
        body += f"<tr>{cells}</tr>"
    return (
        '<table class="heatmap provenance">'
        f"<thead><tr><th scope='col'></th>{head}</tr></thead>"
        f"<tbody>{body}</tbody></table>"
    )


# --------------------------------------------------------------------------- #
# Runtime report → filterable sections
# --------------------------------------------------------------------------- #
_DETAILS_RE = re.compile(
    r"<details><summary>(?P<client>\w+) — NNLS regression summary</summary>\s*"
    r"```\n(?P<nnls>.*?)\n```(?P<rest>.*?)</details>",
    re.S,
)


def _parse_md_table(text: str) -> dict[str, dict]:
    """Parse the per-client summary table at the top of a runtime subsection."""
    rows: dict[str, dict] = {}
    table_lines = [ln for ln in text.splitlines() if ln.strip().startswith("|")]
    for line in table_lines:
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or cells[0] in ("client", "") or set("".join(cells)) <= set("-: "):
            continue
        rows[cells[0]] = {
            "nobs": cells[1], "rsquared": cells[2], "coef": cells[3],
            "pvalue": cells[4], "ci": cells[5],
        }
    return rows


def _split_combo(heading: str) -> tuple[str, str]:
    m = re.match(r"(?P<test>.+?) — combo `(?P<combo>.+)`", heading)
    if m:
        return m.group("test").strip(), m.group("combo")
    return heading.strip(), "all"


def parse_runtime(gasfit: Path) -> dict:
    text = (gasfit / "runtime_estimation_autogenerated_report.md").read_text()
    sections: list[dict] = []
    opcodes: list[str] = []

    opcode_parts = re.split(r"^## (.+)$", text, flags=re.M)
    for i in range(1, len(opcode_parts), 2):
        opcode = opcode_parts[i].strip()
        if opcode.lower() == "contents":
            continue
        opcodes.append(opcode)
        body = opcode_parts[i + 1]

        sub_parts = re.split(r"^### (.+)$", body, flags=re.M)
        for j in range(1, len(sub_parts), 2):
            test, combo = _split_combo(sub_parts[j].strip())
            sub = sub_parts[j + 1]
            table = _parse_md_table(sub)
            for m in _DETAILS_RE.finditer(sub):
                client = m.group("client")
                figs = re.findall(r"!\[\]\((figs/runtime/[^)]+)\)", m.group("rest"))
                # Older runs have runtime figs pruned; only emit those still on disk.
                figs = [f for f in figs if (gasfit / f).exists()]
                sections.append({
                    "opcode": opcode, "test": test, "combo": combo, "client": client,
                    "nnls": m.group("nnls"), "figs": figs,
                    **table.get(client, {}),
                })

    return {
        "sections": sections,
        "opcodes": opcodes,
        "clients": sorted({s["client"] for s in sections}),
    }


# --------------------------------------------------------------------------- #
# Glue report + CSV → filterable sections
# --------------------------------------------------------------------------- #
def _parse_glue_appendix(gasfit: Path) -> list[dict]:
    """Per-client tier/joint NNLS summaries, grouped by client."""
    text = (gasfit / "glue_opcodes_autogenerated_report.md").read_text()
    out: list[dict] = []
    client_parts = re.split(r"^## (.+)$", text, flags=re.M)
    for i in range(1, len(client_parts), 2):
        client = client_parts[i].strip()
        if client.lower() == "contents":
            continue
        body = client_parts[i + 1]
        fits: list[dict] = []
        sub_parts = re.split(r"^### (.+)$", body, flags=re.M)
        for j in range(1, len(sub_parts), 2):
            heading = sub_parts[j].strip()
            for m in re.finditer(r"```\n(.*?)\n```", sub_parts[j + 1], re.S):
                fits.append({"heading": heading, "nnls": m.group(1)})
        if fits:
            out.append({"client": client, "fits": fits})
    return out


def parse_glue(gasfit: Path) -> dict:
    gr = pd.read_csv(gasfit / "glue_results.csv")
    sections: list[dict] = []
    for _, r in gr.iterrows():
        client, opcode = r["client_name"], r["glue_opcode"]
        figs = [
            f"figs/glue/{opcode}__{client}__{kind}.png"
            for kind in ("regression", "bootstrap", "diagnostics")
        ]
        figs = [f for f in figs if (gasfit / f).exists()]
        sections.append({
            "client": client, "glue_opcode": opcode,
            "nobs": int(r["nobs"]),
            "glue_runtime_ms": float(r["glue_runtime_ms"]),
            "p_value": float(r["p_value"]),
            "rsquared": float(r["rsquared"]),
            "figs": figs,
        })
    return {
        "sections": sections,
        "clients": sorted(gr["client_name"].unique().tolist()),
        "glue_opcodes": sorted(gr["glue_opcode"].unique().tolist()),
        "appendix": _parse_glue_appendix(gasfit),
    }


# --------------------------------------------------------------------------- #
# Cross-run trends (the Trends page — spans every run, rendered once)
# --------------------------------------------------------------------------- #
def _combo_label(row) -> str:
    """Human label for the binding fit that produced a client's value.

    The selected row is the client's worst-case fit, so its ``selected_*`` triple
    names the test/opcode/model that set the value; ``param_account_mode`` /
    ``param_opcode`` disambiguate the account-param variants."""
    def clean(v) -> str:
        return "" if v is None or (isinstance(v, float) and pd.isna(v)) else str(v)

    core = " · ".join(p for p in (
        clean(row["selected_test"]),
        clean(row["selected_opcode"]),
        clean(row["selected_model_coef_name"]),
    ) if p)
    extras = [clean(row.get(c)).replace("AccountMode.", "")
              for c in ("param_account_mode", "param_opcode")]
    extras = [e for e in extras if e]
    return f"{core} ({', '.join(extras)})" if extras else core


def collect_trends(runs: list[dict]) -> dict:
    """Per-client gas/runtime series across all runs, for the Trends page.

    ``discover_runs()`` yields newest-first; here we reverse to oldest→newest so
    the run axis reads chronologically. Per run we read the per-client selected
    fits (``new_gas_all_params.csv``) and the binding proposal — the worst-client
    value actually proposed (``new_gas.csv``). Estimated params carry a per-client
    series; derived params (empty ``client_name``) only have the binding value.
    Clients are unioned across runs; a run missing a (param, client) leaves a
    ``None`` gap."""
    chron = list(reversed(runs))
    n = len(chron)
    gas: dict[str, dict[str, list]] = {}
    runtime: dict[str, dict[str, list]] = {}
    combo: dict[str, dict[str, list]] = {}
    poor: dict[str, dict[str, list]] = {}
    binding: dict[str, list] = {}
    clients: set[str] = set()

    def cell(store: dict, param: str, client: str) -> list:
        return store.setdefault(param, {}).setdefault(client, [None] * n)

    for i, run in enumerate(chron):
        gasfit = run["gasfit"]
        ap = pd.read_csv(gasfit / "new_gas_all_params.csv")
        selected = winning_fits(ap)
        for _, row in selected.iterrows():
            client = row["client_name"]
            if not isinstance(client, str) or not client:
                continue  # derived params have no per-client fit
            param = row["gas_param"]
            clients.add(client)
            cell(gas, param, client)[i] = int(row["new_gas_rounded"])
            cell(runtime, param, client)[i] = float(row["runtime_ms"])
            cell(combo, param, client)[i] = _combo_label(row)
            # evm-gasfit's own poor-fit flag (its New-gas R²/p-value thresholds).
            cell(poor, param, client)[i] = str(row["poor_fit"]).strip().lower() in ("true", "1")

        ng = pd.read_csv(gasfit / "new_gas.csv")
        for _, row in ng.iterrows():
            param = row["gas_param"]
            client = row["client_name"]
            binding.setdefault(param, [None] * n)[i] = {
                "value": int(row["new_gas_rounded"]),
                "client": client if isinstance(client, str) and client else None,
            }

    all_params = sorted(binding)
    return {
        "runs": [{"run_id": r["run_id"], "label": r["label"]} for r in chron],
        "clients": sorted(clients),
        "estimated_params": [p for p in all_params if p in gas],
        "derived_params": [p for p in all_params if p not in gas],
        "gas": gas,
        "runtime": runtime,
        "combo": combo,
        "poor": poor,
        "binding": binding,
    }


# --------------------------------------------------------------------------- #
# Goal targets (the Goals page — latest run only, rendered once)
# --------------------------------------------------------------------------- #
# Fixed target gas values a client should reach. A client "clears" a goal when its
# estimate is <= the goal (lower is better). The write goals subtract the bundled
# cold-access component (the access goal) to isolate the pure-write cost, and the
# account goals require *both* the CODE and NOCODE variants to clear.
GOAL_SPECS = [
    {"key": "COLD_STORAGE_ACCESS", "goal": 3000, "subtract": 0,
     "params": ["COLD_STORAGE_ACCESS"], "current_param": "COLD_STORAGE_ACCESS"},
    {"key": "STORAGE_WRITE", "goal": 10000, "subtract": 3000,
     "params": ["COLD_STORAGE_WRITE"], "current_param": "STORAGE_WRITE"},
    {"key": "COLD_ACCOUNT_ACCESS", "goal": 3000, "subtract": 0,
     "params": ["COLD_ACCOUNT_CODE_ACCESS", "COLD_ACCOUNT_NOCODE_ACCESS"],
     "current_param": "COLD_ACCOUNT_NOCODE_ACCESS"},
    {"key": "ACCOUNT_WRITE", "goal": 8000, "subtract": 3000,
     "params": ["COLD_ACCOUNT_CODE_WRITE", "COLD_ACCOUNT_NOCODE_WRITE"],
     "current_param": "ACCOUNT_WRITE"},
    {"key": "WARM_ACCESS", "goal": 100, "subtract": 0,
     "params": ["WARM_ACCESS"], "current_param": "WARM_ACCESS"},
]


def _variant_label(param: str) -> str:
    """CODE / NOCODE tag for an account-param variant; "" for single-param goals."""
    if "NOCODE" in param:
        return "NOCODE"
    return "CODE" if "CODE" in param else ""


def collect_goals(gasfit: Path) -> dict:
    """Per-client pass/fail of each goal target for the latest run.

    Reads the per-client selected fits (``winning_fits`` over
    ``new_gas_all_params.csv``), derives each goal's per-client value (subtracting
    the bundled access component for the write goals), and flags
    ``clears = effective <= goal``. Account goals require *both* the CODE and NOCODE
    variants to clear; a client missing any required param leaves a ``no_data`` cell
    (which never counts as cleared)."""
    ap = pd.read_csv(gasfit / "new_gas_all_params.csv")
    sel = winning_fits(ap)
    # value[param][client] -> rounded proposed gas (same extraction as build_proposal_heatmap)
    value: dict[str, dict[str, int]] = {}
    clients: set[str] = set()
    for _, row in sel.iterrows():
        client = row["client_name"]
        if not isinstance(client, str) or not client:
            continue  # derived params carry no per-client fit
        value.setdefault(row["gas_param"], {})[client] = int(row["new_gas_rounded"])
        clients.add(client)
    ordered_clients = sorted(clients)

    current_by_param = {r["param"]: r["current"] for r in parse_proposed_table(gasfit)}

    matrix: dict[str, dict[str, dict]] = {}
    goals: list[dict] = []
    for spec in GOAL_SPECS:
        goal, sub = spec["goal"], spec["subtract"]
        row: dict[str, dict] = {}
        n_clear = 0
        for client in ordered_clients:
            # One variant entry per param, index-aligned with spec["params"] so the
            # detail table can render CODE/NOCODE as their own rows; missing fits
            # carry effective=None.
            variants = []
            for param in spec["params"]:
                est = value.get(param, {}).get(client)
                eff = None if est is None else est - sub
                variants.append({
                    "label": _variant_label(param),
                    "param": param,
                    "raw": est,
                    "effective": eff,
                    "clears": eff is not None and eff <= goal,
                    "missing": est is None,
                })
            no_data = any(v["missing"] for v in variants)
            clears = (not no_data) and all(v["clears"] for v in variants)
            row[client] = {"variants": variants, "clears": clears, "no_data": no_data}
            if clears:
                n_clear += 1
        matrix[spec["key"]] = row
        # Diff vs the current (osaka baseline) cost, same green=down/red=up coding
        # as the proposal/Trends tables. None when the baseline is non-numeric.
        current = current_by_param.get(spec["current_param"], "—")
        cur_n = int(current) if str(current).lstrip("-").isdigit() else None
        diff_pct = round((goal - cur_n) / cur_n * 100) if cur_n else None
        goals.append({
            "key": spec["key"],
            "goal": goal,
            "subtract": sub,
            "current": current,
            "diff_pct": diff_pct,
            "n_clear": n_clear,
            "n_total": len(ordered_clients),
            "variant_labels": [_variant_label(p) for p in spec["params"]],
        })

    return {
        "clients": ordered_clients,
        "goals": goals,
        "matrix": matrix,
    }


def _goal_param_meta() -> dict[str, dict]:
    """Map each estimated param that feeds a goal to its goal context."""
    meta: dict[str, dict] = {}
    for spec in GOAL_SPECS:
        for p in spec["params"]:
            meta[p] = {"goal_key": spec["key"], "goal": spec["goal"],
                       "subtract": spec["subtract"], "variant": _variant_label(p)}
    return meta


def _clean_cell(v) -> str:
    return "" if v is None or (isinstance(v, float) and pd.isna(v)) else str(v)


def _to_float(v) -> float | None:
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(f) else f


def _candidate_label(row) -> str:
    """Readable label for one candidate combo (the row's own fit triple + factors)."""
    core = " · ".join(p for p in (
        _clean_cell(row.get("test_name")),
        _clean_cell(row.get("target_opcode")),
        _clean_cell(row.get("model_coef_name")),
    ) if p)
    extras = []
    am = _clean_cell(row.get("param_account_mode")).replace("AccountMode.", "")
    if am:
        extras.append(am)
    slots = _clean_cell(row.get("param_existing_slots"))
    if slots:
        extras.append(f"slots={slots}")
    op = _clean_cell(row.get("param_opcode"))
    if op and op != _clean_cell(row.get("target_opcode")):
        extras.append(op)
    return f"{core} ({', '.join(extras)})" if extras else (core or "—")


def collect_goal_combos(gasfit: Path) -> dict[str, dict]:
    """Per (goal param, client) candidate model combos for the per-cell detail pages.

    Each estimated param that feeds a goal gets a page listing, per client, every
    candidate fit evm-gasfit considered (``new_gas_all_params.csv``) with its proposed
    gas and fit stats; the selected (winning) combo is flagged. Duplicate candidate
    rows (same combo + value) are collapsed, OR-ing the winner flag."""
    meta = _goal_param_meta()
    ap = pd.read_csv(gasfit / "new_gas_all_params.csv")
    out: dict[str, dict] = {}
    for param, pmeta in meta.items():
        g = ap[(ap["gas_param"] == param) & ap["client_name"].notna()
               & (ap["client_name"].astype(str) != "")]
        if g.empty:
            continue
        by_client: dict[str, list] = {}
        for client in sorted(g["client_name"].unique()):
            seen: dict[tuple, dict] = {}
            order: list[dict] = []
            for _, r in g[g["client_name"] == client].iterrows():
                key = tuple(_clean_cell(r.get(c)) for c in _PROV_COMBO_COLS)
                win = str(r.get("is_winner", "")).strip().lower() in ("true", "1")
                if key in seen:
                    seen[key]["is_winner"] = seen[key]["is_winner"] or win
                    continue
                combo = {
                    "label": _candidate_label(r),
                    "gas": int(r["new_gas_rounded"]),
                    "rsquared": _to_float(r.get("rsquared")),
                    "pvalue": _to_float(r.get("pvalue")),
                    "runtime_ms": _to_float(r.get("runtime_ms")),
                    "poor_fit": str(r.get("poor_fit", "")).strip().lower() in ("true", "1"),
                    "is_winner": win,
                }
                seen[key] = combo
                order.append(combo)
            # Winner first, then cheapest proposed gas.
            order.sort(key=lambda c: (not c["is_winner"], c["gas"]))
            by_client[client] = order
        out[param] = {
            "param": param,
            "goal_key": pmeta["goal_key"],
            "goal": pmeta["goal"],
            "subtract": pmeta["subtract"],
            "variant": pmeta["variant"],
            "clients": sorted(by_client),
            "by_client": by_client,
        }
    return out


def _ordered_unique(values) -> list:
    """First-appearance-ordered de-dup of a non-empty string column."""
    return list(dict.fromkeys(v for v in values if isinstance(v, str) and v))


def _derived_formula(spec) -> str:
    """The expression string for one ``fit.yaml`` ``derived`` entry (which is
    either a bare string or a ``{formula: ...}`` mapping)."""
    return spec["formula"] if isinstance(spec, dict) else str(spec)


def collect_param_map(gasfit: Path, fit_cfg: dict) -> dict:
    """The parameter→provenance reference for the methodology page.

    ``estimated`` lists one row per fitted gas param — the presets, target
    opcodes, fixtures, and model coefficient that feed its NNLS fits, aggregated
    over *every* candidate combo in ``new_gas_all_params.csv`` (not just the
    winner). ``derived`` lists the params computed from others, with the verbatim
    ``fit.yaml`` formula. Both preserve first-appearance / declaration order so
    the tables stay stable across re-fits."""
    derived_cfg = fit_cfg.get("derived") or {}
    derived = [
        {"param": name, "formula": _derived_formula(spec)}
        for name, spec in derived_cfg.items()
    ]

    estimated: list[dict] = []
    csv = gasfit / "new_gas_all_params.csv"
    if csv.exists():
        ap = pd.read_csv(csv)
        ap = ap[ap["client_name"].notna() & (ap["client_name"].astype(str) != "")]
        for param in _ordered_unique(ap["gas_param"]):
            if param in derived_cfg:
                continue  # a derived param can also carry stray fitted rows
            g = ap[ap["gas_param"] == param]
            presets = _ordered_unique(
                re.sub(r"^presets\[(.*)\]$", r"\1", s)
                for s in g["source_label"]
            )
            estimated.append({
                "param": param,
                "presets": presets,
                "opcodes": _ordered_unique(g["target_opcode"]),
                "fixtures": _ordered_unique(g["test_name"]),
                "coef": _ordered_unique(g["model_coef_name"]),
            })

    return {"estimated": estimated, "derived": derived}


# --------------------------------------------------------------------------- #
# Run discovery
# --------------------------------------------------------------------------- #
def discover_runs() -> list[dict]:
    """Every archived run, newest first; falls back to a synthetic live run."""
    runs: list[dict] = []
    if RUNS.is_dir():
        dirs = sorted(
            (p for p in RUNS.iterdir() if p.is_dir()), key=lambda p: p.name, reverse=True
        )
        for i, d in enumerate(dirs):
            fit = d / "fit.yaml"
            runs.append(_make_run(
                run_id=d.name,
                gasfit=d / "gasfit",
                raw_meta=d / "raw_meta.json",
                fit=fit if fit.exists() else FIT,
                index=i,
            ))
    if not runs:
        # No archive yet — render straight from the live gasfit outputs. As the
        # sole (latest) run it goes to the docs root, so its id is cosmetic.
        runs.append(_make_run("live", GASFIT, RAW / "meta.json", FIT, 0))
    return runs


def _make_run(run_id, gasfit, raw_meta, fit, index):
    is_latest = index == 0
    return {
        "run_id": run_id,
        "gasfit": gasfit,
        "raw_meta": raw_meta,
        "fit": fit,
        "is_latest": is_latest,
        "out_dir": OUT if is_latest else OUT / "runs" / run_id,
        "root_prefix": "" if is_latest else "../../",
        "figs_pruned": index >= KEEP_FULL_FIGS,
        "label": run_label(raw_meta),
    }


def runs_for_page(runs: list[dict], current: dict, page_file: str) -> list[dict]:
    """Dropdown entries for one page: link each run to the same page in that run."""
    rp = current["root_prefix"]
    entries = []
    for r in runs:
        target = rp + ("" if r["is_latest"] else f"runs/{r['run_id']}/") + page_file
        entries.append({
            "run_id": r["run_id"],
            "label": r["label"],
            "is_current": r["run_id"] == current["run_id"],
            "href": target,
        })
    return entries


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
def build_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["sci"] = lambda v: f"{v:.3e}"
    env.filters["g4"] = lambda v: f"{v:.4g}"
    return env


def copy_static() -> None:
    OUT.mkdir(exist_ok=True)
    # Disable GitHub Pages' Jekyll processing so files/dirs with leading
    # underscores are served verbatim instead of being silently dropped.
    (OUT / ".nojekyll").touch()
    for asset in ASSETS.iterdir():
        shutil.copy2(asset, OUT / asset.name)


def clear_stale_outputs() -> None:
    """Drop generated pages/figs so removed runs leave no orphans behind.

    Wipes the per-run tree and the figs dir wholesale, plus the latest run's
    top-level pages; static assets are recopied by copy_static()."""
    if (OUT / "runs").exists():
        shutil.rmtree(OUT / "runs")
    if (OUT / "figs").exists():
        shutil.rmtree(OUT / "figs")
    for page_file in PAGES.values():
        (OUT / page_file).unlink(missing_ok=True)
    (OUT / "trends.html").unlink(missing_ok=True)  # singleton cross-run page
    (OUT / "goals.html").unlink(missing_ok=True)  # singleton page
    for f in OUT.glob("goal_*.html"):  # per-param combo detail pages
        f.unlink()


def render_run(env: Environment, run: dict, runs: list[dict]) -> None:
    out = run["out_dir"]
    out.mkdir(parents=True, exist_ok=True)
    gasfit = run["gasfit"]
    meta = load_meta(run["raw_meta"])

    def common(page: str) -> dict:
        return {
            "meta": meta,
            "page": page,
            "runs": runs_for_page(runs, run, PAGES[page]),
            "is_latest": run["is_latest"],
            "root_prefix": run["root_prefix"],
        }

    # Copy this run's figures next to its pages (relative figs/... paths resolve).
    # The proposal figs (heatmap + provenance PNGs) are skipped — both are now
    # rendered as themed HTML tables (build_proposal_heatmap / build_provenance_heatmap).
    figs_src = gasfit / "figs"
    if figs_src.exists():
        shutil.copytree(
            figs_src, out / "figs", dirs_exist_ok=True,
            ignore=shutil.ignore_patterns("proposal"),
        )

    # Landing page — static narrative. No run-bar here (runs=None): the overview
    # is run-agnostic, so the dropdown would be misleading.
    proposed = parse_proposed_table(gasfit)
    index_ctx = common("index")
    index_ctx["runs"] = None
    (out / PAGES["index"]).write_text(env.get_template("index.html").render(
        **index_ctx,
    ))

    # New-gas page — the headline parameter table is re-rendered as a styled
    # (Δ-colored) table from the parsed rows; everything else renders wholesale.
    # Split the report into the intro (before the table) and the rest (from the
    # next ``## `` heading on), dropping the markdown table in between.
    report = (gasfit / "new_gas_proposal.md").read_text()
    report = drop_section(strip_first_h1(report), "## Contents")
    intro_md, _, tail_md = report.partition("## Proposed gas parameters\n")
    rest_md = re.sub(r"\A.*?(?=^## )", "", tail_md, count=1, flags=re.S | re.M)
    # Swap evm-gasfit's heatmap.png for a themed HTML table (kept inline via a
    # sentinel that survives markdown as a bare paragraph). Falls back to the PNG
    # if the source CSV is missing.
    current_by_param = {r["param"]: r["current"] for r in proposed}
    heatmap_html = build_proposal_heatmap(gasfit, current_by_param)
    if heatmap_html:
        rest_md = rest_md.replace("![](figs/proposal/heatmap.png)", "HEATMAPSLOTTOKEN")
    # Same treatment for the per-param worst-case provenance plots. Each gas
    # param's <details> block carries an M1…Mn legend only when it has enough
    # combos; without one, the heatmap labels rows by their varying components.
    prov_legend = {
        m.group(1)
        for m in re.finditer(r"<summary><code>(\w+)</code>.*?</details>", rest_md, re.S)
        if "| Label | Combo |" in m.group(0)
    }
    prov_html: dict[str, str] = {}
    for p in dict.fromkeys(re.findall(r"provenance__(\w+)\.png", rest_md)):
        html = build_provenance_heatmap(gasfit, p, current_by_param, p in prov_legend)
        if html:
            token = f"PROVHEATMAP{p}TOKEN"
            rest_md = rest_md.replace(f"![](figs/proposal/provenance__{p}.png)", token)
            prov_html[token] = html
    rest_html = md_to_html(rest_md)
    if heatmap_html:
        rest_html = rest_html.replace("<p>HEATMAPSLOTTOKEN</p>", heatmap_html)
    for token, html in prov_html.items():
        rest_html = rest_html.replace(f"<p>{token}</p>", html)
    (out / PAGES["new-gas"]).write_text(env.get_template("new_gas.html").render(
        intro_html=md_to_html(intro_md),
        proposed=proposed,
        rest_html=rest_html,
        **common("new-gas"),
    ))

    # Runtime page — filterable per-fit sections.
    (out / PAGES["runtime"]).write_text(env.get_template("runtime.html").render(
        figs_pruned=run["figs_pruned"], **parse_runtime(gasfit), **common("runtime"),
    ))

    # Glue page — filterable per (client, glue_opcode) sections + appendix.
    (out / PAGES["glue"]).write_text(env.get_template("glue.html").render(
        figs_pruned=run["figs_pruned"], **parse_glue(gasfit), **common("glue"),
    ))

    # Methodology page — static narrative, config-driven values from the run's
    # fit, plus the parameter→provenance map built from this run's fits.
    fit_cfg = yaml.safe_load(run["fit"].read_text())
    (out / PAGES["methodology"]).write_text(env.get_template("methodology.html").render(
        fit=fit_cfg, param_map=collect_param_map(gasfit, fit_cfg),
        **common("methodology"),
    ))


def main() -> None:
    OUT.mkdir(exist_ok=True)
    clear_stale_outputs()
    env = build_env()
    runs = discover_runs()
    for run in runs:
        render_run(env, run, runs)

    # Trends — one cross-run page at the docs root (not per run, so it's kept out
    # of PAGES and the run dropdown). runs=None hides the run-bar in base.html;
    # the newest run supplies the reproducibility footer.
    (OUT / "trends.html").write_text(env.get_template("trends.html").render(
        trends=collect_trends(runs),
        meta=load_meta(runs[0]["raw_meta"]),
        page="trends",
        root_prefix="",
        runs=None,
    ))

    # Goals — one latest-only page at the docs root: per-client estimates vs fixed
    # target gas values. Singleton like Trends (kept out of PAGES / the dropdown).
    latest_gasfit = runs[0]["gasfit"]
    latest_meta = load_meta(runs[0]["raw_meta"])
    (OUT / "goals.html").write_text(env.get_template("goals.html").render(
        goals=collect_goals(latest_gasfit),
        meta=latest_meta,
        page="goals",
        root_prefix="",
        runs=None,
    ))
    # One detail page per goal param (docs root, so base.html's bare nav links work):
    # the candidate model combos behind each client's value. Linked from the Goals
    # per-client detail cells.
    for param, detail in collect_goal_combos(latest_gasfit).items():
        (OUT / f"goal_{param}.html").write_text(env.get_template("goal_detail.html").render(
            detail=detail,
            meta=latest_meta,
            page="goals",
            root_prefix="",
            runs=None,
        ))

    copy_static()
    print(f"Built site → {OUT} ({len(runs)} run(s))")


if __name__ == "__main__":
    main()
