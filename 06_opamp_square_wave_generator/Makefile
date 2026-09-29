PYTHON ?= python3
NGSPICE ?= ngspice

.PHONY: test run spice clean

test: run

run:
	$(PYTHON) scripts/run_analysis.py

spice:
	@if command -v $(NGSPICE) >/dev/null 2>&1; then for f in spice/*.cir; do echo "running $$f"; $(NGSPICE) -b $$f; done; else echo "ngspice not found; SPICE netlists are present but not executed"; fi

clean:
	rm -rf build
