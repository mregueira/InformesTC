# coding=utf-8
import config
from aprox.butter import Butter
from utils import algebra
from utils import etapas
from sympy import *
from menus import TopBar
from aprox.reference import mag_aprox, pha_aprox
from numpy import log10, logspace

# Aca guardamos la informacion importante de la sesion de uso del programa, la cual es accedida y modificada
# Por los menus

class SessionData:
    def __init__(self, parent):
        self.aproximations = dict()
        self.plantilla = None
        self.number = 0
        self.topBar = TopBar.TopBar(parent)
        self.etapas = dict() # polos o ceros componentes de la etapa
        self.index = 0
        self.rd_min_freq = None
        self.rd_max_freq = None
        self.aproximationEtapas = None  # etapas de la aproximacion seleccionada
        self.nuevaPlantilla = 0

    def setPlantilla(self, plantilla):
        # Configurar la plantilla actual seleccionada
        if config.debug:
            print("Seteando plantilla")
            print("data = ", plantilla.data)
        self.nuevaPlantilla = 1

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

    def tryToJoin(self, codes, gain):
        if len(codes) == 0:
            return None

        partes = []
        for code in codes:
            partes.append(self.aproximationEtapas.conjunto[code])

        etapa = etapas.EtapaEE(partes, self.index, gain, partes[0]["contenido"].var)

        if etapa.corrupto:
            return None
        self.etapas[self.index] = etapa
        self.index += 1

        return etapa

    def addEtapaEE(self, etapa):
        self.etapas[etapa.index] = etapa

    def ereaseEtapa(self, index):
        del self.etapas[index]

    def updateMaxMinEtapas(self, min_freq, max_freq):
        for key in self.etapas.keys():
            etapa = self.etapas[key]

            etapa.computarMinMaxGain(min_freq, max_freq)
        self.rd_min_freq = min_freq
        self.rd_max_freq = max_freq

    def computeRD(self, v_ruido, v_sat):
        if len(self.etapas.keys()) == 0:
            return None

        v_max = 1e8
        v_min = v_ruido

        for u in self.etapas.keys():
            k = u

        for fi in range(len(self.etapas[k].mag)):
            # para cada frecuencia limitar v max y v min
            product = 1

            for etapa_k in self.etapas.keys():
                etapa = self.etapas[etapa_k]
                product *= 10**(etapa.mag[fi]/20.0) * 10**(etapa.gain/20.0)

                v_max = min(v_max, v_sat / product)
                v_min = max(v_min, v_ruido / product)

        return v_max, v_min , v_max / v_min

    def flagNuevaPlantilla(self):
        if self.nuevaPlantilla:
            self.nuevaPlantilla = 0
            return 1
        return 0