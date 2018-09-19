
from scipy import signal
import sympy as sp
from pylab import *
def get_rational_coeffs(expr,var):
    expr = sp.expand(expr)
    print(expr)
    num, denom = expr.as_numer_denom()

    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]


Cg, Rg, R, C, BWP, Zg, s  = sp.symbols("Cg Rg R C BWP Zg s")

h=(BWP + s + C*Rg*s**2 + Cg*Rg*s**2 + Cg*Zg*s**2 + BWP*C*Rg*s + BWP*Cg*Rg*s + C*Cg*Rg*Zg*s**3 + BWP*C*Cg*Rg*Zg*s**2)/(C*Cg*(R*Rg + R*Zg + Rg*Zg)*s**3 + (C*R + C*Rg + Cg*Rg + Cg*Zg + BWP*C*Cg*R*Rg + BWP*C*Cg*Rg*Zg)*s**2 + (BWP*C*R + BWP*C*Rg + BWP*Cg*Rg + 1)*s + BWP)

[numh, denh]= get_rational_coeffs(h, s)

print("Lo que hay que ponerle a LTI\n")
print(numh)
print(",")
print(denh)

