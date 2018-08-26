from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



a0 = 10**(110/20)
bwp = 15*pow(10,6)

fp = bwp / a0
wp = fp * 2 * pi

fig, ax1 = plt.subplots()

def derivador_contraste(r,c, mode,f_range,input_filename,spice_filename ,output_filename):
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
        ax1.semilogx(f, mag, "green", linewidth=2)
    else:
        ax1.semilogx(f, pha, "green",linewidth=2)

    ### Simulado

    spice_data = read_file_spice("input/spice_data/"+spice_filename)


    for i in range(len(spice_data["pha"])):
        if spice_data["pha"][i] > 0:
            spice_data["pha"][i] -= 360
    if mode=="mag":
        ax1.semilogx(spice_data["f"], spice_data["abs"], "magenta", linewidth=1,alpha=0.9)
    else:
        ax1.semilogx(spice_data["f"], spice_data["pha"], "magenta",linewidth=1,alpha=0.9)


    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (Hz)")
    if mode=="mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")

    magenta_patch = mpatches.Patch(color='magenta', label='simulado')
    green_patch = mpatches.Patch(color='green', label='teorico')

    plt.legend(handles=[green_patch, magenta_patch])
    plt.savefig("output/contraste/" + output_filename, dpi=300)
    plt.cla()


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




