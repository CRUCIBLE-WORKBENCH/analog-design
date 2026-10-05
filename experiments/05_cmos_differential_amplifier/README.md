# Experiment 05: CMOS Differential Amplifier

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

Sizes a differential pair and estimates differential gain, common-mode range, and CMRR.
