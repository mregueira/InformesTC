from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

w_range = np.logspace(4,8)
A0 = 10**(110/20)
BWP = 15*pow(10,6)

FP = BWP / A0
WP = FP * 2 * pi

fig, ax1 = plt.subplots()

def get_rational_coeffs(expr,var):
    num, denom = expr.as_numer_denom()
    #print(num,denom)
    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]

def dibujar_bode(R,C, input_filename,spice_filename ,output_filename):
    a0, r , c , s , w_p , Z2 , Z1 , A = sp.symbols("a0 r c s w_p Z2 Z1 A")

    Z1 = 1 / (s*c)
    Z2 = r

    A = A0 / (s / WP + 1)

    H = (Z2/(Z1+Z2))/ (-1/A - Z1/(Z1+Z2))
    print(H)

    H = H.subs(r,R)
    H = H.subs(c,C)
    H = H.subs(a0,A0)
    H = H.subs(w_p,WP)
    print("fp=",FP)
    print("1/RC=",1/(R*C)/2/pi)

    coef = get_rational_coeffs(H,s)
    for i in range(len(coef[0])):
        coef[0][i] = float(coef[0][i].evalf())
    for i in range(len(coef[1])):
        coef[1][i] = float(coef[1][i].evalf())
    print(coef)
    s1 = signal.lti(coef[0],coef[1])

    w, mag, phase = signal.bode(s1, w_range)
    f = [i / 2 / pi for i in w]

    ax1.semilogx(f, mag, "blue", linewidth="2")

    spice_data = read_file_spice(spice_filename)

    ax1.semilogx(spice_data["f"],spice_data["abs"])

dibujar_bode(1800,56*(10**(-9) ),"","input/caso1_derivador_sc.txt","")
#dibujar_bode(1500,5.8*pow(10,-9),"","","")\

ax1.set_axisbelow(True)
ax1.minorticks_on()
ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

plt.show()
