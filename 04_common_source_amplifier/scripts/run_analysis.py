from math import pi
VDD=1.8; ID=100e-6; VOV=0.20; LAMBDA=0.08; RD=7.5e3; CL=100e-15
gm=2*ID/VOV; ro=1/(LAMBDA*ID); rout=1/(1/RD+1/ro); gain=-gm*rout
VOUT=VDD-ID*RD; pole=1/(2*pi*rout*CL)
print(f"gm={gm*1e3:.2f} mS ro={ro/1e3:.1f} kOhm gain={gain:.2f} V/V VoutQ={VOUT:.2f} V pole={pole/1e6:.1f} MHz")
assert -8.0 < gain < -5.0
assert 0.7 < VOUT < 1.2
assert pole > 100e6
print("PASS common_source_amplifier")
