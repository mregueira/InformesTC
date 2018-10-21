from utils.algebra import armarPolinomino, conseguir_tf, expand_and_get_coef
from utils import compare
import sympy as sp
from scipy import signal
from math import pi, sqrt
import config


EPS = 1e-15

# En este modulo estarán programadas todas las aproximacione

class Etapa:
    def __init__(self, w0, xi, order):
        self.w0 = w0
        self.q = 1 / 2 * xi
        self.xi = xi
        self.order = order

    def show(self):
        print("Etapa de orden 2:")
        print("w0 = ", self.w0, " q = ", self.q)


class Aprox:
    # Aproximacion padre, con todas las funciones generales de una aproximacion
    polynominal = None
    data = dict()
    tf = None

    def __init__(self, plantilla):
        self.plantilla = plantilla

    def calcular(self, n_value, k=1): # calcular mediante N la funcion transferencia de la aproximacion
        poles = self.getPoles(n_value, self.getXi())
        zeroes = self.getZeroes(n_value, self.getXi())
        sn, sa, s = sp.symbols("sn sa s")
        pol = armarPolinomino(poles, zeroes, sn, self.getZeroGain(n_value))
        #pol = self.plantilla.denormalizarAmplitud(pol, sa, sn, n_value, 1, 0)
        pol = self.plantilla.denormalizarFrecuencias(pol, s, sn)

        self.tf = conseguir_tf(pol, s, poles)
        self.updateEtapas()
        return self.tf

    def getMinNValue(self):
        return -1

    def getQValues(self):
        return -1

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

    def updateEtapas(self):
        if config.debug:
            print("Actualizando etapas")

        poles = self.tf.poles

        # tengo que armar los pares de polos complejos conjugados

        poles = sorted(poles, key=lambda x: x.real)

        s = sp.symbols("s")
        if config.debug:
            print(poles)
        sing = []
        for i in range(len(poles)):
            if i != len(poles)-1 and compare(poles[i].imag, -poles[i+1].imag):
                # por cada singularidad de segundo orden
                mySing = {
                    "order": 2,
                    "exp": (s - poles[i])*(s - poles[i+1]) / (-poles[i]) / (-poles[i+1])
                }
                sing.append(mySing)
            else:
                if i == 0 or not compare(poles[i].imag, -poles[i-1].imag):
                    #por cada singularidad de primer orden
                    mySing = {
                        "order": 1,
                        "exp": (s - poles[i]) / (-poles[i])
                    }
                    sing.append(mySing)
        #if config.debug:
        #    print("Etapas encontradas: ")
        #    for s in sing:
        #        print(s)
        etapas = []

        for si in sing:
            if si["order"] == 2:
                si["exp"] = si["exp"].subs({sp.I: 1j})
                print(si["exp"])
                exp = expand_and_get_coef(si["exp"], s)

                w0 = sqrt(1/exp[0][0])
                xi = exp[0][1]*w0/2

                etapas.append(Etapa(w0, xi, 2))

        if config.debug:
            for etapa in etapas:
                etapa.show()
