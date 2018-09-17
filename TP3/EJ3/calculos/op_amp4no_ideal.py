import sympy as sp

def get_rational_coeffs(expr,var):
    expr = sp.expand(expr)
    print(expr)
    num, denom = expr.as_numer_denom()

    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]


v1, v2, vx, vout1, vout2, vfeed, vout, s, a0, wp = sp.symbols("v1 v2 vx vout1 vout2 vfeed vout s a0 wp")

r1, r2, r3, r4, r5, r6, r7, r8, r9 = sp.symbols("r1 r2 r3 r4 r5 r6 r7 r8 r9")

h = sp.solve([
    (vout1-vout2)/r1-(vout2-vout)/r2,
    (vout1-v1)/r3-(v1-vx)/r4,
    (vfeed-vx)/r5-(vx-v1)/r4-(vx-v2)/r6,
    (vx-v2)/r6-(v2-vout2)/r7,
    a0 / (1 + s / wp)*vout2-vfeed,
    ],
    (vx, vout1, vout2, vfeed, vout)
)

print(h[vout])
print("racionalizando")

h = get_rational_coeffs(h[vout], s)

print(h)
