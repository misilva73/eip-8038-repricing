#!/usr/bin/env python3
"""Archive the current gasfit outputs as a dated run under ``data/runs/``.

Invoked by ``make gasfit`` after ``evm-gasfit``. Snapshots ``data/gasfit/`` plus
``data/raw/meta.json`` and ``fit.yaml`` into ``data/runs/<run_id>/``, so the site
can accumulate a history of runs that the run-selector dropdown switches between.

``run_id`` is the data-window end timestamp (``:``/``-`` stripped, so it is
filesystem-safe and sorts chronologically) plus the first suite hash. Re-fitting
the same data window overwrites the same run dir rather than duplicating it.

To bound repo size, only the ``KEEP_FULL_FIGS`` newest runs keep the heavy
runtime/glue figures; older runs keep their (small) proposal figures and all
text/tables, but their runtime/glue plots are pruned.
"""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
GASFIT = ROOT / "data" / "gasfit"
RUNS = ROOT / "data" / "runs"
FIT = ROOT / "fit.yaml"

# Newest N runs keep runtime/glue figs; older runs keep only the proposal figs.
KEEP_FULL_FIGS = 5


def run_id_from_meta(meta: dict) -> str:
    """``<data_window.end stripped of :/->``_``<first suite hash>``."""
    end = (meta.get("data_window") or {}).get("end") or meta.get("fetched_at") or "unknown"
    stamp = re.sub(r"[:\-]", "", str(end))
    suites = meta.get("suites") or []
    token = ""
    if suites:
        first = suites[0]
        h = first.get("suite_hash") if isinstance(first, dict) else first
        if h:
            token = f"_{h}"
    return f"{stamp}{token}"


def archive() -> str:
    meta = json.loads((RAW / "meta.json").read_text())
    run_id = run_id_from_meta(meta)
    dest = RUNS / run_id
    # Re-fit of the same data window overwrites in place (no duplicate runs).
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    shutil.copytree(GASFIT, dest / "gasfit")
    shutil.copy2(RAW / "meta.json", dest / "raw_meta.json")
    if FIT.exists():
        shutil.copy2(FIT, dest / "fit.yaml")
    print(f"Archived run -> {dest.relative_to(ROOT)}")
    return run_id


def prune_old_figs() -> None:
    """Drop runtime/glue figs from every run beyond the newest KEEP_FULL_FIGS."""
    runs = sorted(
        (p for p in RUNS.iterdir() if p.is_dir()), key=lambda p: p.name, reverse=True
    )
    for old in runs[KEEP_FULL_FIGS:]:
        for sub in ("runtime", "glue"):
            figdir = old / "gasfit" / "figs" / sub
            if figdir.exists():
                shutil.rmtree(figdir)
                print(f"Pruned {figdir.relative_to(ROOT)} (beyond newest {KEEP_FULL_FIGS})")


def main() -> None:
    RUNS.mkdir(parents=True, exist_ok=True)
    archive()
    prune_old_figs()


if __name__ == "__main__":
    main()
