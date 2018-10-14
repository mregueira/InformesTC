import sympy as sp
import config
from scipy import signal

### Funciones auxiliares para asistencia algebraica

def g(w):
    #print(w.evalf(subs={sp.I: 1j}))
    return complex(w.evalf(subs={sp.I: 1j}))


def get_rational_coeffs(expr, var):
    num, denom = expr.as_numer_denom()
    #print(num,denom)
    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]


def expand_and_get_coef(exp, var):

    data = get_rational_coeffs(exp, var)

    data[0] = [g(v) for v in data[0]]
    data[1] = [g(v) for v in data[1]]

    return data


# Armamos un polinomio simbolico a partir de los polos y ceros

def armarPolinomino(polos, ceros, var, k=1):
    h = k
    for c in ceros:
        h = h * (var - c) / (-c)
    for p in polos:
        h = h * 1 / (var - p) / (-p)

    return h

# Obtenemos la funcion trasnferencia de scipy a partir de un polinomio en var

def conseguir_tf(exp, var):
    value = expand_and_get_coef(exp, var)
    tf = signal.lti(value[0], value[1])

    return tf

