import sympy as sp

v1, v2, vx, vout1, vfeed, vout = sp.symbols("v1 v2 vx vfeed vout")

r1, r2, r3, r4, r5, r6, r7, r8, r9 = sp.symbols("r1 r2 r3 r4 r5 r6 r7 r8 r9")


h = sp.solve(
    [(vout1-v1)/r3, (v1-vx)/r4]
)