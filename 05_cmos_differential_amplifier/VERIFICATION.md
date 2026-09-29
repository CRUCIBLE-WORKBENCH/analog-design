# Verification Methodology

- Analytical Python flow estimates differential gain, common-mode gain, CMRR, and input common-mode range.
- Assertions check gain, CMRR, and headroom constraints.
- SPICE AC/operating-point deck is included for later simulator-backed validation.
- SystemVerilog real-number helper function captures the differential gain equation.
