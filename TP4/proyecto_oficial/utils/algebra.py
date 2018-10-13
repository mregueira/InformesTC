import sympy as sp
import config


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
