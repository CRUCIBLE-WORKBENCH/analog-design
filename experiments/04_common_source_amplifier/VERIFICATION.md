# Verification Methodology

- Analytical Python flow checks bias point, small-signal gain, output headroom, and dominant pole estimate.
- Assertions constrain gain, quiescent output voltage, and bandwidth.
- SPICE AC/operating-point deck is included for later simulator-backed validation.
- SystemVerilog real-number helper function captures the gain equation.
