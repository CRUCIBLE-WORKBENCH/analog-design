# Verification Methodology

- Analytical Python flow sizes an nMOS device for the target current and overdrive.
- Assertions verify gate bias, device width, and saturation margin.
- SPICE operating-point deck is included for later `ngspice` validation.
- SystemVerilog real-number model documents the drain-current equation used by the analysis.
