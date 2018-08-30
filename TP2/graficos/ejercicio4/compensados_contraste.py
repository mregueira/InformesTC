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
    [180*k, 35, -202],
    [190*k, 34.9, -207],
    [200*k, 34.9, -213],
    [250*k, 33.3, -221],
    [300*k, 33.3, 132-360],
    [400*k, 31.3, 114-360],
    [500*k, 29.1, 100-360],
    [600*k,27.2,90-360],
    [700*k,25.4,83-360],
    [800*k,23.8,78-360],
    [1*m,21.2,70-360],
    [2*m,13.1,52-360],
    [3*m,8.5,42-360]
]

medidos_integrador = [
    [10,32.8,166],
    [25,31.4,150],
    [50,28.4,124],
    [100,23.6,110],
    [150,20.4,106],
    [200,18,100],
    [300,14.6,97],
    [400,12.1,95],
    [500,10.2,94],
    [700,7.3,93],
    [1*k,4.1,92],
    [1.5*k,0.6,92],
    [2*k,-1.8,92],
    [3*k,-5.4,91],
    [4*k,-7.9,91],
    [5*k,-9.8,90],
    [7*k,-12.8,91],
    [8*k,-13.9,90],
    [10*k,-15.8,90],
    [15*k,-19.3,90],
    [20*k,-21.7,90],
    [30*k,-25.4,90],
    [50*k,-29.9,90],
    [70*k,-32.4,90],
    [100*k,-35,90],
    [150*k,-39.4,90],
    [200*k,-41.8,90],
    [300*k,-44.8,91],
    [400*k,-47.8,90],
    [500*k,-48,90],
    [700*k,-49.2,90],
    [m,-48.9,100],
    [1.5*m,-48.1,104],

]


medidos_derivador = convert_map(medidos_derivador)
medidos_integrador = convert_map(medidos_integrador)

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

#graficar(r = 1800,
#         r2 = 33,
#         c = 56*(10**(-9)),
#         h_func = function_derivador,
#         f_range=np.logspace(3,7,10000),
#         mode = "mag",
#         datos = medidos_derivador,
#         spice_filename="derivador_caso2.txt",
#         output_filename="derivador_compensado_contrasteA.png")

#graficar(r = 1800,
#         r2 = 33,
#         c = 56*(10**(-9)),
#         h_func = function_derivador,
#         f_range=np.logspace(2,7,10000),
#         mode = "pha",
#         datos = medidos_derivador,
#         spice_filename="derivador_caso2.txt",
#         output_filename="derivador_compensado_contrasteA_fase.png")

graficar(r = 1800,
         r2 = 82*k,
         c = 56*(10**(-9)),
         h_func = function_integrador,
         f_range=np.logspace(1,7,10000),
         mode = "mag",
         datos = medidos_integrador,
         spice_filename="integrador_caso2.txt",
         output_filename="integrador_compensado_contrasteA.png")

graficar(r = 1800,
         r2 = 82*k,
         c = 56*(10**(-9)),
         h_func = function_integrador,
         f_range=np.logspace(1,7,10000),
         mode = "pha",
         datos = medidos_integrador,
         spice_filename="integrador_caso2.txt",
         output_filename="integrador_compensado_contrasteA_fase.png")
