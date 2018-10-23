import sympy as sp
import config
from scipy import signal
from decimal import *
from numpy import roots, nditer, log10, floor, pi, sqrt
from utils import compare


def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)


### Funciones auxiliares para asistencia algebraica

def g(w):
    #print(w.evalf(subs={sp.I: 1j}))
    return w.evalf(subs={sp.I: 1j})


def get_rational_coeffs(expr, var):
    num, denom = expr.as_numer_denom()
    #print(num,denom)
    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]

def expand_and_get_coef(exp, var):

    data = get_rational_coeffs(exp, var)

    #data[0] = [g(v) for v in data[0]]
    #data[1] = [g(v) for v in data[1]]

    return data


def getRoots(exp, var):
    data = get_rational_coeffs(exp, var)

    data[0] = roots(data[0])
    data[1] = roots(data[1])

    return data


def filterRealNegativeRoots(rootList):
    ans = []
    for i in nditer(rootList):
        if i.real < 0:
            ans.append(i)
    return ans


# Armamos un polinomio simbolico a partir de los polos y ceros
def armarPolinomino(polos, ceros, var, k=1):
    h = k
    for c in ceros:
        h = h * (var - c["value"]) / -c["value"]
    for p in polos:
        h = h * 1 / (var - p["value"]) * -p["value"]

    return h

# Obtenemos la funcion trasnferencia de scipy a partir de un polinomio en var

def conseguir_coef(exp, var):
    value = expand_and_get_coef(exp, var)

    my_subs = dict()
    my_subs[sp.I] = 1j

    for i in range(len(value[0])):
        value[0][i] = complex(value[0][i].evalf(subs=my_subs))
    for i in range(len(value[1])):
        value[1][i] = complex(value[1][i].evalf(subs=my_subs))

    return value

def conseguir_tf(exp, var, poles = []):

    value = expand_and_get_coef(exp, var)

    my_subs = dict()
    my_subs[sp.I] = 1j

    for i in range(len(value[0])):
        value[0][i] = complex(value[0][i].evalf(subs=my_subs))
    for i in range(len(value[1])):
        value[1][i] = complex(value[1][i].evalf(subs=my_subs))
    #print(value[0], value[1])

    tf = signal.lti(value[0], value[1])

    return tf


class Etapa:
    def __init__(self, w0, xi, order):
        self.f0 = w0 / 2 / pi
        self.q = 1 / (2 * xi)
        self.xi = xi
        self.order = order

        self.k = 1

        # Si order=1, q no tiene sentido
        # Si f0 = -1, la singularidad esta en el origen
        # Si Q > 100, se considera una singularidad en el eje jw

    def getType(self):
        if self.f0 == -1:
            tipo = "origen"
        elif self.q > 100:
            tipo = "conjugados, eje jw"
        elif self.order == 2:
            tipo = "conjugados"
        else:
            tipo = "real"
        return tipo

    def show(self):
        print("Etapa de orden 2:")
        print("w0 = ", self.w0, " q = ", self.q)


# obtener singularidades de primer y segundo orden a partir de polos o ceros

def getSing(data):
    print("data = ",data)
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

    #print("entidades = " , entidades)

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
    #print("sing = ",sing)

    for si in sing:
        if si["order"] == 2:
            exp = conseguir_coef(si["exp"], s)
            #print("exp = ",exp)

            w0 = sqrt(1 / exp[0][0].real)
            xi = exp[0][1].real * w0 / 2

            etapas.append(Etapa(w0, xi, 2))

        elif si["order"] == 1:
            exp = conseguir_coef(si["exp"], s)

            w0 = 1 / exp[0][0].real

            etapas.append(Etapa(w0, -1, 1))

    return etapas


