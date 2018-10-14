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

    def calcular(self, freq, n_value, k=1):
        poles = self.getPoles(n_value)
        sn, sa, s = sp.symbols("sn sa s")

        pol = armarPolinomino(poles, [], sn, k)
        pol = self.plantilla.denormalizarAmplitude(n_value, pol, sa, sn, 1)
        pol = self.plantilla.denormalizarFrecuencias(pol, s, sa)

        tf = conseguir_tf(pol, s)

        w_range = [i * 2 * pi for i in freq]
        w, mag, pha = signal.bode(tf, w_range)

        f = [i / 2 / pi for i in w]

        return f, mag, pha

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
