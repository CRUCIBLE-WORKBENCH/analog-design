from itertools import product
VDD=1.8; RN=8e3; RP_WEAK=60e3
def cmos_nand(a,b): return int(not (a and b))
def pseudo_level(a,b):
    if a and b:
        return VDD * RN/(RN + RP_WEAK)
    return VDD
for a,b in product([0,1],[0,1]):
    y=cmos_nand(a,b); vp=pseudo_level(a,b)
    print(f"A={a} B={b} CMOS={y} pseudo_nmos={vp:.3f} V")
assert pseudo_level(1,1) < 0.30
assert all(cmos_nand(a,b)==(0 if a and b else 1) for a,b in product([0,1],[0,1]))
print("PASS cmos_pseudo_nmos_nand")
