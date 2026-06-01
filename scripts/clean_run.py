#!/usr/bin/env python3
"""Delete an archived run directory and re-render the site.

Removes ``data/runs/<RUN_ID>/`` (the per-run archive snapshotted by
``scripts/archive_run.py`` during ``make gasfit``) and then re-renders the
whole site by invoking ``build_site.py``. There is no "latest pointer" to
maintain in this repo — the latest run is simply the newest directory under
``data/runs/`` — so deletion is just a recursive remove plus a rebuild.
``build_site.py`` clears stale ``docs/runs/`` output itself, so no extra
cleanup is needed here.

Usage (typically via ``make clean-run RUN_ID=<id>``):

    python scripts/clean_run.py <RUN_ID>

Run ids are the subdirectory names under ``data/runs/`` (also shown in the
dashboard run dropdown).
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = ROOT / "data" / "runs"
BUILD_SITE = ROOT / "scripts" / "build_site.py"


def main(argv: list[str]) -> int:
    if len(argv) != 1 or not argv[0].strip():
        print("usage: python scripts/clean_run.py <RUN_ID>", file=sys.stderr)
        return 2
    run_id = argv[0].strip()

    target = RUNS_DIR / run_id
    if not target.is_dir():
        print(f"error: no archived run at {target}", file=sys.stderr)
        existing = (
            sorted(p.name for p in RUNS_DIR.iterdir() if p.is_dir())
            if RUNS_DIR.is_dir()
            else []
        )
        if existing:
            print("available run ids:", file=sys.stderr)
            for rid in existing:
                print(f"  {rid}", file=sys.stderr)
        return 1

    shutil.rmtree(target)
    print(f"Deleted {target.relative_to(ROOT)}")

    # Re-render the site (build_site clears stale docs/runs/ output itself).
    print("Rebuilding site...")
    return subprocess.run([sys.executable, str(BUILD_SITE)], cwd=ROOT).returncode


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
