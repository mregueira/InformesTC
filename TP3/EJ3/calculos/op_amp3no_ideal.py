import sympy as sp


def get_rational_coeffs(expr,var):
    expr = sp.expand(expr)
    print(expr)
    num, denom = expr.as_numer_denom()

    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]


v1, v2, vx, vout1, vout, vd, s, a0, wp = sp.symbols("v1 v2 vx vout1 vout vd s a0 wp")

r1, r2, r3, r4, r5, r6, r7, r8, r9 = sp.symbols("r1 r2 r3 r4 r5 r6 r7 r8 r9")

h = sp.solve([
    (0-v2)/r7-(v2-vx)/r6,
    (vx-v1)/r4-(v1-vout1)/r3,
    (vout1+vd)/r1-(-vd-vout)/r2,
    (a0*vd/(1+s/wp)-vout)],
    (vx, vout1, vout, vd)
)

print(h[vout])
print("racionalizando")

h = get_rational_coeffs(h[vout], s)
print(h)
