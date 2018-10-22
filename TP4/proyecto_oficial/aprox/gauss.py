# coding=utf-8
import aprox
import sympy as sp
from utils import algebra
from decimal import *
from scipy import signal
import config


class Gauss(aprox.Aprox):
    def __init__(self, plantilla):
        super(Gauss, self).__init__(plantilla)
        self.factor = Decimal(self.plantilla.t0)

    def calcularDadoGamma(self, n_value, k=1, norm=-1, gamma=1):
        sn, s = sp.symbols("sn s")


        #print(num)
        den = 0
        fact = 1
        cnt = -1

        for i in range(1, n_value+1):
            fact *= i
            den += (gamma**i)*((s/sp.I)**(2*i)) / fact
        #print(den)

        exp = 1 / (1+den)
        #exp = self.plantilla.denormalizarFrecuencias(exp, s, sn)
        #print(exp)

        roots = algebra.getRoots(exp, s)
        roots[1] = algebra.filterRealNegativeRoots(roots[1])

        poles = []
        for i in roots[1]:
            poles.append({"value": i})

        exp = algebra.armarPolinomino(poles, [], s, 1)
        self.tf = algebra.conseguir_tf(exp, s, [])

        return self.tf

    def calcular(self, n_value, norm):
        gamma = self.computarGamma(self.plantilla.t0, n_value)
        return self.calcularDadoGamma(n_value,1,1, gamma)

    def computarGamma(self, t0, n):
        # for k in range(5, 1000, 1):
        #     gamma = k / 100.0
        gamma_min = 0
        gamma_max = 10
        iterations = 50
        while iterations > 0:
            #print(iterations)
            #print(gamma_min, gamma_max)
            half = (gamma_max + gamma_min) / 2
            self.calcularDadoGamma(n, 1, 0, half)
            gd = self.evaluarRetardoDeGrupo(1e-3, 1e-6)
            #print("gd = " , gd)
            #print("tmin =", self.plantilla.tmin)
            if gd > self.plantilla.t0:
                gamma_max = half
            else:
                gamma_min = half

            iterations -= 1

        return gamma_max

        # print("gamma = ", gamma, "gd = ", self.evaluarRetardoDeGrupo(1e-3, 1e-6))

    def getMinNValue(self):
        return -2
        ans = 1
        found = 0
        for i in range(1, config.max_n+1):
            ans = i
            self.calcular(i, 0)

            gd = self.evaluarRetardoDeGrupo(self.plantilla.fp, self.plantilla.fp * 0.001)

        if found:
            return ans
        else:
            return -1
