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
    figs_src = gasfit / "figs"
    if figs_src.exists():
        shutil.copytree(figs_src, out / "figs", dirs_exist_ok=True)

    # Landing page — static narrative + headline counts.
    proposed = parse_proposed_table(gasfit)
    n_up = sum(1 for r in proposed if r["diff"].startswith("+"))
    n_down = sum(1 for r in proposed if r["diff"].startswith("-"))
    (out / PAGES["index"]).write_text(env.get_template("index.html").render(
        proposed=proposed, n_up=n_up, n_down=n_down, **common("index"),
    ))

    # New-gas page — wholesale render of the proposal report.
    report = (gasfit / "new_gas_proposal.md").read_text()
    report = drop_section(strip_first_h1(report), "## Contents")
    (out / PAGES["new-gas"]).write_text(env.get_template("new_gas.html").render(
        report_html=md_to_html(report), **common("new-gas"),
    ))

    # Runtime page — filterable per-fit sections.
    (out / PAGES["runtime"]).write_text(env.get_template("runtime.html").render(
        figs_pruned=run["figs_pruned"], **parse_runtime(gasfit), **common("runtime"),
    ))

    # Glue page — filterable per (client, glue_opcode) sections + appendix.
    (out / PAGES["glue"]).write_text(env.get_template("glue.html").render(
        figs_pruned=run["figs_pruned"], **parse_glue(gasfit), **common("glue"),
    ))

    # Methodology page — static narrative, config-driven values from the run's fit.
    fit_cfg = yaml.safe_load(run["fit"].read_text())
    (out / PAGES["methodology"]).write_text(env.get_template("methodology.html").render(
        fit=fit_cfg, **common("methodology"),
    ))


def main() -> None:
    OUT.mkdir(exist_ok=True)
    clear_stale_outputs()
    env = build_env()
    runs = discover_runs()
    for run in runs:
        render_run(env, run, runs)
    copy_static()
    print(f"Built site → {OUT} ({len(runs)} run(s))")


if __name__ == "__main__":
    main()
