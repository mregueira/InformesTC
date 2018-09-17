import sympy as sp
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import read_spice
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax1 = plt.subplots()

def add_legend(mode,l1,l2,l3):
    blue_patch = mpatches.Patch(color='blue', label=l1)
    red_patch = mpatches.Patch(color='red', label=l2)
    green_patch = mpatches.Patch(color='green', label=l3)

    ax1.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (Hz)")
    if mode == "mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")

    plt.legend(handles=[green_patch, blue_patch, red_patch])


def get_rational_coeffs(expr,var):
    num, denom = expr.as_numer_denom()
    #print(num,denom)
    data = [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]
    return data

def graficar_op_amp4():
    a0 = 200 * (10**3)

    bwp = 3 * (10**6)
    fp = bwp / a0

    wp = fp * 2 * pi

    k = 10**3
    m = 10**6

    r1 = 1*k
    r2 = 100*k
    r3 = 1*k
    r4 = 3.3*k
    r5 = 10
    r6 = 3.3*k
    r7 = 1*k
    r8 = 1*k
    r9 = 100*k

    v1 = 1/2
    v2 = 1/2

    h = [[r1*r4**2*r5*r6*v2*wp + r1*r4**2*r6**2*v2*wp + r1*r4**2*r6*r7*v2*wp + r1*r4*r5*r6**2*v2*wp - r1*r4*r5*r6*r7*v1*wp + r1*r4*r5*r6*r7*v2*wp - r2*r3*r4*r5*r6*v1*wp + r2*r3*r4*r5*r6*v2*wp - r2*r3*r4*r6**2*v1*wp - r2*r4**2*r5*r6*v1*wp + r2*r4**2*r5*r6*v2*wp - r2*r4**2*r6**2*v1*wp + r2*r4**2*r6**2*v2*wp + r2*r4**2*r6*r7*v2*wp - r2*r4*r5*r6**2*v1*wp + r2*r4*r5*r6**2*v2*wp - r2*r4*r5*r6*r7*v1*wp + r2*r4*r5*r6*r7*v2*wp, a0*r2*r3*r4*r6**2*v2*wp - a0*r2*r3*r4*r6*r7*v1*wp + a0*r2*r3*r4*r6*r7*v2*wp - a0*r2*r4**2*r6*r7*v1*wp + r1*r4**2*r5*r6*v2 + r1*r4**2*r6**2*v2 + r1*r4**2*r6*r7*v2 + r1*r4*r5*r6**2*v2 - r1*r4*r5*r6*r7*v1 + r1*r4*r5*r6*r7*v2 - r2*r3*r4*r5*r6*v1 + r2*r3*r4*r5*r6*v2 - r2*r3*r4*r6**2*v1 - r2*r4**2*r5*r6*v1 + r2*r4**2*r5*r6*v2 - r2*r4**2*r6**2*v1 + r2*r4**2*r6**2*v2 + r2*r4**2*r6*r7*v2 - r2*r4*r5*r6**2*v1 + r2*r4*r5*r6**2*v2 - r2*r4*r5*r6*r7*v1 + r2*r4*r5*r6*r7*v2], [r1*r4**2*r5*r6*wp + r1*r4**2*r6**2*wp + r1*r4*r5*r6**2*wp, a0*r1*r4**2*r6*r7*wp + r1*r4**2*r5*r6 + r1*r4**2*r6**2 + r1*r4*r5*r6**2]]
    s1 = signal.lti(h[0], h[1])
    f_range = np.logspace(2, 8, 10000)
    w_range = [2*pi*i for i in f_range]

    w, mag, pha = signal.bode(s1, w_range)
    f = [i / 2 / pi for i in w]

    data_spice = read_spice.read_file_spice("input/ej3 tp3 no ideal.txt")
    ax1.semilogx(f, mag, "blue")
    ax1.semilogx(data_spice["f"],data_spice["abs"],"red")

    add_legend(mode="mag", l1="Teórico", l2="Simulado", l3="")

    plt.show()

graficar_op_amp4()