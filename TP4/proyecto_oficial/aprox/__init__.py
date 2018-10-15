from utils.algebra import armarPolinomino, conseguir_tf
import sympy as sp
from scipy import signal
from math import pi, sqrt

# En este modulo estarán programadas todas las aproximacione


class Aprox:
    # Aproximacion padre, con todas las funciones generales de una aproximacion
    polynominal = None
    data = dict()

    def __init__(self, plantilla):
        self.plantilla = plantilla

    def calcular(self, n_value, k=1): # calcular mediante N la funcion transferencia de la aproximacion
        poles = self.getPoles(n_value, self.getXi())
        zeroes = self.getZeroes(n_value, self.getXi())
        sn, sa, s = sp.symbols("sn sa s")
        pol = armarPolinomino(poles, zeroes, sn, self.getZeroGain(n_value))
        #pol = self.plantilla.denormalizarAmplitud(pol, sa, sn, n_value, 1, 0)
        pol = self.plantilla.denormalizarFrecuencias(pol, s, sn)

        return conseguir_tf(pol, s, poles)

    def getMinNValue(self):
        pass

    def getQValues(self):
        pass

    def getPoles(self, n_value, xi):
        pass

    def getZeroes(self, n_value, xi):
        pass

    def getData(self, start_freq, end_freq):
        pass

    def getZeroGain(self, n_value):
        return 1

    def getXi(self):
        return sqrt(10**(self.plantilla.data["ap"]/10.0)-1)
