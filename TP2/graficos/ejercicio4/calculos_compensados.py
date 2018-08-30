
import sympy as sp


def get_rational_coeffs(expr,var):
    num, denom = expr.as_numer_denom()
    #print(num,denom)
    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]
def divide_by_factor(expr, factor):

    num = [sp.simplify(expr[0][i] / factor) for i in range(len(expr[0]))]
    den = [sp.simplify(expr[1][i] / factor) for i in range(len(expr[1]))]

    return [num,den]
def paralell(a,b):
    return (a*b)/(a+b)

def derivador_compensado():
    a0, r, r2 , c, s, wp, Z2, Z1, a = sp.symbols("a0 r r2 c s wp Z2 Z1 a")

    Z1 = 1 / (s * c) + r2
    Z2 = r

    a = a0 / (s / wp + 1)
    H = -Z2 / Z1 / (1 + (Z1 + Z2) / (a * Z1))

    H = sp.factor(H,s)


    coef = get_rational_coeffs(H, s)

    factor = wp + a0*wp

    coef = divide_by_factor(coef,factor)

    print(coef)

    ### impedancia de entrada
    print("Impedancia de entrada ")

    a = a0 / (s / wp + 1)
    H = - (Z1 * (1 - a) + Z2) / (a + 1)

    coef = get_rational_coeffs(H, s)

    print(coef)



def integrador_compensado():
    a0, r, r2, c, s, wp, Z2, Z1, a = sp.symbols("a0 r r2 c s wp Z2 Z1 a")

    Z1 = r
    Z2 = paralell ( 1 / (s*c) , r2)

    a = a0 /(s/wp+1)
    H = -Z2/Z1 / (1+(Z1+Z2)/(a*Z1))

    H = sp.factor(H,s)

    coef = get_rational_coeffs(H,s)
    coef = divide_by_factor(coef ,a0*r*wp + r*wp + r2*wp)
    print(coef)
    ### impedancia de entrada
    print("Impedancia de entrada ")

    a = a0 / (s / wp + 1)
    H = - (Z1 * (1 - a) + Z2) / (a + 1)

    coef = get_rational_coeffs(H, s)

    print(coef)

derivador_compensado()
#integrador_compensado()
