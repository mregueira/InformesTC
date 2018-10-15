from utils import algebra
import sympy as sp
from decimal import *
from aprox.butter import Butter

polos = []
ceros = []

for i in range(20):
    polos.append({"symbol": Decimal(1.23432), "value": 1})


s = sp.symbols("s")

pol = algebra.armarPolinomino(polos, ceros, s, 1)
value = algebra.expand_and_get_coef(pol, s)

print(value)