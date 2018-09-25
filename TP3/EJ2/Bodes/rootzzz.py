import sympy as sp
import numpy as np
import math


R = 12000
C = 2.2e-9
Rg = 47
Cg = 10e-9
Zg = 200e3
BWP = 3e6*2*math.pi

x  = sp.symbols("x")

result=(sp.roots((C*Cg*R*Zg)*(1/BWP)*x**3 +((Cg*Zg/BWP)+C*Rg*Cg*Zg) + x**2 + C*R*x+1,x))
