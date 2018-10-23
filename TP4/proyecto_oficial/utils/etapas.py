from utils.algebra import conseguir_tf, conseguir_coef, compare
from numpy import pi, sqrt
import sympy as sp

# Aqui esta el codigo que administra las etapas formadas por polos y ceros


class Etapa:
    index = None

    def __init__(self, w0, xi, order):
        self.f0 = w0 / 2 / pi
        if -1e-5 < xi < 1e-5:
            self.q = 1e5
        else:
            self.q = 1 / (2 * xi)
        self.xi = xi
        self.order = order

        self.k = 1

        # Si order=1, q no tiene sentido
        # Si f0 = -1, la singularidad esta en el origen
        # Si Q > 100, se considera una singularidad en el eje jw

    def getType(self):
        if self.f0 < 0:
            tipo = "origen"
        elif self.q > 100 or self.q < -100:
            tipo = "conjugados, eje jw"
        elif self.order == 2:
            tipo = "conjugados"
        else:
            tipo = "real"
        return tipo

    def setIndex(self, index):
        self.index = index

    def show(self):
        print("Etapa de orden 2:")
        print("w0 = ", self.w0, " q = ", self.q)


class EtapaEE:  # etapa compuesta por un polo de orden dos o uno mas uno cero de orden 1 o 2
    def __init__(self, partes, index, gain=1):
        self.polos = []
        self.ceros = []
        self.index = index
        self.gain = gain

        orderPolos = 0
        orderCeros = 0

        for comp in partes:
            if comp["tipo"] == "polo":
                self.polos.append(comp["contenido"])
                orderPolos += comp["contenido"].order
            else:
                self.ceros.append(comp["contenido"])
                orderCeros += comp["contenido"].order

        self.corrupto = 0
        if orderPolos >= 3 or orderPolos == 0:
            self.corrupto = 1
            return
        if orderCeros >= 3:
            self.corrupto = 1
            return

        if len(self.polos) == 2:
            t1 = self.polos[0].getType()
            t2 = self.polos[1].getType()
            if t1 == "origen" and t2 == "origen":
                self.polos = [Etapa(-1, -1, 2)]
        if len(self.ceros) == 2:
            t1 = self.ceros[0].getType()
            t2 = self.ceros[1].getType()
            if t1 == "origen" and t2 == "origen":
                self.ceros = [Etapa(-1, -1, 2)]

        self.polo = self.polos[0]
        if len(self.ceros) > 0:
            self.cero = self.ceros[0]
        else:
            self.cero = None

    def getTransfer(self):
        pass


# obtener singularidades de primer y segundo orden a partir de polos o ceros
def getSing(data):
    print("data = ", data)
    s = sp.symbols("s")

    entidades = []
    etapas = []
    # tengo que armar los pares de polos complejos conjugados
    for i in range(len(data)):
        if compare(data[i].real, 0) and compare(data[i].imag, 0):
            etapas.append(Etapa(-1, -1, 1))
        elif data[i].imag < 0:
            entidades.append(data[i].real - data[i].imag * 1j)
        else:
            entidades.append(data[i].real + data[i].imag * 1j)
    entidades = sorted(entidades, key=lambda x: x.imag)

    # print("entidades = " , entidades)

    sing = []
    skip = 0

    for i in range(len(entidades)):
        if skip:
            skip = 0
            continue
        if i != len(entidades) - 1 and compare(entidades[i].imag, entidades[i + 1].imag):
            # por cada singularidad de segundo orden
            cong = entidades[i].real - entidades[i].imag * 1j
            mySing = {
                "order": 2,
                "exp": (s - entidades[i]) * (s - cong) / (-entidades[i]) / (-cong)
            }
            sing.append(mySing)

            skip = 1
        else:
            mySing = {
                "order": 1,
                "exp": (s - entidades[i]) / (-entidades[i])
            }
            sing.append(mySing)
    # print("sing = ",sing)

    for si in sing:
        if si["order"] == 2:
            exp = conseguir_coef(si["exp"], s)
            # print("exp = ",exp)

            w0 = sqrt(1 / exp[0][0].real)
            xi = exp[0][1].real * w0 / 2

            etapas.append(Etapa(w0, xi, 2))

        elif si["order"] == 1:
            exp = conseguir_coef(si["exp"], s)

            w0 = 1 / exp[0][0].real

            etapas.append(Etapa(w0, -1, 1))

    return etapas


