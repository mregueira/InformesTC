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

    def setPlantilla(self, plantilla):
        # Configurar la plantilla actual seleccionada
        if config.debug:
            print("Seteando plantilla")
            print("data = ", plantilla.data)
        self.plantilla = plantilla
        # Debemos recomputar todas las aproximaciones
        for i in self.aproximations.keys():
            self.calcular(self.aproximations[i])

    def addPlot(self, plotData, updateProgressFunc=None):
        # Agregamos un nuevo gráfico a la lista
        self.number += 1

        self.aproximations[self.number] = {"info": plotData, "data": dict()}
        if self.plantilla:
            self.calcular(self.aproximations[self.number], updateProgressFunc)

        return self.number

    def eraseAproximation(self, code):
        # Borramos una aproximación de la lista
        if config.debug:
            print("Eliminando aproximacion ",code)
        del self.aproximations[code]
        if config.debug:
            print("Aproximaciones: ", self.aproximations)

    def calcular(self, aproximacion, updateProgressFunc = None):
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
        total = data["maxN"] - data["minN"] + 1
        for n in range(data["minN"], data["maxN"]+1):
            aproximacion["data"][str(n)] = my_aprox.calcular(n, 1)
            if updateProgressFunc: # Para mostrar la barra de cargando
                updateProgressFunc(int(float(i) / float(total) * 100))

            i += 1
        if config.debug:
            print("Se terminaron de calcular las transferencias")
