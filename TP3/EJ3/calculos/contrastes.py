import sympy as sp
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import read_spice
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax1 = plt.subplots()

k = 10 ** 3
m = 10 ** 6

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

    a0 = 200 * k

    bwp = 3 * m
    fp = bwp / a0

    wp = fp * 2 * pi


    r1 = 1*k
    r2 = 100*k
    r3 = 1*k
    r4 = 3.3*k
    r5 = 10
    r6 = 3.3*k
    r7 = 1*k
    r8 = 1*k
    r9 = 100*k

    v1 = 1
    v2 = 1

    h = [[a0**2*r1*r3*r4*r5*r6*v2*wp**2 + a0**2*r1*r3*r4*r6**2*v2*wp**2 + a0**2*r1*r3*r4*r6*r7*v2*wp**2 + a0**2*r1*r4**2*r5*r6*v2*wp**2 + a0**2*r1*r4**2*r6**2*v2*wp**2 + a0**2*r1*r4**2*r6*r7*v2*wp**2 + a0**2*r1*r4*r5*r6**2*v2*wp**2 + a0**2*r1*r4*r5*r6*r7*v2*wp**2 - a0**2*r2*r3*r4*r5*r6*v1*wp**2 + a0**2*r2*r3*r4*r5*r6*v2*wp**2 - a0**2*r2*r3*r4*r6**2*v1*wp**2 + a0**2*r2*r3*r4*r6**2*v2*wp**2 - a0**2*r2*r3*r4*r6*r7*v1*wp**2 + a0**2*r2*r3*r4*r6*r7*v2*wp**2 - a0**2*r2*r4**2*r5*r6*v1*wp**2 + a0**2*r2*r4**2*r5*r6*v2*wp**2 - a0**2*r2*r4**2*r6**2*v1*wp**2 + a0**2*r2*r4**2*r6**2*v2*wp**2 - a0**2*r2*r4**2*r6*r7*v1*wp**2 + a0**2*r2*r4**2*r6*r7*v2*wp**2 - a0**2*r2*r4*r5*r6**2*v1*wp**2 + a0**2*r2*r4*r5*r6**2*v2*wp**2 - a0**2*r2*r4*r5*r6*r7*v1*wp**2 + a0**2*r2*r4*r5*r6*r7*v2*wp**2, a0**3*r1*r4**2*r5*r6*v2*wp**3 + a0**3*r1*r4**2*r6**2*v2*wp**3 + a0**3*r1*r4**2*r6*r7*v2*wp**3 + a0**3*r1*r4*r5*r6**2*v2*wp**3 - a0**3*r1*r4*r5*r6*r7*v1*wp**3 + a0**3*r1*r4*r5*r6*r7*v2*wp**3 - a0**3*r2*r3*r4*r5*r6*v1*wp**3 + a0**3*r2*r3*r4*r5*r6*v2*wp**3 - a0**3*r2*r3*r4*r6**2*v1*wp**3 - a0**3*r2*r4**2*r5*r6*v1*wp**3 + a0**3*r2*r4**2*r5*r6*v2*wp**3 - a0**3*r2*r4**2*r6**2*v1*wp**3 + a0**3*r2*r4**2*r6**2*v2*wp**3 + a0**3*r2*r4**2*r6*r7*v2*wp**3 - a0**3*r2*r4*r5*r6**2*v1*wp**3 + a0**3*r2*r4*r5*r6**2*v2*wp**3 - a0**3*r2*r4*r5*r6*r7*v1*wp**3 + a0**3*r2*r4*r5*r6*r7*v2*wp**3 + 2*a0**2*r1*r3*r4*r5*r6*v2*wp**3 + 2*a0**2*r1*r3*r4*r6**2*v2*wp**3 + 2*a0**2*r1*r3*r4*r6*r7*v2*wp**3 + 2*a0**2*r1*r4**2*r5*r6*v2*wp**3 + 2*a0**2*r1*r4**2*r6**2*v2*wp**3 + 2*a0**2*r1*r4**2*r6*r7*v2*wp**3 + 2*a0**2*r1*r4*r5*r6**2*v2*wp**3 + 2*a0**2*r1*r4*r5*r6*r7*v2*wp**3 - 2*a0**2*r2*r3*r4*r5*r6*v1*wp**3 + 2*a0**2*r2*r3*r4*r5*r6*v2*wp**3 - 2*a0**2*r2*r3*r4*r6**2*v1*wp**3 + 2*a0**2*r2*r3*r4*r6**2*v2*wp**3 - 2*a0**2*r2*r3*r4*r6*r7*v1*wp**3 + 2*a0**2*r2*r3*r4*r6*r7*v2*wp**3 - 2*a0**2*r2*r4**2*r5*r6*v1*wp**3 + 2*a0**2*r2*r4**2*r5*r6*v2*wp**3 - 2*a0**2*r2*r4**2*r6**2*v1*wp**3 + 2*a0**2*r2*r4**2*r6**2*v2*wp**3 - 2*a0**2*r2*r4**2*r6*r7*v1*wp**3 + 2*a0**2*r2*r4**2*r6*r7*v2*wp**3 - 2*a0**2*r2*r4*r5*r6**2*v1*wp**3 + 2*a0**2*r2*r4*r5*r6**2*v2*wp**3 - 2*a0**2*r2*r4*r5*r6*r7*v1*wp**3 + 2*a0**2*r2*r4*r5*r6*r7*v2*wp**3, a0**4*r2*r3*r4*r6**2*v2*wp**4 - a0**4*r2*r3*r4*r6*r7*v1*wp**4 + a0**4*r2*r3*r4*r6*r7*v2*wp**4 - a0**4*r2*r4**2*r6*r7*v1*wp**4 + a0**3*r1*r4**2*r5*r6*v2*wp**4 + a0**3*r1*r4**2*r6**2*v2*wp**4 + a0**3*r1*r4**2*r6*r7*v2*wp**4 + a0**3*r1*r4*r5*r6**2*v2*wp**4 - a0**3*r1*r4*r5*r6*r7*v1*wp**4 + a0**3*r1*r4*r5*r6*r7*v2*wp**4 - a0**3*r2*r3*r4*r5*r6*v1*wp**4 + a0**3*r2*r3*r4*r5*r6*v2*wp**4 - a0**3*r2*r3*r4*r6**2*v1*wp**4 - a0**3*r2*r4**2*r5*r6*v1*wp**4 + a0**3*r2*r4**2*r5*r6*v2*wp**4 - a0**3*r2*r4**2*r6**2*v1*wp**4 + a0**3*r2*r4**2*r6**2*v2*wp**4 + a0**3*r2*r4**2*r6*r7*v2*wp**4 - a0**3*r2*r4*r5*r6**2*v1*wp**4 + a0**3*r2*r4*r5*r6**2*v2*wp**4 - a0**3*r2*r4*r5*r6*r7*v1*wp**4 + a0**3*r2*r4*r5*r6*r7*v2*wp**4 + a0**2*r1*r3*r4*r5*r6*v2*wp**4 + a0**2*r1*r3*r4*r6**2*v2*wp**4 + a0**2*r1*r3*r4*r6*r7*v2*wp**4 + a0**2*r1*r4**2*r5*r6*v2*wp**4 + a0**2*r1*r4**2*r6**2*v2*wp**4 + a0**2*r1*r4**2*r6*r7*v2*wp**4 + a0**2*r1*r4*r5*r6**2*v2*wp**4 + a0**2*r1*r4*r5*r6*r7*v2*wp**4 - a0**2*r2*r3*r4*r5*r6*v1*wp**4 + a0**2*r2*r3*r4*r5*r6*v2*wp**4 - a0**2*r2*r3*r4*r6**2*v1*wp**4 + a0**2*r2*r3*r4*r6**2*v2*wp**4 - a0**2*r2*r3*r4*r6*r7*v1*wp**4 + a0**2*r2*r3*r4*r6*r7*v2*wp**4 - a0**2*r2*r4**2*r5*r6*v1*wp**4 + a0**2*r2*r4**2*r5*r6*v2*wp**4 - a0**2*r2*r4**2*r6**2*v1*wp**4 + a0**2*r2*r4**2*r6**2*v2*wp**4 - a0**2*r2*r4**2*r6*r7*v1*wp**4 + a0**2*r2*r4**2*r6*r7*v2*wp**4 - a0**2*r2*r4*r5*r6**2*v1*wp**4 + a0**2*r2*r4*r5*r6**2*v2*wp**4 - a0**2*r2*r4*r5*r6*r7*v1*wp**4 + a0**2*r2*r4*r5*r6*r7*v2*wp**4], [r1*r3*r4*r5*r6 + r1*r3*r4*r6**2 + r1*r3*r4*r6*r7 + r1*r4**2*r5*r6 + r1*r4**2*r6**2 + r1*r4**2*r6*r7 + r1*r4*r5*r6**2 + r1*r4*r5*r6*r7 + r2*r3*r4*r5*r6 + r2*r3*r4*r6**2 + r2*r3*r4*r6*r7 + r2*r4**2*r5*r6 + r2*r4**2*r6**2 + r2*r4**2*r6*r7 + r2*r4*r5*r6**2 + r2*r4*r5*r6*r7, 2*a0*r1*r3*r4*r5*r6*wp + 2*a0*r1*r3*r4*r6**2*wp + a0*r1*r3*r4*r6*r7*wp + 3*a0*r1*r4**2*r5*r6*wp + 3*a0*r1*r4**2*r6**2*wp + 2*a0*r1*r4**2*r6*r7*wp + 3*a0*r1*r4*r5*r6**2*wp + 2*a0*r1*r4*r5*r6*r7*wp + a0*r2*r3*r4*r5*r6*wp + a0*r2*r3*r4*r6**2*wp + 2*a0*r2*r4**2*r5*r6*wp + 2*a0*r2*r4**2*r6**2*wp + a0*r2*r4**2*r6*r7*wp + 2*a0*r2*r4*r5*r6**2*wp + a0*r2*r4*r5*r6*r7*wp + 4*r1*r3*r4*r5*r6*wp + 4*r1*r3*r4*r6**2*wp + 4*r1*r3*r4*r6*r7*wp + 4*r1*r4**2*r5*r6*wp + 4*r1*r4**2*r6**2*wp + 4*r1*r4**2*r6*r7*wp + 4*r1*r4*r5*r6**2*wp + 4*r1*r4*r5*r6*r7*wp + 4*r2*r3*r4*r5*r6*wp + 4*r2*r3*r4*r6**2*wp + 4*r2*r3*r4*r6*r7*wp + 4*r2*r4**2*r5*r6*wp + 4*r2*r4**2*r6**2*wp + 4*r2*r4**2*r6*r7*wp + 4*r2*r4*r5*r6**2*wp + 4*r2*r4*r5*r6*r7*wp, a0**2*r1*r3*r4*r5*r6*wp**2 + a0**2*r1*r3*r4*r6**2*wp**2 + a0**2*r1*r3*r4*r6*r7*wp**2 + 3*a0**2*r1*r4**2*r5*r6*wp**2 + 3*a0**2*r1*r4**2*r6**2*wp**2 + 2*a0**2*r1*r4**2*r6*r7*wp**2 + 3*a0**2*r1*r4*r5*r6**2*wp**2 + a0**2*r1*r4*r5*r6*r7*wp**2 + a0**2*r2*r3*r4*r6*r7*wp**2 + a0**2*r2*r4**2*r5*r6*wp**2 + a0**2*r2*r4**2*r6**2*wp**2 + a0**2*r2*r4**2*r6*r7*wp**2 + a0**2*r2*r4*r5*r6**2*wp**2 + 6*a0*r1*r3*r4*r5*r6*wp**2 + 6*a0*r1*r3*r4*r6**2*wp**2 + 3*a0*r1*r3*r4*r6*r7*wp**2 + 9*a0*r1*r4**2*r5*r6*wp**2 + 9*a0*r1*r4**2*r6**2*wp**2 + 6*a0*r1*r4**2*r6*r7*wp**2 + 9*a0*r1*r4*r5*r6**2*wp**2 + 6*a0*r1*r4*r5*r6*r7*wp**2 + 3*a0*r2*r3*r4*r5*r6*wp**2 + 3*a0*r2*r3*r4*r6**2*wp**2 + 6*a0*r2*r4**2*r5*r6*wp**2 + 6*a0*r2*r4**2*r6**2*wp**2 + 3*a0*r2*r4**2*r6*r7*wp**2 + 6*a0*r2*r4*r5*r6**2*wp**2 + 3*a0*r2*r4*r5*r6*r7*wp**2 + 6*r1*r3*r4*r5*r6*wp**2 + 6*r1*r3*r4*r6**2*wp**2 + 6*r1*r3*r4*r6*r7*wp**2 + 6*r1*r4**2*r5*r6*wp**2 + 6*r1*r4**2*r6**2*wp**2 + 6*r1*r4**2*r6*r7*wp**2 + 6*r1*r4*r5*r6**2*wp**2 + 6*r1*r4*r5*r6*r7*wp**2 + 6*r2*r3*r4*r5*r6*wp**2 + 6*r2*r3*r4*r6**2*wp**2 + 6*r2*r3*r4*r6*r7*wp**2 + 6*r2*r4**2*r5*r6*wp**2 + 6*r2*r4**2*r6**2*wp**2 + 6*r2*r4**2*r6*r7*wp**2 + 6*r2*r4*r5*r6**2*wp**2 + 6*r2*r4*r5*r6*r7*wp**2, a0**3*r1*r3*r4*r6*r7*wp**3 + a0**3*r1*r4**2*r5*r6*wp**3 + a0**3*r1*r4**2*r6**2*wp**3 + 2*a0**3*r1*r4**2*r6*r7*wp**3 + a0**3*r1*r4*r5*r6**2*wp**3 + a0**3*r2*r4**2*r6*r7*wp**3 + 2*a0**2*r1*r3*r4*r5*r6*wp**3 + 2*a0**2*r1*r3*r4*r6**2*wp**3 + 2*a0**2*r1*r3*r4*r6*r7*wp**3 + 6*a0**2*r1*r4**2*r5*r6*wp**3 + 6*a0**2*r1*r4**2*r6**2*wp**3 + 4*a0**2*r1*r4**2*r6*r7*wp**3 + 6*a0**2*r1*r4*r5*r6**2*wp**3 + 2*a0**2*r1*r4*r5*r6*r7*wp**3 + 2*a0**2*r2*r3*r4*r6*r7*wp**3 + 2*a0**2*r2*r4**2*r5*r6*wp**3 + 2*a0**2*r2*r4**2*r6**2*wp**3 + 2*a0**2*r2*r4**2*r6*r7*wp**3 + 2*a0**2*r2*r4*r5*r6**2*wp**3 + 6*a0*r1*r3*r4*r5*r6*wp**3 + 6*a0*r1*r3*r4*r6**2*wp**3 + 3*a0*r1*r3*r4*r6*r7*wp**3 + 9*a0*r1*r4**2*r5*r6*wp**3 + 9*a0*r1*r4**2*r6**2*wp**3 + 6*a0*r1*r4**2*r6*r7*wp**3 + 9*a0*r1*r4*r5*r6**2*wp**3 + 6*a0*r1*r4*r5*r6*r7*wp**3 + 3*a0*r2*r3*r4*r5*r6*wp**3 + 3*a0*r2*r3*r4*r6**2*wp**3 + 6*a0*r2*r4**2*r5*r6*wp**3 + 6*a0*r2*r4**2*r6**2*wp**3 + 3*a0*r2*r4**2*r6*r7*wp**3 + 6*a0*r2*r4*r5*r6**2*wp**3 + 3*a0*r2*r4*r5*r6*r7*wp**3 + 4*r1*r3*r4*r5*r6*wp**3 + 4*r1*r3*r4*r6**2*wp**3 + 4*r1*r3*r4*r6*r7*wp**3 + 4*r1*r4**2*r5*r6*wp**3 + 4*r1*r4**2*r6**2*wp**3 + 4*r1*r4**2*r6*r7*wp**3 + 4*r1*r4*r5*r6**2*wp**3 + 4*r1*r4*r5*r6*r7*wp**3 + 4*r2*r3*r4*r5*r6*wp**3 + 4*r2*r3*r4*r6**2*wp**3 + 4*r2*r3*r4*r6*r7*wp**3 + 4*r2*r4**2*r5*r6*wp**3 + 4*r2*r4**2*r6**2*wp**3 + 4*r2*r4**2*r6*r7*wp**3 + 4*r2*r4*r5*r6**2*wp**3 + 4*r2*r4*r5*r6*r7*wp**3, a0**4*r1*r4**2*r6*r7*wp**4 + a0**3*r1*r3*r4*r6*r7*wp**4 + a0**3*r1*r4**2*r5*r6*wp**4 + a0**3*r1*r4**2*r6**2*wp**4 + 2*a0**3*r1*r4**2*r6*r7*wp**4 + a0**3*r1*r4*r5*r6**2*wp**4 + a0**3*r2*r4**2*r6*r7*wp**4 + a0**2*r1*r3*r4*r5*r6*wp**4 + a0**2*r1*r3*r4*r6**2*wp**4 + a0**2*r1*r3*r4*r6*r7*wp**4 + 3*a0**2*r1*r4**2*r5*r6*wp**4 + 3*a0**2*r1*r4**2*r6**2*wp**4 + 2*a0**2*r1*r4**2*r6*r7*wp**4 + 3*a0**2*r1*r4*r5*r6**2*wp**4 + a0**2*r1*r4*r5*r6*r7*wp**4 + a0**2*r2*r3*r4*r6*r7*wp**4 + a0**2*r2*r4**2*r5*r6*wp**4 + a0**2*r2*r4**2*r6**2*wp**4 + a0**2*r2*r4**2*r6*r7*wp**4 + a0**2*r2*r4*r5*r6**2*wp**4 + 2*a0*r1*r3*r4*r5*r6*wp**4 + 2*a0*r1*r3*r4*r6**2*wp**4 + a0*r1*r3*r4*r6*r7*wp**4 + 3*a0*r1*r4**2*r5*r6*wp**4 + 3*a0*r1*r4**2*r6**2*wp**4 + 2*a0*r1*r4**2*r6*r7*wp**4 + 3*a0*r1*r4*r5*r6**2*wp**4 + 2*a0*r1*r4*r5*r6*r7*wp**4 + a0*r2*r3*r4*r5*r6*wp**4 + a0*r2*r3*r4*r6**2*wp**4 + 2*a0*r2*r4**2*r5*r6*wp**4 + 2*a0*r2*r4**2*r6**2*wp**4 + a0*r2*r4**2*r6*r7*wp**4 + 2*a0*r2*r4*r5*r6**2*wp**4 + a0*r2*r4*r5*r6*r7*wp**4 + r1*r3*r4*r5*r6*wp**4 + r1*r3*r4*r6**2*wp**4 + r1*r3*r4*r6*r7*wp**4 + r1*r4**2*r5*r6*wp**4 + r1*r4**2*r6**2*wp**4 + r1*r4**2*r6*r7*wp**4 + r1*r4*r5*r6**2*wp**4 + r1*r4*r5*r6*r7*wp**4 + r2*r3*r4*r5*r6*wp**4 + r2*r3*r4*r6**2*wp**4 + r2*r3*r4*r6*r7*wp**4 + r2*r4**2*r5*r6*wp**4 + r2*r4**2*r6**2*wp**4 + r2*r4**2*r6*r7*wp**4 + r2*r4*r5*r6**2*wp**4 + r2*r4*r5*r6*r7*wp**4]]
    s1 = signal.lti(h[0], h[1])
    f_range = np.logspace(2, 8, 10000)
    w_range = [2*pi*i for i in f_range]

    w, mag, pha = signal.bode(s1, w_range)
    f = [i / 2 / pi for i in w]

    data_spice = read_spice.read_file_spice("input/ej3 tp3 no ideal comun.txt")
    ax1.semilogx(f, mag, "blue",linewidth=4)
    ax1.semilogx(data_spice["f"],data_spice["abs"],"red")

    add_legend(mode="mag", l1="Teórico", l2="Simulado", l3="")

    plt.show()

graficar_op_amp4()