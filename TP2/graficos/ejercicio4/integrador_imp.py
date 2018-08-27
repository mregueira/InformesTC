from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

f_range = np.logspace(3,12,10000)
a0 = 10**(110/20)
bwp = 15*pow(10,6)

fp = bwp / a0
wp = fp * 2 * pi

fig, ax1 = plt.subplots()


def derivador_impedancia(r,c, mode,input_filename,spice_filename ,output_filename , data_func):
    w_range = [i * (2 * pi) for i in f_range]

    data = [[-c*r, -2*c*r*wp - 1, a0*wp - c*r*wp**2 - 2*wp, a0*wp**2 - wp**2], [c, a0*c*wp + 2*c*wp, a0*c*wp**2 + c*wp**2, 0]]
    num = data[0]
    den = data[1]

    s1 = signal.lti(num,den)

    w, H = signal.freqresp(s1, w_range)

    f = [i / 2 / pi for i in w]

    if mode=="mag":
        ax1.semilogx(f, abs(H), "blue", linewidth=2)
    else:
        pass
        #ax1.semilogx(f, a, "blue",linewidth=2)

    spice_data = read_file_spice("input/spice_data/"+spice_filename)

    for i in range(len(spice_data["abs"])):
        spice_data["abs"][i] = 10**(spice_data["abs"][i]/20.0)
    if mode=="mag":
        ax1.semilogx(spice_data["f"],spice_data["abs"],"green",linewidth=2)
    else:
        ax1.semilogx(spice_data["f"],spice_data["pha"],"green",linewidth=2)

    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    blue_patch = mpatches.Patch(color='blue', label='teoria')
    green_patch = mpatches.Patch(color='green', label='simulacion')

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Impedancia (ohms)")

    plt.legend(handles=[green_patch, blue_patch])
    plt.savefig("output/teoricos/" + output_filename, dpi=300)
    plt.cla()


derivador_impedancia(r=1800,c=56*(10**(-9)),
                     mode="mag",
                     input_filename="",
                     spice_filename="derivador_caso1imp.txt",
                     output_filename="derivador_impA.png")

