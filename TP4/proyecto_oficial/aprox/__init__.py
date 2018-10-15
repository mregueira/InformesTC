from utils.algebra import armarPolinomino, conseguir_tf
import sympy as sp
from scipy import signal
from math import pi

# En este modulo estarán programadas todas las aproximaciones


# Listado de aproximaciones disponibles
mag_aprox = [
    "Butterworth",
    "Chebycheff",
    "Chebycheff inverso",
    "Cauer",
    "Legendre"
]

pha_aprox = [
    "Bessel"
]


class Aprox:
    polynominal = None
    data = dict()

    def __init__(self, plantilla):
        self.plantilla = plantilla

    def calcular(self, n_value, k=1):
        poles = self.getPoles(n_value)
        sn, sa, s = sp.symbols("sn sa s")

        pol = armarPolinomino(poles, [], sn, k)
        pol = self.plantilla.denormalizarAmplitud(pol, sa, sn, n_value, 1, 0)
        pol = self.plantilla.denormalizarFrecuencias(pol, s, sa)

        return conseguir_tf(pol, s, poles)

    def getMinNValue(self):
        pass

    def getQValues(self):
        pass

    def getPoles(self, n_value):
        pass

    def getZeroes(self):
        pass

    def getData(self, start_freq, end_freq):
        pass
