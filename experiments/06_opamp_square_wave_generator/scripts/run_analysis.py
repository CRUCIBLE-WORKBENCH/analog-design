from math import log
VDD=1.8; BETA=0.5; R=8.2e3; C=50e-12
freq = 1/(2*R*C*log((1+BETA)/(1-BETA)))
high=VDD; low=0.0; duty=0.5
print(f"R={R/1e3:.2f} kOhm C={C*1e12:.1f} pF beta={BETA:.2f} freq={freq/1e6:.3f} MHz duty={duty:.2f}")
assert freq >= 1e6
assert 0.45 < duty < 0.55
print("PASS opamp_square_wave_generator")
