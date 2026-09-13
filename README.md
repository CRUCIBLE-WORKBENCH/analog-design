# Analog Design Experiments

This repository contains analog and mixed-signal design experiments and learning
resources created using **Crucible by Ignytion IO**.

It is intended for students, educators, researchers, and engineers exploring analog
circuits, SPICE simulation, device behaviour, and design workflows.

## Repository Structure

```text
experiments/                         analog and mixed-signal experiments
  01_mosfet_parameter_extraction/    individual experiment directories
  ...
  06_opamp_square_wave_generator/
  crucible_docs/                     whitepapers and Crucible learning resources
LICENSE                              repository license
README.md                            repository overview
```

Generated simulation outputs, plots, reports, raw data, and local run logs are
intentionally not tracked. Recreate them locally from the source files when needed.

## Experiment Index

| No. | Experiment |
|---:|---|
| 01 | MOSFET parameter extraction |
| 02 | Short-channel NMOS bias |
| 03 | CMOS pseudo-NMOS NAND |
| 04 | Common-source amplifier |
| 05 | CMOS differential amplifier |
| 06 | Op-amp square-wave generator |

## Running Experiments

Each experiment is self-contained and typically includes:

```text
Makefile              command targets for the experiment
spice/design.cir      SPICE circuit deck
scripts/run_analysis.py
src/design_model.sv   mixed-signal/SystemVerilog model where applicable
README.md             experiment notes
VERIFICATION.md       verification notes
```

Most experiments can be run from their directory:

```bash
cd experiments/01_mosfet_parameter_extraction
make
```

You can also run the SPICE deck directly:

```bash
ngspice -b experiments/01_mosfet_parameter_extraction/spice/design.cir
```

## Prerequisites

| Workflow | Tools |
|---|---|
| SPICE simulation | `ngspice` |
| Analysis scripts | `python3` |
| Mixed-signal model review | SystemVerilog-capable tooling, where applicable |

With Crucible / Igny CLI, install tools into a workspace and run the same tool
commands through `igny run`:

```bash
igny env create analog-design
igny workspace create --env analog-design
igny tool install ngspice
```

## License

Unless otherwise stated, original materials developed by Ignytion IO in this repository
are licensed under the [Apache License 2.0](./LICENSE).

Third-party PDKs, device models, tools, libraries, and generated outputs remain subject
to their respective licences and are not relicensed by this repository.

Copyright 2026 Ignytion IO Private Limited.
