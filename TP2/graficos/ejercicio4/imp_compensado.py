from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


k = 10**3
mili = 10**(-3)
a0 = 10**(110/20)
bwp = 15*pow(10,6)

fp = bwp / a0
wp = fp * 2 * pi

fig, ax1 = plt.subplots()


def convert_map(datos):
    ans = dict()
    ans["f"] = [datos[i][0] for i in range(len(datos))]
    ans["abs"] = [datos[i][1] for i in range(len(datos))]
    ans["pha"] = [datos[i][2] for i in range(len(datos))]




datos_derivador = []





datos_integrador = []





def graficar_imp(mode,f_range,datos_medidos,spice_filename ,output_filename,data):
    w_range = [i * (2 * pi) for i in f_range]
    num = data[0]
    den = data[1]

    s1 = signal.lti(num, den)

    w, H = signal.freqresp(s1, w_range)

    f = [i / 2 / pi for i in w]
    Ha = [abs(i) for i in H]

    if mode=="mag":
        ax1.semilogx(f, abs(H), "yellow", linewidth=3)
    else:
        pass

    spice_data = read_file_spice("input/spice_data/" + spice_filename)

    for i in range(len(spice_data["abs"])):
        spice_data["abs"][i] = 10**(spice_data["abs"][i]/20.0)

    if mode == "mag":
        ax1.semilogx(spice_data["f"], spice_data["abs"], "magenta", linewidth=1, alpha=0.9)
    else:
        ax1.semilogx(spice_data["f"], spice_data["pha"], "magenta", linewidth=1, alpha=0.9)


    ax1.minorticks_on()
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')

    blue_patch = mpatches.Patch(color='yellow', label='teoria')
    green_patch = mpatches.Patch(color='magenta', label='simulacion')

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Impedancia (ohms)")

    plt.legend(handles=[green_patch, blue_patch])
    plt.savefig("output/contraste/" + output_filename, dpi=300)
    plt.cla()

r = 1800
c = 56 * (10**(-9))
r2 = 33
graficar_imp(
    mode="mag",
    data=[[-c*r - 2*c*r2, a0*c*r2*wp - 2*c*r*wp - 4*c*r2*wp - 1, a0*c*r2*wp**2 + a0*wp - c*r*wp**2 - 2*c*r2*wp**2 - 2*wp, a0*wp**2 - wp**2], [c, a0*c*wp + 2*c*wp, a0*c*wp**2 + c*wp**2, 0]],
    f_range=np.logspace(4,7,1000),
    datos_medidos=datos_derivador,
    spice_filename="derivador_caso2imp.txt",
    output_filename="derivador_imp_compensado.png"
)


r = 1800
c = 56 * (10**(-9))
r2 = 68*k
graficar_imp(
    mode="mag",
    data=[[-c**2*r*r2, a0*c**2*r*r2*wp - 2*c**2*r*r2*wp - c*r - c*r2, a0*c**2*r*r2*wp**2 + a0*c*r*wp - c**2*r*r2*wp**2 - 2*c*r*wp - 2*c*r2*wp, a0*c*r*wp**2 - c*r*wp**2 - c*r2*wp**2, 0], [c**2*r2, a0*c**2*r2*wp + 2*c**2*r2*wp + c, a0*c**2*r2*wp**2 + a0*c*wp + c**2*r2*wp**2 + 2*c*wp, a0*c*wp**2 + c*wp**2, 0]],
    f_range=np.logspace(2,7,1000),
    datos_medidos=datos_integrador,
    spice_filename="integrador_caso2imp.txt",
    output_filename="integrador_imp_compensado.png"
)