from math import sqrt
VDD=1.8; VTH=0.45; MUCOX=260e-6; L=0.18e-6; ID=100e-6; VOV=0.20
W = 2*ID*L/(MUCOX*VOV*VOV)
VGS = VTH + VOV
VDS_MIN = VOV
VDS = 0.90
gm = 2*ID/VOV
sat_margin = VDS - VDS_MIN
print(f"W={W*1e6:.2f} um L={L*1e6:.2f} um VGS={VGS:.2f} V VDS={VDS:.2f} V")
print(f"ID={ID*1e6:.1f} uA gm={gm*1e3:.2f} mS saturation_margin={sat_margin:.2f} V")
assert W > 3e-6
assert VGS < VDD and sat_margin > 0.2
print("PASS short_channel_nmos_bias")
