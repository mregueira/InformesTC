# coding=utf-8

from aprox import Aprox
import sympy as sp
from utils import algebra

polyBessel = dict()


def computeBesselPoly(n, var):
    if polyBessel.has_key(n):
        return polyBessel[n]
    # No lo calculamos ya, asi que debemos calcular el bessel N

    # casos base
    if n == 1:
        return var + 1
    if n == 2:
        return var * var + 3 * var + 3

    # Caso n
    return sp.expand((2*n-1)*computeBesselPoly(n-1, var) + var * var * computeBesselPoly(n-2, var))


class Bessel(Aprox):
    def __init__(self):
        pass

    def calcular(self, n_value, k=1):
        sn, s = sp.symbols("sn s")

        num = computeBesselPoly(n_value, sn).evalf(subs={sn:0})
        den = computeBesselPoly(n_value, sn)

        exp = num / den

        return algebra.conseguir_tf(exp, s, [])
