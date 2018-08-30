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

def convert_map(datos):
    ans = dict()
    ans["f"] = [datos[i][0] for i in range(len(datos))]
    ans["abs"] = [datos[i][1] for i in range(len(datos))]
    ans["pha"] = [datos[i][2] for i in range(len(datos))]

    return ans



medidos_derivador = [
    [100, -24,-90],
    [1*k,-4,-90],
    [2*k,2,-91],
    [3*k,5.4,-93],
    [4*k,7.9,-95],
    [5*k, 9.8,-94],
    [6*k, 11.4, -95],
    [7*k,12.7,-94],
    [8*k, 13.9, -95],
    [9*k, 14.9, -95],
    [10*k, 15.8, -97],
    [20*k,21.7,-103],
    [30*k, 25.1, -110],
    [40*k,27.4,-117],
    [50*k, 29.2, -123],
    [60*k, 30.5, -131],
    [70*k, 31.6, -136],
    [80*k, 32.5, -143],
    [90*k, 33.4, -154],
    [100*k, 33.7,-155 ],
    [110*k, 34.1, -161],
    [120*k, 34.4,-167],
    [130*k, 34.7, -173],
    [140*k, 34.9, -180],
    [150*k, 34.9, -185],
    [160*k, 34.9, -190],
    [170*k, 34.7, -197],
    [180*k, 34.4, -202],
    [190*k, 34, -207],
    [200*k, 33.5, -213],
    [250*k, 33.3, -221],
    [300*k, 31.1, -239]





]



medidos_derivador = convert_map(medidos_derivador)


def function_derivador(r , r2 , c):
    return [[-a0*c*r/(a0 + 1), 0], [c*(r + r2)/(wp*(a0 + 1)), (a0*c*r2*wp + c*r*wp + c*r2*wp + 1)/(wp*(a0 + 1)), 1]]

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

    if mode=="mag":
        ax1.semilogx(datos["f"],datos["abs"],"cyan",linewidth=1.5,alpha=1)
    else:
        ax1.semilogx(datos["f"],datos["pha"],"cyan",linewidth=1.5,alpha=1)


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
         datos = medidos_derivador,
         spice_filename="derivador_caso2.txt",
         output_filename="derivador_compensado_contrasteA.png")

graficar(r = 1800,
         r2 = 33,
         c = 56*(10**(-9)),
         h_func = function_derivador,
         f_range=np.logspace(2,7,10000),
         mode = "pha",
         datos = medidos_derivador,
         spice_filename="derivador_caso2.txt",
         output_filename="derivador_compensado_contrasteA_fase.png")

#graficar(r = 1800,
#         r2 = 100,
#         c = 56*(10**(-9)),
#         h_func = function_integrador,
#         f_range=np.logspace(3,7,10000),
#         mode = "mag",
#         datos = derivador_medidos,
#         spice_filename="integrador_caso2.txt",
#         output_filename="integrador_compensado_contrasteA.png")
