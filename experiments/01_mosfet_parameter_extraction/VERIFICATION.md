# Verification Methodology

- Analytical Python flow computes representative MOS parameters from stated process assumptions.
- Assertions check physically reasonable ranges and internal consistency, such as `Cgs > Cgd > 0`.
- SPICE deck is included for later simulator-backed checks when `ngspice` is available.
- SystemVerilog real-number helper functions are included for future Crucible-oriented modeling.
