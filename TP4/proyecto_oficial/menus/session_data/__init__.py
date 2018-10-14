# coding=utf-8
import config

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

    def addPlot(self, plotData):
        self.number += 1

        self.aproximations[self.number] = plotData

        return self.number

    def setPlantilla(self, data):
        pass

    def eraseAproximation(self, code):
        pass

