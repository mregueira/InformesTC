
from scipy import signal
import sympy as sp
from pylab import *
def get_rational_coeffs(expr,var):
    expr = sp.expand(expr)
    print(expr)
    num, denom = expr.as_numer_denom()

    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]


Cg, Rg, R, C, BWP, Zg, s  = sp.symbols("Cg Rg R C BWP Zg s")

Vmenos,Vmas,Vhashtag,Vin,Vout  = sp.symbols("Vmenos Vmas Vhashtag Vin Vout")


h = sp.solve([
    Vmenos-Vmas*(1/(1+(s/BWP))),
    Vin-Zg*(Vmas-Vhashtag)*s*Cg - Vmas,
    -Vout+(Vmas-Vhashtag)*Cg+(Vmenos  -Vhashtag)/(s*C*Rg),
    -Vout+ Vhashtag*(1/(s*C*R+1)) ],
    (Vmas, Vmenos, Vhashtag, Vout, Vin)
)

print(h[Vout]/Vin)

h=(BWP*C*Cg*Rg*s + BWP + C*Cg*Rg*s**2)/(C*Rg*s*(BWP*Cg*Zg*s + BWP + Cg*Zg*s**2 + s) + (C*R*s + 1)*(BWP*C*Cg*Rg*s + BWP + C*Cg*Rg*s**2 + Cg*Zg*s**2 + s))

[numh, denh]= get_rational_coeffs(h, s)

print("Lo que hay que ponerle a LTI\n")
print(numh)
print(",")
print(denh)

