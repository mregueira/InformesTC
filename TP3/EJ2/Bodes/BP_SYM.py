
from scipy import signal
import sympy as sp
from pylab import *
def get_rational_coeffs(expr,var):
    expr = sp.expand(expr)
    print(expr)
    num, denom = expr.as_numer_denom()

    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]


Cg, Rg, R, C, BWP, Zg, s  = sp.symbols("Cg Rg R C BWP Zg s")

h=(Cg*Rg*Zg*s**2 + (Rg + BWP*Cg*Rg*Zg)*s + BWP*Rg)/(C*Cg*R*Rg*Zg*s**3 + (C*R*Rg + Cg*R*Rg + Cg*R*Zg + Cg*Rg*Zg + BWP*C*Cg*R*Rg*Zg)*s**2 + (R + Rg + BWP*C*R*Rg + BWP*Cg*R*Rg + BWP*Cg*Rg*Zg)*s + BWP*R + BWP*Rg)

[numh, denh]= get_rational_coeffs(h, s)

print("Lo que hay que ponerle a LTI\n")
print(numh)
print(",")
print(denh)

