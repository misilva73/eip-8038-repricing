BENCHMARKOOR_TOKEN := $(shell jq -r .benchmarkoor_bearer_token secrets.json)
export BENCHMARKOOR_TOKEN

PORT ?= 8000

.PHONY: all fetch gasfit site serve clean clean-run

all:
	$(MAKE) fetch
	$(MAKE) gasfit
	$(MAKE) site

fetch:
	benchmarkoor-fetch run --config fetch.yaml --out data/raw/

gasfit:
	evm-gasfit run --config fit.yaml \
		--runtimes data/raw/runtimes.csv \
		--opcounts data/raw/opcounts.json \
		--out data/gasfit/
	python scripts/archive_run.py

site:
	python scripts/build_site.py

serve:
	python -m http.server $(PORT) --directory docs/

# Delete one archived run from data/runs/ and re-render. Usage:
#   make clean-run RUN_ID=20260529T234448Z_3182dda7b93dee61
clean-run:
	@test -n "$(RUN_ID)" || { echo "usage: make clean-run RUN_ID=<id>"; exit 2; }
	python scripts/clean_run.py "$(RUN_ID)"

# Preserves data/runs/ (the committed run history); wipes only fetched inputs,
# the live fit outputs, and the built site.
clean:
	rm -rf data/raw data/gasfit docs/
