# coding=utf-8
import aprox
from math import sin, sinh, cos, cosh, pi
from numpy import arcsinh, arccos, arccosh
import sympy as sp
from decimal import *


class Cheby(aprox.Aprox):
    def __init__(self,plantilla):
        super(Cheby, self).__init__(plantilla)

    def getPoles(self, n_value, xi):
        poles = []

        for k in range(1, n_value+1):
            alpha_k = (2*k-1)/(2*n_value) * pi
            beta = -1/n_value * arcsinh(1/xi)

            re = Decimal(sin(alpha_k) * sinh(beta))
            im = Decimal(cos(alpha_k) * cosh(beta))

            poles.append({"symbol": sp.symbols("p"+str(k)), "value": re + im * sp.I})

        return poles

    def Tn(self, n, w):
        if w < 1:
            return cos(n*arccos(w))
        else:
            return cosh(n*arccosh(w))

    def getZeroGain(self, n_value):
        if n_value % 2 == 0:
            return 10**(-self.plantilla.data["ap"]/20.0)
        else:
            return 1
