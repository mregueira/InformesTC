import aprox
from math import pi
from cmath import exp
import sympy as sp
from decimal import *

class Butter(aprox.Aprox):
    def __init__(self, plantilla):
        super(Butter, self).__init__(plantilla)

    def getPoles(self, n):
        poles = []
        symbols = []

        for k in range(1, n+1):
            pole = exp(1j * (2 * k + n - 1) * (pi / (2 * n)))
            re = Decimal(pole.real)
            im = Decimal(pole.imag)
            poles.append({"symbol": sp.symbols("p"+str(k)), "value": re + im * sp.I })

        return poles
