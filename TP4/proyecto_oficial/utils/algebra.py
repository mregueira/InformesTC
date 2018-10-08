import sympy as sp
import config


def g(w):
    print(w.evalf(subs={sp.I:1j}))
    return complex(w.evalf(subs={sp.I: 1j}))

def expand_and_get_coef(exp, var):
    if config.debug:
        print("Funcion transferencia:", sp.expand(exp))
    data = sp.Poly(sp.expand(exp), var).all_coeffs()
    #if config.debug:
    #    print("Coeficientes transferencia: ",data)
    # print(len(data))
    # for i in range(len(data)):
    #     print(i, data[i])
    data = [g(v) for v in data]

    return data