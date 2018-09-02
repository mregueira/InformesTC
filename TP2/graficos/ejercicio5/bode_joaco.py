
import sympy as sp
from read_spice import *
import numpy as np
from scipy import signal
from math import *
import pandas as pd
import plotly.plotly as py
import plotly.tools as tls
from pylab import *
from scipy import signal


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def convert_map(datos):
    ans = dict()
    ans["f"] = [datos[i][0] for i in range(len(datos))]
    ans["abs"] = [datos[i][1] for i in range(len(datos))]
    ans["pha"] = [datos[i][2] for i in range(len(datos))]

    return ans


fig, ax1 = plt.subplots()
k = 10**(3)
m = 10**(6)
datos_circuito =[
    [5,-8.9,209-360],
    [6,-4.7,205-360],
    [8,1.9,170-360],
    [10,6.5,162-360],
    [15,13.8,149-360],
    [20,17.9,125-360],
    [30,22,95-360],
    [50,24.8,62-360],
    [70,26,45-360],
    [100,26.3,32-360],
    [150,26.6,22-360],
    [200,26.7,16-360],
    [300,26.8,11-360],
    [400,26.8,7-360],
    [500,26.8,5-360],
    [700,26.8,3-360],
    [k,26.8,0-360],
    [1.5*k,26.8,-2-360],
    [2*k,26.8,-4-360],
    [3*k,26.7,-8-360],
    [5*k,26.6,-14-360],
    [7*k,26.5,-19-360],
    [9*k,26.3,-24-360],
    [11*k,26,-28-360],
    [15*k,25.4,-38-360],
    [17*k,25.1,-43-360],
    [19*k,24.7,-46-360],
    [20*k,24.5,-49-360],
    [22*k,24.2,-52-360],
    [25*k,23.6,-59-360],
    [30*k,22.7,-65-360],
    [50*k,19.1,-89-360],
    [70*k,15.9,-102-360],
    [100*k,12,-121-360],
    [150*k,6.7,-140-360],
    [200*k,2.4,-146-360],
    [300*k,-4.1,-162-360],
    [500*k,-13.1,-190-360]
  # [700*k,-19,170],
   # [1*m,-24.6,90]
]
#con a0 infinito
#system = signal.lti([9.090909090909092e+03,3.952569169960475e+04,0, 0], [0.002608695652174, 4.167035573122531e+02,1.190068271649300e+05,1.132950053898671e+07,3.593244699964069e+08])

#con wp=bwp
system = signal.lti([1.923636363636364e+09,1.778109090909092e+12,7.694545454545455e+12,0, 0], [1.380000000000000e-04, 5.742843381818183e+02,8.872715376108432e+07,1.063289203597012e+11,2.556854763449125e+13,2.281747053712397e+15,6.995111272727274e+16])

#con wp=bwp/2
#system = signal.lti([4.181818181818182e+12,8.363654545454547e+18,3.636363636363637e+19,0, 0], [1.380000000000000e-04, 1.200574030418182e+06,2.592323762224625e+12,3.835101542937484e+17,1.095082464381165e+20,1.042413729256198e+22,3.305818181818183e+23])



f = logspace(0.69897,5.69897)
w = 2 * pi * f
w, mag, phase = signal.bode(system, w)

#phase = phase-360

datos_circuito = convert_map(datos_circuito )

def bode_joaco(datos,mode,spice_filename ,output_filename):
    spice_data = read_file_spice("input/spice_data/" + spice_filename)
    for i in range(len(spice_data["pha"])):
        if spice_data["f"][i] < 9:
            spice_data["pha"][i] = spice_data["pha"][i]+360
        spice_data["pha"][i] -= 360

         #   spice_data["pha"][i]-=360
    if mode == "mag":
        ax1.semilogx(spice_data["f"], spice_data["abs"], "magenta", linewidth=2.5, alpha=0.9)
    else:
        ax1.semilogx(spice_data["f"], spice_data["pha"], "magenta", linewidth=2.5, alpha=0.9)

    ### Real

    if mode == "mag":
        ax1.set_title('Diagrama de Bode (Módulo)')
        ax1.semilogx(datos["f"], datos["abs"], "cyan", linewidth=1, alpha=1)
        ax1.set_xlabel('Frecuencia (Hz)', fontsize=10)
        ax1.set_ylabel('|H(s)|db', fontsize=10)
        ax1.semilogx(f, mag,"darkblue",linewidth=1, alpha=1)

    else:
        ax1.set_title('Diagrama de Bode (Fase)')
        ax1.semilogx(datos["f"], datos["pha"], "cyan", linewidth=1, alpha=1)
        ax1.set_xlabel('Frecuencia (Hz)', fontsize=10)
        ax1.set_ylabel('Fase (grados)', fontsize=10)
        ax1.semilogx(f, phase, "darkblue",linewidth=1, alpha=1)

    blue_patch = mpatches.Patch(color='magenta', label='Simulación')
    green_patch = mpatches.Patch(color='cyan', label='Práctica')
    red_patch = mpatches.Patch(color='darkblue', label='Teórico')
    plt.legend(handles=[green_patch, blue_patch, red_patch])

    ax1.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
    plt.savefig("output/dataset1/" + output_filename, dpi=300)
    plt.cla()



bode_joaco(datos=datos_circuito,
           spice_filename="punto 5 senoide.txt",
           output_filename="magnitud.png",
           mode="mag")

bode_joaco(datos=datos_circuito,
           spice_filename="punto 5 senoide.txt",
           output_filename="phase.png",
           mode="pha")
