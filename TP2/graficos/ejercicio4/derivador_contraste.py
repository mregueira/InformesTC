from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from mpldatacursor import datacursor

def convert_map(datos):
    ans = dict()
    ans["f"] = [datos[i][0] for i in range(len(datos))]
    ans["abs"] = [datos[i][1] for i in range(len(datos))]
    ans["pha"] = [datos[i][2] for i in range(len(datos))]

    return ans

k = 10**3
m = 10**6

datos_puros = [
    [1*k , -4, -90],
    [10*k , 15.9, -91],
    [30*k , 25.7, -91],
    [40*k, 28.4, -90],
    [50*k, 30.7, -90],
    [60*k, 32.8, -90],
    [70*k, 34.7, -89],
    [80*k, 36.6, -90],
    [90*k, 38.5, -90],
    [100*k,40.7, -90],
    [110*k,42.5, -90],
    [120*k,45.1, -86],
    [130*k,48.4, -86],
    [140*k,53.2, -81],
    [150*k,61.3, -49],
    [154.8*k,64.5,0],
    [160*k,60.5, -20],
    [170*k,53.4, -15],
    [180*k,49.3,70],
    [190*k,46.7,70],
    [200*k,44.7,75],
    [300*k,35.7,77],
    [400*k,31.5,73],
    [500*k,28.8,71],
    [600*k,26.6,69],
    [m   , 20.6,63],
    [2*m , 12.8,56]
]

datos_derivador = convert_map(datos_puros)


a0 = 10**(110/20)
bwp = 15*pow(10,6)

fp = bwp / a0
wp = fp * 2 * pi


def derivador_contraste(r,c, mode,f_range,input_filename,spice_filename ,output_filename):

    fig, ax1 = plt.subplots()

    w_range = [i * (2 * pi) for i in f_range]
    RC = r*c

    k = -a0 * RC / (a0 + 1)
    w0 = sqrt(wp * (a0 + 1) / RC)
    xi = 1.0 / 2.0 * w0 * (RC * wp + 1) / (wp * (a0 + 1))


    s1 = signal.lti([k, 0], [1 / w0 ** 2, 2 * xi / w0, 1])

    w, mag, pha = signal.bode(s1, w_range)
    f = [i / 2 / pi for i in w]

    ### Teorico
    if mode=="mag":
        ax1.semilogx(f, mag, "yellow", linewidth=3)
    else:
        ax1.semilogx(f, pha, "yellow",linewidth=3)

    ### Simulado

    spice_data = read_file_spice("input/spice_data/"+spice_filename)


    for i in range(len(spice_data["pha"])):
        while spice_data["pha"][i] > 0:
            spice_data["pha"][i] -= 360
    if mode=="mag":
        ax1.semilogx(spice_data["f"], spice_data["abs"], "magenta", linewidth=1,alpha=0.9)
    else:
        ax1.semilogx(spice_data["f"], spice_data["pha"], "magenta",linewidth=1,alpha=0.9)

    ### Real
    for i in range(len(datos_derivador["pha"])):
        if datos_derivador["pha"][i] > 0:
            datos_derivador["pha"][i] -= 360

    if mode=="mag":
        ax1.semilogx(datos_derivador["f"],datos_derivador["abs"],"cyan",linewidth=1.5,alpha=1)
    else:
        ax1.semilogx(datos_derivador["f"],datos_derivador["pha"],"cyan",linewidth=1.5,alpha=1)
    ax1.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (Hz)")
    if mode=="mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")

    magenta_patch = mpatches.Patch(color='magenta', label='Simulado')
    yellow_patch = mpatches.Patch(color='yellow', label='Teorico')
    cyan_patch = mpatches.Patch(color='cyan',label='Practico')
    plt.legend(handles=[yellow_patch, magenta_patch,cyan_patch])
    if mode == "mag":
        datacursor(display='multiple', tolerance=10, formatter="Frec: {x:.3e} Hz \nAmplitud:{y:.2f} dB".format,draggable=True)
    elif mode == "pha":
        datacursor(display='multiple', tolerance=10, formatter="Frec: {x:.3e} Hz \nFase:{y:.2f} grados".format, draggable=True)

    plt.show()

    input("Press enter to continue")

    if mode == "pha":
        fig.savefig("output/contraste/" + output_filename, dpi=300)

    plt.cla()
    plt.close()

derivador_contraste(r=1800,c=56*10**(-9),
                    mode="mag",
                    f_range=np.logspace(3,7,1000),
                    input_filename="",
                    spice_filename="derivador_caso1.txt",
                    output_filename="derivador_contrasteA.png")
derivador_contraste(r=1800,c=56*10**(-9),
                    mode="pha",
                    f_range=np.logspace(3,7,1000),
                    input_filename="",
                    spice_filename="derivador_caso1.txt",
                    output_filename="derivador_contrasteA_fase.png")




