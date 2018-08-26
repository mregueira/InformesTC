import sympy as sp

def get_rational_coeffs(expr,var):
    num, denom = expr.as_numer_denom()
    #print(num,denom)
    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]



#### Caso derivador no ideal - Avol finito

a0, r , c , s , wp , Z2 , Z1 , a = sp.symbols("a0 r c s wp Z2 Z1 a")
#
Z1 = 1 / (s*c)
Z2 = r

H = -Z2/Z1 / (1+ (Z1+Z2)/(a0*Z1) )

coef = get_rational_coeffs(H,s)


num = []
den = []

for i in range(len(coef[0])):
    num.append(sp.simplify(coef[0][i] / (r*c**2)) )
for i in range(len(coef[1])):
    den.append(sp.simplify(coef[1][i] / (r*c**2)) )

print("Avol finito independiente de w, numerador/denominador")

print(num)
print(den)


print("Avol finito dependiente de w, numerador/denominador")

a = a0 / (s/wp + 1)
H = -Z2/Z1 / (1+ (Z1+Z2)/(a*Z1) )

coef = get_rational_coeffs(H,s)

num = [sp.simplify(coef[0][i] / (r*c**2))  for i in range(len(coef[0]))]
den = [sp.simplify(coef[1][i] / (r*c**2)) for i in range(len(coef[1]))]

print(num)
print(den)

