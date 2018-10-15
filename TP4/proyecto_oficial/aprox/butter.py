import aprox
from math import pi
from cmath import exp
import sympy as sp
from decimal import *


class Butter(aprox.Aprox):
    def __init__(self, plantilla):
        super(Butter, self).__init__(plantilla)

    def getPoles(self, n, xi):
        poles = []
        symbols = []

        mod = 1 / (xi ** (1 / float(n)))
        print("mod = ", mod)
        for k in range(1, n+1):

            pole = mod * exp(1j * (2 * k + n - 1) * (pi / (2 * n)))
            re = Decimal(pole.real)
            im = Decimal(pole.imag)
            poles.append({"symbol": sp.symbols("p"+str(k)), "value": re + im * sp.I})

        return poles

    def Tn(self, n, w):
        return w ** (2*n)

    def getZeroGain(self, n_value):
        return 1
