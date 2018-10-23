# coding=utf-8
import config
from aprox.butter import Butter
from utils import algebra
from sympy import *
from menus import TopBar
from aprox.reference import mag_aprox, pha_aprox

# Aca guardamos la informacion importante de la sesion de uso del programa, la cual es accedida y modificada
# Por los menus

class SessionData:
    def __init__(self, parent):
        self.aproximations = dict()
        self.plantilla = None
        self.number = 0
        self.topBar = TopBar.TopBar(parent)
        self.etapas = dict()
        self.index = 0

        self.aproximationEtapas = None  # etapas de la aproximacion seleccionada

    def setPlantilla(self, plantilla):
        # Configurar la plantilla actual seleccionada
        if config.debug:
            print("Seteando plantilla")
            print("data = ", plantilla.data)
        self.plantilla = plantilla
        # Debemos recomputar todas las aproximaciones
        for i in self.aproximations.keys():
            self.calcular(self.aproximations[i])

    def addPlot(self, plotData):
        # Agregamos un nuevo gráfico a la lista
        self.number += 1
        plotData["number"] = self.number
        self.aproximations[self.number] = {"info": plotData, "data": dict(), "number": self.number}
        if self.plantilla:
            self.calcular(self.aproximations[self.number])

        return self.number, self.aproximations[self.number]["data"]["instance"].getQValues()

    def eraseAproximation(self, code):
        # Borramos una aproximación de la lista
        if config.debug:
            print("Eliminando aproximacion ",code)
        del self.aproximations[code]
        if config.debug:
            print("Aproximaciones: ", self.aproximations)

    def calcular(self, aproximacion):
        # Calculamos una aproximacion, esta función puede llegar a tardar
        # Por eso suele ser ejecutada sobre un thread

        # Nomenclatura
        # aproximacion["info"] tiene
        #  - 'minN', 'maxN', 'maxQ'
        # aproximacion["data"][str(n)} debe ser escrita con la transferencia correspondiente

        data = aproximacion["info"]

        if config.debug:
            print("Caculando aproximacion, ", data)

        if self.plantilla.type == "magnitud":
            my_aprox = mag_aprox[data["aprox"]](self.plantilla)
        elif self.plantilla.type == "fase":
            my_aprox = pha_aprox[data["aprox"]](self.plantilla)

        i = 0
        n = aproximacion["info"]["minN"]
        aproximacion["data"] = dict()
        if self.plantilla.type == "fase":
            norm = -1
        else:
            norm = aproximacion["info"]["norm"]
        aproximacion["data"]["tf"] = my_aprox.calcular(n, norm)
        aproximacion["data"]["instance"] = my_aprox
        aproximacion["data"]["number"] = n

        i += 1
        if config.debug:
            print("Se terminaron de calcular las transferencias")

    def selectParaEtapas(self, code):
        if config.debug:
            print("Selected: ",code)

        self.aproximationEtapas = self.aproximations[code]["data"]["instance"].updateEtapas()
        self.flagUpdateSing = 1

    def getUpdateSing(self):
        if self.flagUpdateSing:
            self.flagUpdateSing = 0
            return 1
        return 0

    def tryToJoin(self, codes):
        partes = []
        for code in codes:
            partes.append(self.aproximationEtapas.conjunto[code])

        etapa = algebra.EtapaEE(partes, self.index)

        if etapa.corrupto:
            return None
        self.etapas[self.index] = etapa
        self.index += 1

        return etapa


