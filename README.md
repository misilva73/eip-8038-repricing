# EIP-8038 Repricing

A static, multi-page site summarising the [EIP-8038](https://eips.ethereum.org/EIPS/eip-8038)
gas-repricing analysis. The analysis fits NNLS regressions on EVM client benchmark
runtimes to propose new gas costs for the state-access operations touched by the EIP.

**Live site:** <https://misilva73.github.io/eip-8038-repricing/>

## Pipeline

```text
benchmarkoor-fetch  →  evm-gasfit  →  build_site.py  →  docs/  (GitHub Pages)
   (data/raw/)         (data/gasfit/)     (Jinja2)
```

1. **Fetch** — `benchmarkoor-fetch` pulls the pinned benchmark suites into `data/raw/`,
   driven by [fetch.yaml](fetch.yaml).
2. **Fit** — `evm-gasfit` runs the NNLS estimation (driven by [fit.yaml](fit.yaml)) and
   emits the proposal artifacts and reports into `data/gasfit/`.
3. **Build** — `scripts/build_site.py` renders the Jinja2 templates in `site_src/` into
   `docs/`, pulling structured data (CSVs, parsed reports) from `data/gasfit/`.
4. **Deploy** — GitHub Pages serves `docs/` from `main`.

`data/` is committed alongside `docs/` so the published site is self-contained and auditable.

## Setup

Requires Python ≥ 3.11, plus `make` and `jq`.

```bash
pip install -e .          # installs benchmarkoor-fetch, evm-gasfit, jinja2, pandas
```

### Benchmarkoor token

Fetching benchmark data needs a Benchmarkoor API key. Request your own key, then create
a gitignored `secrets.json` at the repo root:

```json
{ "benchmarkoor_bearer_token": "bmk_..." }
```

The `Makefile` reads it with `jq` and exports `BENCHMARKOOR_TOKEN` before invoking
`benchmarkoor-fetch`. The token must never live in `fetch.yaml` (the config loader
rejects it).

## Running

```bash
make fetch     # → data/raw/    (reads token from secrets.json)
make gasfit    # → data/gasfit/
make site      # renders site_src/templates → docs/, copies figures
make serve     # preview docs/ locally on http://localhost:8000 (override PORT=…)
# or end-to-end:
make
```

`make clean` removes `data/raw/`, `data/gasfit/`, and `docs/` (it preserves
`data/runs/`, the committed run history — see below).

## Run history

Each `make gasfit` archives the fit into `data/runs/<run_id>/` (committed), so
the dashboard accumulates a history of runs rather than just showing the latest.

- The site shows the **latest** run on its main pages; a dropdown banner switches
  to any previous run, updating every page at once.
- The **5 newest** runs keep all plots. Older runs keep their new-gas plots plus
  all text and tables, but drop the runtime and glue plots to bound repo size.
- Remove a run with `make clean-run RUN_ID=<id>` (deletes `data/runs/<id>/` and
  re-renders the site).

A run dir holds `meta.json`, `fit.yaml`, the markdown reports, the CSVs, and
`figs/{proposal,runtime,glue}/`.

## Layout

| Path | Purpose |
| --- | --- |
| `fetch.yaml` | benchmarkoor-fetch config (pinned suites, amsterdam fork) |
| `fit.yaml` | evm-gasfit config (anchor 1e8, osaka cost table, presets, glue on) |
| `scripts/build_site.py` | renders templates → `docs/`, copies figures |
| `scripts/clean_run.py` | deletes a run dir + re-renders (`make clean-run RUN_ID=<id>`) |
| `site_src/templates/` | Jinja2 templates (`base.html` + one per page) |
| `site_src/assets/` | `style.css`, `runtime_filter.js` |
| `data/raw/` | fetched benchmark inputs |
| `data/gasfit/` | estimation outputs (CSVs, reports, `figs/`) |
| `data/runs/<run_id>/` | committed per-run archive (one dir per fit; the site's history) |
| `docs/` | generated static site (served by GitHub Pages) |
