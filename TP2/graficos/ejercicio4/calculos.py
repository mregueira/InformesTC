import sympy as sp

def get_rational_coeffs(expr,var):
    num, denom = expr.as_numer_denom()
    #print(num,denom)
    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]

def divide_by_factor(expr, factor):

    num = [sp.simplify(expr[0][i] / factor) for i in range(len(expr[0]))]
    den = [sp.simplify(expr[1][i] / factor) for i in range(len(expr[1]))]

    return [num,den]
def calculos_derivador():
    #### Caso derivador no ideal - Avol finito

    a0, r, c, s, wp, Z2, Z1, a = sp.symbols("a0 r c s wp Z2 Z1 a")
    #
    Z1 = 1 / (s * c)
    Z2 = r

    H = -Z2 / Z1 / (1 + (Z1 + Z2) / (a0 * Z1))

    coef = get_rational_coeffs(H, s)

    num = []
    den = []

    for i in range(len(coef[0])):
        num.append(sp.simplify(coef[0][i] / (r * c ** 2)))
    for i in range(len(coef[1])):
        den.append(sp.simplify(coef[1][i] / (r * c ** 2)))

    print("Avol finito independiente de w, numerador/denominador")

    print(num)
    print(den)

    print("Avol finito dependiente de w, numerador/denominador")

    a = a0 / (s / wp + 1)
    H = -Z2 / Z1 / (1 + (Z1 + Z2) / (a * Z1))

    coef = get_rational_coeffs(H, s)

    factor = wp * (a0 + 1) / (r * c)
    num = [sp.simplify(coef[0][i] / (r * c ** 2) / factor) for i in range(len(coef[0]))]
    den = [sp.simplify(coef[1][i] / (r * c ** 2) / factor) for i in range(len(coef[1]))]

    print(num)
    print(den)

def calculos_integrador():
    a0, r, c, s, wp, Z2, Z1, a = sp.symbols("a0 r c s wp Z2 Z1 a")

    Z1 = r
    Z2 = 1 / (s*c)
    ### Caso ideal
    print("Caso Ideal")

    H = (-Z2/Z1)

    print(sp.simplify(H))

    ### Caso Avol finito

    H = -Z2 / Z1 / (1 + (Z1 + Z2) / (a0 * Z1))
    coef = get_rational_coeffs(H, s)

    print("Avol finito independiente de w, numerador/denominador")

    factor = c*r
    num = [sp.simplify(coef[0][i] / factor) for i in range(len(coef[0]))]
    den = [sp.simplify(coef[1][i] / factor) for i in range(len(coef[1]))]

    print(num)
    print(den)

    ### Caso avol infinito
    print("Avol infinito independiente de w, numerador/denominador")

    a = a0 / (1+s/wp)
    H = -Z2 / Z1 / (1 + (Z1 + Z2) / (a * Z1))

    coef = get_rational_coeffs(H,s)
    print(coef)
    factor = c*r*wp
    coef = divide_by_factor(coef,factor)

    print(coef)
calculos_derivador()
calculos_integrador()