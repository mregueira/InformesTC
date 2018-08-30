### Calculos compensados contraste
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from random import *

k = 10**3
m = 10**6


a0 = 10**(110/20)
bwp = 15*(10**6)

fp = bwp / a0
wp = fp * 2 * pi

fig, ax1 = plt.subplots()

derivador_medidos = []

def function_derivador(r , r2 , c):
    return [[-a0 * c * (r + r2) / (a0 + 1), 0],
     [c * (r + 2 * r2) / (wp * (a0 + 1)), (a0 * c * r2 * wp + c * r * wp + 2 * c * r2 * wp + 1) / (wp * (a0 + 1)), 1]]

def function_integrador(r, r2 , c):
    return [[-a0*r2*wp], [c*r*r2, a0*c*r*r2*wp + c*r*r2*wp + r + r2, a0*r*wp + r*wp + r2*wp]]



def graficar(r,r2,c , h_func ,mode,f_range,datos, spice_filename , output_filename):
    w_range = [i * (2 * pi) for i in f_range]
    func = h_func(r, r2, c)
    H = signal.lti(func[0], func[1])
    w, mag, pha = signal.bode(H, w_range)
    poles = H.poles
    for i in range(len(poles)):
        poles[i] = poles[i] / 2 / pi
    print(poles)

    f = [i / 2 / pi for i in w]

    if mode == "mag":
        ax1.semilogx(f, mag, "red", linewidth=3)
    else:
        ax1.semilogx(f, pha, "red", linewidth=3)

    plt.xlabel("Frecuencia (Hz)")
    if mode=="mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")

    spice_data = read_file_spice("input/spice_data/"+spice_filename)


    for i in range(len(spice_data["pha"])):
        if spice_data["pha"][i] > 0:
            spice_data["pha"][i] -= 360
    if mode=="mag":
        ax1.semilogx(spice_data["f"], spice_data["abs"], "magenta", linewidth=1,alpha=0.9)
    else:
        ax1.semilogx(spice_data["f"], spice_data["pha"], "magenta",linewidth=1,alpha=0.9)


    teorico_patch = mpatches.Patch(color="red",label="Teórico")
    simulado_patch = mpatches.Patch(color="magenta",label="Simulado")

    plt.legend(handles=[teorico_patch , simulado_patch])
    plt.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.savefig("output/contraste/" + output_filename, dpi=300)
    plt.cla()

graficar(r = 1800,
         r2 = 33,
         c = 56*(10**(-9)),
         h_func = function_derivador,
         f_range=np.logspace(3,7,10000),
         mode = "mag",
         datos = derivador_medidos,
         spice_filename="derivador_caso2.txt",
         output_filename="derivador_compensado_contrasteA.png")

graficar(r = 1800,
         r2 = 33,
         c = 56*(10**(-9)),
         h_func = function_derivador,
         f_range=np.logspace(2,7,10000),
         mode = "pha",
         datos = derivador_medidos,
         spice_filename="derivador_caso2.txt",
         output_filename="derivador_compensado_contrasteA_fase.png")

graficar(r = 1800,
         r2 = 33,
         c = 56*(10**(-9)),
         h_func = function_integrador,
         f_range=np.logspace(3,7,10000),
         mode = "mag",
         datos = derivador_medidos,
         spice_filename="derivador_caso2.txt",
         output_filename="derivador_compensado_contrasteA.png")
