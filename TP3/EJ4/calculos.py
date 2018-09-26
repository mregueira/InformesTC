import sympy as sp


def get_rational_coeffs(expr,var):
    expr = sp.expand(expr)
    #print(expr)
    num, denom = expr.as_numer_denom()

    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]


k, s = sp.symbols("k s")

nano = 10.0**(-9)
K = 10.0**3


def get_transfer(R1, R2, R3, C1, C2):
    a1 = C1 * C2 * R1 * R2 * (R1 + 2 * R2 * k - 2 * R2 * (k ** 2) + R3)
    a2 = (C2 * (((R1) ** 2) + ((R2) ** 2) * k - ((R2) ** 2) * (k ** 2) + R1 * R2 + R1 * R3 + R2 * R3 - R2 * R3 * k)) + (
                2 * C1 * R1 * R2)
    a3 = 2 * R1 + R2
    b1 = C1 * C2 * R1 * R2 * (R1 + 2 * R2 * k - 2 * R2 * (k ** 2) + R3);
    b2 = (C2 * (((R1) ** 2) + ((R2) ** 2) * k - ((R2) ** 2) * (k ** 2) + R1 * R2 + R1 * R3 + R2 * R3 * k)) + (
                2 * C1 * R1 * R2)
    b3 = 2 * R1 + R2

    return -((a1)*(s**2) + (a2)*s + a3)/((b1)*(s**2) + (b2)*s + b3)


t1 = get_transfer(
    R1=560,
    R2=10000,
    R3=100000,
    C1=1000*nano,
    C2=100*nano
)

t2 = get_transfer(
    R1=560,
    R2=10*K,
    R3=100*K,
    C1=100*nano,
    C2=10*nano
)

t3 = get_transfer(
    R1=560,
    R2=10*K,
    R3=100*K,
    C1=10*nano,
    C2=1*nano
)


h = get_rational_coeffs( -5/9*(t1+t2+t3), s)


print(h)