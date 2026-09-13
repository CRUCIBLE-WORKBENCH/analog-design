from math import log10
VDD=1.8; ISS=200e-6; ID=ISS/2; VOV=0.20; RD=6e3; LAMBDA=0.08; RSS=500e3
gm=2*ID/VOV; ro=1/(LAMBDA*ID); rout=1/(1/RD+1/ro); adm=-gm*rout
acm=-rout/(2*RSS); cmrr=abs(adm/acm); cmrr_db=20*log10(cmrr)
vcm_min=0.45+VOV+0.20; vcm_max=VDD-ID*RD+0.45
print(f"Ad={adm:.2f} V/V Acm={acm:.4f} CMRR={cmrr_db:.1f} dB VCM=[{vcm_min:.2f},{vcm_max:.2f}] V")
assert abs(adm) > 4.0
assert cmrr_db > 55
assert vcm_min < 0.9 and vcm_max > 1.0
print("PASS cmos_differential_amplifier")
