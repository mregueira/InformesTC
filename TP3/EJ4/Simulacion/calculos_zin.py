
import sympy as sp

s, k = sp.symbols("s k")

nano = 10.0**(-9)
K = 10.0**3

def get_rational_coeffs(expr,var):
    expr = sp.expand(expr)
    #print(expr)
    num, denom = expr.as_numer_denom()

    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]


def get_transfer_zin(R1, R2, R3, C1L, C1M, C1H, C2L, C2M, C2H):
    return 1 / ((
                     2 * R1 + R2 + C2H * R1 ** 2 * s + C2H * R2 ** 2 * k * s - C2H * R2 ** 2 * k ** 2 * s + 2 * C1H * R1 * R2 * s + C2H * R1 * R2 * s + C2H * R1 * R3 * s + C2H * R2 * R3 * s - C2H * R2 * R3 * k * s + C1H * C2H * R1 ** 2 * R2 * s ** 2 + 2 * C1H * C2H * R1 * R2 ** 2 * k * s ** 2 - 2 * C1H * C2H * R1 * R2 ** 2 * k ** 2 * s ** 2 + C1H * C2H * R1 * R2 * R3 * s ** 2) / (
                     R3 * (
                         2 * R1 + R2 + C2H * R1 ** 2 * s + C2H * R2 ** 2 * k * s - C2H * R2 ** 2 * k ** 2 * s + 2 * C1H * R1 * R2 * s + C2H * R1 * R2 * s + C1H * C2H * R1 ** 2 * R2 * s ** 2 + 2 * C1H * C2H * R1 * R2 ** 2 * k * s ** 2 - 2 * C1H * C2H * R1 * R2 ** 2 * k ** 2 * s ** 2)) + (
                     2 * R1 + R2 + C2L * R1 ** 2 * s + C2L * R2 ** 2 * k * s - C2L * R2 ** 2 * k ** 2 * s + 2 * C1L * R1 * R2 * s + C2L * R1 * R2 * s + C2L * R1 * R3 * s + C2L * R2 * R3 * s - C2L * R2 * R3 * k * s + C1L * C2L * R1 ** 2 * R2 * s ** 2 + 2 * C1L * C2L * R1 * R2 ** 2 * k * s ** 2 - 2 * C1L * C2L * R1 * R2 ** 2 * k ** 2 * s ** 2 + C1L * C2L * R1 * R2 * R3 * s ** 2) / (
                     R3 * (
                         2 * R1 + R2 + C2L * R1 ** 2 * s + C2L * R2 ** 2 * k * s - C2L * R2 ** 2 * k ** 2 * s + 2 * C1L * R1 * R2 * s + C2L * R1 * R2 * s + C1L * C2L * R1 ** 2 * R2 * s ** 2 + 2 * C1L * C2L * R1 * R2 ** 2 * k * s ** 2 - 2 * C1L * C2L * R1 * R2 ** 2 * k ** 2 * s ** 2)) + (
                     2 * R1 + R2 + C2M * R1 ** 2 * s + C2M * R2 ** 2 * k * s - C2M * R2 ** 2 * k ** 2 * s + 2 * C1M * R1 * R2 * s + C2M * R1 * R2 * s + C2M * R1 * R3 * s + C2M * R2 * R3 * s - C2M * R2 * R3 * k * s + C1M * C2M * R1 ** 2 * R2 * s ** 2 + 2 * C1M * C2M * R1 * R2 ** 2 * k * s ** 2 - 2 * C1M * C2M * R1 * R2 ** 2 * k ** 2 * s ** 2 + C1M * C2M * R1 * R2 * R3 * s ** 2) / (
                     R3 * (
                         2 * R1 + R2 + C2M * R1 ** 2 * s + C2M * R2 ** 2 * k * s - C2M * R2 ** 2 * k ** 2 * s + 2 * C1M * R1 * R2 * s + C2M * R1 * R2 * s + C1M * C2M * R1 ** 2 * R2 * s ** 2 + 2 * C1M * C2M * R1 * R2 ** 2 * k * s ** 2 - 2 * C1M * C2M * R1 * R2 ** 2 * k ** 2 * s ** 2)) + (
                     (C1H * C2H * R2 ** 2 * k * s ** 2 - C1H * C2H * R2 ** 2 * k ** 2 * s ** 2 + C1H * R2 * s + 1) * (
                         4 * R1 + 2 * R2 + 2 * C2H * R1 ** 2 * s + 2 * C2H * R2 ** 2 * k * s - 2 * C2H * R2 ** 2 * k ** 2 * s + 4 * C1H * R1 * R2 * s + 2 * C2H * R1 * R2 * s + 2 * C2H * R1 * R3 * s + C2H * R2 * R3 * s + 2 * C1H * C2H * R1 ** 2 * R2 * s ** 2 + 4 * C1H * C2H * R1 * R2 ** 2 * k * s ** 2 - 4 * C1H * C2H * R1 * R2 ** 2 * k ** 2 * s ** 2 + 2 * C1H * C2H * R1 * R2 * R3 * s ** 2)) / (
                     (
                                 2 * R1 + R2 + C2H * R1 ** 2 * s + C2H * R2 ** 2 * k * s - C2H * R2 ** 2 * k ** 2 * s + 2 * C1H * R1 * R2 * s + C2H * R1 * R2 * s + C1H * C2H * R1 ** 2 * R2 * s ** 2 + 2 * C1H * C2H * R1 * R2 ** 2 * k * s ** 2 - 2 * C1H * C2H * R1 * R2 ** 2 * k ** 2 * s ** 2) * (
                                 2 * R1 + R2 + C2H * R1 ** 2 * s + C2H * R2 ** 2 * k * s - C2H * R2 ** 2 * k ** 2 * s + 2 * C1H * R1 * R2 * s + C2H * R1 * R2 * s + C2H * R1 * R3 * s + C2H * R2 * R3 * k * s + C1H * C2H * R1 ** 2 * R2 * s ** 2 + 2 * C1H * C2H * R1 * R2 ** 2 * k * s ** 2 - 2 * C1H * C2H * R1 * R2 ** 2 * k ** 2 * s ** 2 + C1H * C2H * R1 * R2 * R3 * s ** 2)) + (
                     (C1L * C2L * R2 ** 2 * k * s ** 2 - C1L * C2L * R2 ** 2 * k ** 2 * s ** 2 + C1L * R2 * s + 1) * (
                         4 * R1 + 2 * R2 + 2 * C2L * R1 ** 2 * s + 2 * C2L * R2 ** 2 * k * s - 2 * C2L * R2 ** 2 * k ** 2 * s + 4 * C1L * R1 * R2 * s + 2 * C2L * R1 * R2 * s + 2 * C2L * R1 * R3 * s + C2L * R2 * R3 * s + 2 * C1L * C2L * R1 ** 2 * R2 * s ** 2 + 4 * C1L * C2L * R1 * R2 ** 2 * k * s ** 2 - 4 * C1L * C2L * R1 * R2 ** 2 * k ** 2 * s ** 2 + 2 * C1L * C2L * R1 * R2 * R3 * s ** 2)) / (
                     (
                                 2 * R1 + R2 + C2L * R1 ** 2 * s + C2L * R2 ** 2 * k * s - C2L * R2 ** 2 * k ** 2 * s + 2 * C1L * R1 * R2 * s + C2L * R1 * R2 * s + C1L * C2L * R1 ** 2 * R2 * s ** 2 + 2 * C1L * C2L * R1 * R2 ** 2 * k * s ** 2 - 2 * C1L * C2L * R1 * R2 ** 2 * k ** 2 * s ** 2) * (
                                 2 * R1 + R2 + C2L * R1 ** 2 * s + C2L * R2 ** 2 * k * s - C2L * R2 ** 2 * k ** 2 * s + 2 * C1L * R1 * R2 * s + C2L * R1 * R2 * s + C2L * R1 * R3 * s + C2L * R2 * R3 * k * s + C1L * C2L * R1 ** 2 * R2 * s ** 2 + 2 * C1L * C2L * R1 * R2 ** 2 * k * s ** 2 - 2 * C1L * C2L * R1 * R2 ** 2 * k ** 2 * s ** 2 + C1L * C2L * R1 * R2 * R3 * s ** 2)) + (
                     (C1M * C2M * R2 ** 2 * k * s ** 2 - C1M * C2M * R2 ** 2 * k ** 2 * s ** 2 + C1M * R2 * s + 1) * (
                         4 * R1 + 2 * R2 + 2 * C2M * R1 ** 2 * s + 2 * C2M * R2 ** 2 * k * s - 2 * C2M * R2 ** 2 * k ** 2 * s + 4 * C1M * R1 * R2 * s + 2 * C2M * R1 * R2 * s + 2 * C2M * R1 * R3 * s + C2M * R2 * R3 * s + 2 * C1M * C2M * R1 ** 2 * R2 * s ** 2 + 4 * C1M * C2M * R1 * R2 ** 2 * k * s ** 2 - 4 * C1M * C2M * R1 * R2 ** 2 * k ** 2 * s ** 2 + 2 * C1M * C2M * R1 * R2 * R3 * s ** 2)) / (
                     (
                                 2 * R1 + R2 + C2M * R1 ** 2 * s + C2M * R2 ** 2 * k * s - C2M * R2 ** 2 * k ** 2 * s + 2 * C1M * R1 * R2 * s + C2M * R1 * R2 * s + C1M * C2M * R1 ** 2 * R2 * s ** 2 + 2 * C1M * C2M * R1 * R2 ** 2 * k * s ** 2 - 2 * C1M * C2M * R1 * R2 ** 2 * k ** 2 * s ** 2) * (
                                 2 * R1 + R2 + C2M * R1 ** 2 * s + C2M * R2 ** 2 * k * s - C2M * R2 ** 2 * k ** 2 * s + 2 * C1M * R1 * R2 * s + C2M * R1 * R2 * s + C2M * R1 * R3 * s + C2M * R2 * R3 * k * s + C1M * C2M * R1 ** 2 * R2 * s ** 2 + 2 * C1M * C2M * R1 * R2 ** 2 * k * s ** 2 - 2 * C1M * C2M * R1 * R2 ** 2 * k ** 2 * s ** 2 + C1M * C2M * R1 * R2 * R3 * s ** 2)))


t = get_transfer_zin(
    R1=560,
    R2=10*K,
    R3=100*K,
    C1L=1000*nano,
    C1M=100*nano,
    C1H=10*nano,
    C2L=100*nano,
    C2M=10*nano,
    C2H=1*nano)

h = get_rational_coeffs(t, s)

print(h)
