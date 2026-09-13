# Experiment 02: Properly Biased Short-Channel nMOSFET

## Contents

- `scripts/run_analysis.py`: executable analytical design and verification flow.
- `src/design_model.sv`: SystemVerilog real-number/reference model for future Crucible porting.
- `spice/*.cir`: self-contained SPICE deck(s), including local MOS models.
- `Makefile`: runs Python verification now and SPICE when `ngspice` is available.
- `VERIFICATION.md`: verification plan and checks.

## Run

```sh
make test
make spice
```

Designs an 180 nm nMOS current sink biased in saturation with explicit margin checks.
