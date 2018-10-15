# coding=utf-8
import aprox
from math import sin, sinh, cos, cosh, pi
from numpy import arcsinh, arccos, arccosh
import sympy as sp
from decimal import *


class ChebyInv(aprox.Aprox):
    #Al igual que con butter escribimos las tres funciones propias de la aproximación

    def __init__(self,plantilla):
        super(ChebyInv, self).__init__(plantilla)

    def getPoles(self, n_value, xi):
        poles = []

        for k in range(1, n_value+1):
            alpha_k = (2*k-1)/(2*n_value) * pi
            beta = abs(-1/n_value * arcsinh(1/xi))

            re = Decimal(sin(alpha_k) * sinh(beta))
            im = Decimal(cos(alpha_k) * cosh(beta))

            #re + im * sp.I
            poleval = 1/(re + im * sp.I)

            poles.append({"symbol": sp.symbols("p"+str(k)), "value": poleval})

        return poles
    def getZeroes(self,n_value , xi):
        zeroes = []
        for k in range(1, n_value + 1):
            alpha_k = (2 * k - 1) / (2 * n_value) * pi
            zeroval = sp.I / (cos(alpha_k))
            zeroes.append({"symbol": sp.symbols("z" + str(k)), "value": zeroval})
        return zeroes
    def getXi(self):
        return (1/(10**(self.plantilla.data["aa"]/10)-1))**(1/2)

    # def Tn(self, n, w):
    #     if w < 1:
    #         return cos(n*arccos(w))
    #     else:
    #         return cosh(n*arccosh(w))

    def getZeroGain(self, n_value):
        return 1
