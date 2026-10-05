from math import isclose

EPS0 = 8.854e-12
EPS_OX = 3.9 * EPS0
TOX = 4.1e-9
L = 0.18e-6
W_N = 10e-6
W_P = 20e-6
MU_N = 450e-4
MU_P = 160e-4
VTH_N = 0.45
VTH_P = -0.45
VOV_N = 0.20
VOV_P = 0.22
LAMBDA_N = 0.08
ID_N = 100e-6

cox = EPS_OX / TOX
kn = MU_N * cox
kp = MU_P * cox
beta_n = kn * W_N / L
beta_p = kp * W_P / L
gm_n = 2 * ID_N / VOV_N
ro_n = 1 / (LAMBDA_N * ID_N)
cgs_n = 2 * W_N * L * cox / 3
cgd_n = 0.10 * cgs_n
print(f"Cox={cox:.3e} F/m^2 kn={kn:.3e} A/V^2 kp={kp:.3e} A/V^2")
print(f"beta_n={beta_n:.3e} beta_p={beta_p:.3e} gm_n={gm_n:.3e} ro_n={ro_n:.3e}")
print(f"cgs_n={cgs_n:.3e} cgd_n={cgd_n:.3e} Vtn={VTH_N:.2f} Vtp={VTH_P:.2f} Vov={VOV_N:.2f}")
assert 7e-3 < cox < 9e-3
assert gm_n > 0.9e-3 and ro_n > 100e3
assert cgs_n > cgd_n > 0
print("PASS mosfet_parameter_extraction")
