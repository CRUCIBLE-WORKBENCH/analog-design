# Analog CMOS Experiments

Six analog CMOS experiments — MOS device modelling, logic families, amplification, and oscillation. Each experiment pairs a hand-derived design-equation check in Python against a SPICE deck run through `ngspice`, so the theory and the simulation have to agree before a result is accepted.

The experiments drive `ngspice` and Python from `PATH`, so they run under any toolchain that provides them. See [Toolchain](#toolchain) for getting those tools from `igny` (Crucible) instead of installing them by hand.

## The suite

| Experiment | What it covers |
|---|---|
| [`01_mosfet_parameter_extraction`](01_mosfet_parameter_extraction/) | Extract threshold voltage, transconductance parameter, and channel-length modulation from simulated device characteristics |
| [`02_short_channel_nmos_bias`](02_short_channel_nmos_bias/) | Bias a short-channel NMOS and quantify the departure from the long-channel square law |
| [`03_cmos_pseudo_nmos_nand`](03_cmos_pseudo_nmos_nand/) | Compare a static CMOS NAND against its pseudo-NMOS counterpart — noise margin, static current, area |
| [`04_common_source_amplifier`](04_common_source_amplifier/) | Small-signal gain, bandwidth, and bias sensitivity of a common-source stage |
| [`05_cmos_differential_amplifier`](05_cmos_differential_amplifier/) | Differential and common-mode gain, CMRR, and input range of a CMOS diff pair |
| [`06_opamp_square_wave_generator`](06_opamp_square_wave_generator/) | An astable op-amp relaxation oscillator — period from the RC network, verified against transient simulation |

## Structure of an experiment folder

```text
NN_experiment_name/
├── README.md            aim, theory, procedure, expected result
├── VERIFICATION.md      the measured numbers from a real run
├── Makefile             `make` runs the whole experiment
├── spice/design.cir     the SPICE deck
├── src/design_model.sv  SystemVerilog behavioural model
└── scripts/run_analysis.py   design-equation check and plotting
```

## Running an experiment

```bash
cd 01_mosfet_parameter_extraction
make
```

`make` runs the Python design-equation check. `make spice` runs the SPICE decks, and skips them with a notice if `ngspice` is not on `PATH`. Both honour overrides — `make PYTHON=python NGSPICE=/opt/bin/ngspice`.

## Toolchain

This repository is **not** a Crucible workspace — there is no `crucible.toml` or `crucible.lock`, so `igny workspace sync` does not apply here. The simplest way to get the tools is an `igny` environment shell, which puts every bound tool on `PATH` so the Makefiles run unchanged:

```bash
igny env create analog
igny env activate analog
igny tool install ngspice
igny env shell analog
# inside the subshell:
cd 01_mosfet_parameter_extraction && make && make spice
```

Making this a locked workspace — `igny workspace create`, then `igny workspace lock` — is open work.

## Paired document repository

The published write-up for these experiments lives in its own repository, [`analog_whitepapers`](https://gitlab.com/ignytion_io-group/ignytion_ae/analog_whitepapers.git), checked out here as the `analog_whitepapers/` submodule and pinned to an exact document revision.

```bash
git clone --recurse-submodules https://gitlab.com/ignytion_io-group/ignytion_ae/analog_experiments.git
```

or, in an existing clone:

```bash
git submodule update --init -- analog_whitepapers
```

The pairing is two-way and deliberately circular: `analog_whitepapers` carries this repository back as a submodule, so a document can always be traced to the experiment revision behind its numbers. On that side the back-reference is declared with `update = none`, which is what stops `git clone --recursive` from following the pair back and forth forever. `--recursive` is therefore safe from here.

`crucible_docs/` holds the same whitepaper alongside its PPTX source and predates the submodule. The submodule is the published, version-pinned copy; treat it as canonical.

## Contact

- Product information — [ignytion.io](https://www.ignytion.io)
- Support and questions — [info@ignytion.io](mailto:info@ignytion.io)

© 2026 Ignytion IO
