# coding=utf-8
import config
from aprox.butter import Butter
from utils import algebra
from sympy import *

# Aca guardamos la informacion importante de la sesion de uso del programa

class SessionData:
    def __init__(self):
        self.aproximations = dict()
        self.plantilla = None
        self.number = 0

    def setPlantilla(self, plantilla):
        if config.debug:
            print("Seteando plantilla")
            print("data = ", plantilla.data)
        self.plantilla = plantilla
        ### Debemos recomputar todas las aproximaciones
        for i in self.aproximations:
            self.calcular(i)

    def addPlot(self, plotData):
        self.number += 1

        self.aproximations[self.number] = {"info": plotData, "data": dict()}
        if self.plantilla:
            self.calcular(self.aproximations[self.number])

        return self.number

    def eraseAproximation(self, code):
        if config.debug:
            print("Eliminando aproximacion ",code)
        del self.aproximations[code]
        if config.debug:
            print("Aproximaciones: ", self.aproximations)

    def calcular(self, aproximacion):
        data = aproximacion["info"]

        if config.debug:
            print("Caculando aproximacion, ", data)

        butter = Butter(self.plantilla)

        for n in range(data["minN"], data["maxN"]+1):
            sn, s, sa = symbols("sn s sa")

            poles = butter.getPoles(n)
            exp = algebra.armarPolinomino(poles, [], s, 1)
            exp = self.plantilla.denormalizarAmplitud(exp, sa, sn, n, 1, 0)
            exp = self.plantilla.denormalizarFrecuencias(exp, s, sa)

            tf = algebra.conseguir_tf(exp, s)

            aproximacion["data"][str(n)] = tf

        if config.debug:
            print("Se terminaron de calcular las transferencias")
