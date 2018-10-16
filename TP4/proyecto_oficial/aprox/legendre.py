# coding=utf-8

from aprox import Aprox
from numpy.polynomial import legendre
from math import sqrt
import sympy as sp
from utils import algebra
from numpy import polynomial as P


def get_a(i, n):
    if n % 2 == 0:
        k = int((n-2)/2)
        if (k + i) % 2 == 0:
            return 2 * i + 1
        else:
            return 0
    else:
        return 2*i+1


class Legendre(Aprox):
    def __init__(self, plantilla):
        super(Legendre, self).__init__(plantilla)

    def calcular(self, n, k_factor = 1):
        if n % 2 == 1:
            k = int((n-1)/2)
            arr = []
            for i in range(k+1):
                arr.append(get_a(i, n))

            poly = legendre.leg2poly(legendre.legint(legendre.legmul(arr, arr)))
        else:
            k = int((n-2)/2)
            arr = []
            for i in range(k+1):
                arr.append(get_a(i, n))

            leg_b = legendre.legmul(legendre.legmul(arr, arr), legendre.poly2leg([1, 1]))

            poly = legendre.leg2poly(legendre.legint(leg_b))

        exp = 0
        wn, sn, s = sp.symbols("wn sn s")

        for i in range(len(poly)):
            exp += poly[i] * ((2*(wn**2)-1) ** i)
            exp -= poly[i] * ((-1)**i)

        if n % 2 == 1:
            exp = exp * 1 / (2 * (k+1)**2)
        else:
            exp = exp * 1 / ((k+1)*(k+2))

        exp = 1 / (1+self.getXi()**2*exp)
        exp = exp.subs(wn, sn/1j)

        roots = algebra.getRoots(exp, sn)
        roots[1] = algebra.filterRealNegativeRoots(roots[1])

        poles = []
        for i in roots[1]:
            poles.append({"value": i})

        exp = algebra.armarPolinomino(poles, [], sn, 1)
        exp = self.plantilla.denormalizarFrecuencias(exp, s, sn)

        return algebra.conseguir_tf(exp, s, [])





