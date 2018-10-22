# coding=utf-8
import aprox
import sympy as sp
from utils import algebra


class Gauss(aprox.Aprox):
    def __init__(self, plantilla):
        super(Gauss, self).__init__(plantilla)

    def calcular(self, n_value, k=1, norm = -1):
        sn, s = sp.symbols("sn s")


        #print(num)
        den = 0
        fact = 1
        for i in range(1, n_value+1):
            den += (s/sp.I)**(2*i) / fact
            fact *= i
        #print(den)

        exp = 1 / (1+den)
        exp = self.plantilla.denormalizarFrecuencias(exp, s, sn)

        roots = algebra.getRoots(exp, s)
        roots[1] = algebra.filterRealNegativeRoots(roots[1])

        poles = []
        for i in roots[1]:
            poles.append({"value": i})

        exp = algebra.armarPolinomino(poles, [], s, 1)

        return algebra.conseguir_tf(exp, s, [])
