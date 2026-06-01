# CLAUDE.md — maintaining eip-8038-repricing

Pipeline: `benchmarkoor-fetch` → `evm-gasfit` → `build_site.py` → `docs/` (GitHub Pages, `main`, `/docs`).
README.md has user-facing setup/run docs — this file is for *changing* the repo. Don't duplicate the README.

## Layout that matters
- `fetch.yaml` — what benchmark data to pull (pinned suites, fork).
- `fit.yaml` — the estimation: anchor, clients, cost-table fork, op presets, glue.
- `scripts/build_site.py` — renders `site_src/templates/` → `docs/`, parses `data/gasfit/` reports (now per run dir).
- `scripts/archive_run.py` — snapshots a fit into `data/runs/<run_id>/` (run by `make gasfit`). Owned elsewhere; see Run history.
- `scripts/clean_run.py` — deletes a run dir + re-renders (`make clean-run RUN_ID=<id>`).
- `site_src/{templates,assets}/` — edit these, never `docs/` (regenerated).
- `data/raw/` — fetched inputs; `data/gasfit/` — estimation outputs; `data/runs/<run_id>/` — committed per-run archive (the history). All committed.

## Common tasks
- **Re-run end-to-end:** `make` (= `make fetch gasfit site`). `make clean` wipes `data/raw`, `data/gasfit`, `docs/` — NOT `data/runs/` (history preserved).
- **Rebuild site only** (after template/asset edits): `make site` — no token needed.
- **Preview locally:** `make serve` (serves `docs/` on `:8000`; override with `PORT=…`).
- **Re-fit only** (after `fit.yaml` edits): `make gasfit && make site` (still holds; `make gasfit` now also archives the fit — see Run history).
- **Delete a run:** `make clean-run RUN_ID=<id>` (`scripts/clean_run.py`) — removes `data/runs/<id>/` and re-renders.
- **Change the op set:** edit `models.presets` in `fit.yaml` (preset names; 101 available in evm-gasfit). New 8038 gas params that error as missing in the osaka table go under `new_params` (this repo already sets `COLD_ACCOUNT_*`, `ACCOUNT_WRITE`, `STORAGE_WRITE`, plus the `derived` block).
- **Re-pin suites:** `benchmarkoor-fetch suites --network <n> --fork <f> --test-type <t>` → paste hashes into `fetch.yaml`. `run_id_pattern` is a full regex match.
- **Deploy:** commit the new/updated `data/runs/<run_id>/` + regenerated `docs/` (and any changed `data/raw`/`data/gasfit`), push `main`. No CI. (GitHub Pages → Settings → Pages: source `main` / `/docs`.)

## Gotchas
- **secrets.json** (gitignored, repo root): `{ "benchmarkoor_bearer_token": "bmk_..." }`. Makefile reads it with `jq`, exports `BENCHMARKOOR_TOKEN`. Never put the token in `fetch.yaml` (loader rejects it). Never commit it.
- **Gitignored raw bulk:** `runtimes.csv`, `bench_data.parquet`, `trace.parquet` are NOT committed (regenerate with `make fetch`). `data/raw/meta.json` + `opcounts.json` ARE committed (meta drives the site footer; opcounts feeds glue).
- **build_site.py parsing is brittle by design.** It regex-parses the exact markdown shape of evm-gasfit's reports — `<details><summary>… NNLS regression summary</summary>` blocks, `## `/`### ` heading splits, the `## Proposed gas parameters` table. If an evm-gasfit upgrade changes report formatting, the runtime/glue/new-gas pages silently lose sections. After bumping `evm-gasfit`, eyeball those three pages.
- **Two forks, intentionally:** benchmarks run on `amsterdam` (`fetch.yaml`); gas-cost table is `osaka` (`fit.yaml`). Not a typo.
- **`ethrex` is dropped by omission** from `clients` in `fit.yaml`. Per-op fixture exclusions live inside each preset's built-in `filter_by` — not in a pre-fit script.

## Run history
- **`data/runs/<run_id>/`** is the committed archive — one dir per fit. `run_id` = `data_window.end` from `meta.json` (with `:` and `-` stripped) + first suite hash, e.g. `20260529T234448Z_3182dda7b93dee61`. Newest sorts last lexically. Re-fitting the same data window overwrites the same dir (no dupes).
- A run dir holds `meta.json`, `fit.yaml`, the markdown reports, the CSVs, and `figs/{proposal,runtime,glue}/`.
- **`make gasfit` runs evm-gasfit THEN `scripts/archive_run.py`** — archive_run snapshots `data/gasfit/` + `data/raw/meta.json` + `fit.yaml` into the run dir, then prunes `figs/runtime/` + `figs/glue/` from every run beyond the 5 newest (keeping `figs/proposal/`). So those older runtime/glue pages render text/tables but no plots.
- **`make site`** (`build_site.py`) renders every run dir: latest → `docs/*.html` (+ `docs/figs/`); older → `docs/runs/<run_id>/*.html` (+ `docs/runs/<run_id>/figs/`). Older pages sit beside their own `figs/` so relative image paths resolve without rewriting. A dropdown banner switches runs across all five pages. Stale `docs/runs/` is cleared at the start of each build.
- **`make clean-run RUN_ID=<id>`** (`scripts/clean_run.py`) recursively removes the run dir and re-renders. No "latest pointer" to fix up (latest = newest dir; no `results.json` here, unlike eip-2780).

## Site pages (data coupling)
- `index` — static + headline up/down counts from the proposal table.
- `new-gas` — wholesale render of `new_gas_proposal.md` (minus H1 + Contents).
- `runtime` — filterable sections parsed from `runtime_estimation_autogenerated_report.md`; client-side JS filter (`runtime_filter.js`).
- `glue` — filterable sections from `glue_results.csv` + `glue_opcodes_autogenerated_report.md`.
- `trends` — **cross-run, singleton page** (not per run): rendered once to `docs/trends.html` via `collect_trends()` in `build_site.py`, which unions every run's per-client selected fits (`new_gas_all_params.csv`, filtered to the `selected_*` triple) plus the binding proposal (`new_gas.csv`). Data is embedded as JSON and drawn client-side by `trends.js` with vendored Chart.js (`assets/chart.umd.min.js`). Deliberately kept **out of `PAGES`** and the run dropdown (the run-bar is hidden via `runs=None`); the nav link in `base.html` uses `{{ root_prefix }}` so older-run pages point back to the single root copy. Section 1 = latest-vs-previous delta table + a diverging Δ% bar chart (one bar per param·client, green=faster/lower, red=regression; with a "combo changed" badge from the per-client selected fit, and the **binding/worst-case** client's row highlighted + its bar outlined — from `new_gas.csv`'s `client_name` for the latest run); section 2 = one line chart per **estimated** param (clients as lines). Both sections cover estimated params only — the 3 derived params have no per-client series, so they're excluded everywhere (and from the parameter filter); their `binding` values are emitted by `collect_trends()` but unused. Delta-table values carry a `*` when evm-gasfit's own `poor_fit` flag (its New-gas R²/p-value thresholds) is set for that (param, client, run) — sourced from the `poor_fit` column of `new_gas_all_params.csv`, not a threshold re-derived here. The footnote and asterisks only appear when a flag is actually set (none in the current data). The Δ% axis ticks are rounded (`pctTick` in `trends.js`) to avoid float-noise labels.
- `methodology` — static, but reads live values from `fit.yaml`.
