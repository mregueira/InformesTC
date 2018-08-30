from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def convert_map(datos):
    ans = dict()
    ans["f"] = [datos[i][0] for i in range(len(datos))]
    ans["abs"] = [datos[i][2] / sqrt(2) / (datos[i][1] * 56 * (10**(-9)) * (datos[i][0]*2*pi ) ) for i in range(len(datos))]

    return ans
def convert_map_int(datos):
    ans = dict()
    ans["f"] = [datos[i][0] for i in range(len(datos))]
    ans["abs"] = [ 1800*datos[i][1]/datos[i][2]  for i in range(len(datos))]

    return ans
k = 10**3
mili = 10**(-3)
a0 = 10**(110/20)
bwp = 15*pow(10,6)

fp = bwp / a0
wp = fp * 2 * pi

fig, ax1 = plt.subplots()

datos = [
    [1*k ,352*mili,0.5],
    [2*k, 352.8*mili,0.5],
    [5*k, 351*mili,0.5],
    [10*k,346*mili,0.5],
    [15*k, 342.3*mili,0.5],
    [20*k, 335.4*mili,0.5],
    [30*k, 317.7*mili,0.5],
    [50*k, 276*mili,0.5],
    [80*k, 20*mili,0.05],
    [100*k, 17*mili,0.05],
    [120*k, 13*mili, 0.05 ],
    [200*k, 15*mili, 0.05],
    [400*k, 4*mili, 0.05],
    [500*k, 3*mili, 0.05],
    [800*k, 1.9*mili, 0.05],
    [1000*k, 2*mili, 0.05]


]


datos_integrador = [
    [30  ,48.2,50.5,98.5],
    [50,48.2,50.4,98.5],
    [70,48.2,50.5,98.6],
    [100 , 49 , 50 , 99],
    [120, 48.2,50.5,98.4],
    [150,48.4,50.5,98.5],
    [200,47.9,50.5,98.4],
    [500,48.6,51,98],
    [700,48.6,50,6,98.1],
    [1*k,49.9,52,98.6],
    [2*k,149,148,297],
    [5*k,152,152,299],
    [10*k,152.8,152.6,298]
]

datos_derivador = convert_map(datos)
datos_integrador = convert_map_int(datos_integrador)

def graficar_imp(mode,f_range,datos_medidos,spice_filename ,output_filename,data):
    w_range = [i * (2 * pi) for i in f_range]

    num = data[0]
    den = data[1]

    s1 = signal.lti(num,den)

    w, H = signal.freqresp(s1, w_range)

    f = [i / 2 / pi for i in w]

    if mode=="mag":
        ax1.semilogx(f, abs(H), "blue", linewidth=0.5)
    else:
        pass
        #ax1.semilogx(f, a, "blue",linewidth=2)
    print(datos_medidos["abs"])
    if mode == "mag":
        ax1.semilogx(datos_medidos["f"], datos_medidos["abs"], "cyan", linewidth=2)
    else:
        ax1.semilogx(datos_medidos["f"], datos_medidos["pha"], "cyan", linewidth=2)



    spice_data = read_file_spice("input/spice_data/"+spice_filename)

    for i in range(len(spice_data["abs"])):
        spice_data["abs"][i] = 10**(spice_data["abs"][i]/20.0)
    if mode=="mag":
        ax1.semilogx(spice_data["f"],spice_data["abs"],"green",linewidth=0.5)
    else:
        ax1.semilogx(spice_data["f"],spice_data["pha"],"green",linewidth=0.5)



    ax1.minorticks_on()
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')

    blue_patch = mpatches.Patch(color='blue', label='teoria')
    green_patch = mpatches.Patch(color='green', label='simulacion')

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Impedancia (ohms)")

    plt.legend(handles=[green_patch, blue_patch])
    plt.savefig("output/contraste/" + output_filename, dpi=300)
    plt.cla()

r=1800
c=56*(10**(-9))

graficar_imp(data=[[-c*r, -2*c*r*wp - 1, a0*wp - c*r*wp**2 - 2*wp, a0*wp**2 - wp**2],
                   [c, a0*c*wp + 2*c*wp, a0*c*wp**2 + c*wp**2, 0]],
                    datos_medidos=datos_derivador,
                     f_range= np.logspace(3,9,10000),
                     mode="mag",
                     spice_filename="derivador_caso1imp.txt",
                     output_filename="derivador_impA.png")

graficar_imp(data=[[-c*r, a0*c*r*wp - 2*c*r*wp - 1, a0*c*r*wp**2 - c*r*wp**2 - 2*wp, -wp**2],
                   [c, a0*c*wp + 2*c*wp, a0*c*wp**2 + c*wp**2, 0]],
                     datos_medidos=datos_integrador,
                     f_range=np.logspace(1.3, 4, 10000),
                     mode="mag",
                     spice_filename="integrador_caso1imp.txt",
                     output_filename="integrador_impA.png")

