import sympy as sp
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import read_spice
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import transferencias
import read_csv


k = 10 ** 3
m = 10 ** 6

f_range = np.logspace(2, 8, 10000)
w_range = [2 * pi * i for i in f_range]


def add_legend(mode, ax, l1, l2, l3):
    blue_patch = mpatches.Patch(color='blue', label=l1)
    red_patch = mpatches.Patch(color='red', label=l2)
    green_patch = mpatches.Patch(color='green', label=l3)

    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (Hz)")
    if mode == "mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")

    plt.legend(handles=[green_patch, blue_patch, red_patch])


def graficar_op_amp4(v1, v2, mode, spice_filename, medido_filename):
    fig, ax1 = plt.subplots()

    h1, h2, h3, h4 = transferencias.get_out(v1, v2)

    s1 = signal.lti(h4[0], h4[1])

    h = dict()
    w, h["mag"], h["pha"] = signal.bode(s1, w_range)
    f = [i / 2 / pi for i in w]

    #data_spice = read_spice.read_file_spice(spice_filename)

    data_medido = read_csv.read_csv_bode(medido_filename)

    for i in range(len(data_medido["pha"])):
        if data_medido["pha"][i] < 0.0:
            data_medido["pha"][i] += 360.0

    ax1.semilogx(f, h[mode],  "blue", linewidth=4)

    #if mode == "mag":
    #    ax1.semilogx(data_spice["f"], data_spice["abs"], "red")
    #else:
    #    ax1.semilogx(data_spice["f"], data_spice["pha"], "red")
    if mode == "mag":
        ax1.semilogx(data_medido["freq"], data_medido["amp"], "green")
    else:
        ax1.semilogx(data_medido["freq"], data_medido["pha"], "green")

    add_legend(mode, ax=ax1, l1="Teórico", l2="Simulado", l3="Medido")

    plt.show()

    plt.cla()
    plt.close()


# graficar_op_amp4(v1=1,
#                  v2=1,
#                  mode="mag",
#                  spice_filename="input/spice/modo_comun_TL084.txt",
#                  medido_filename="input/mediciones/output/mode_comun_02.csv")
#
#
# graficar_op_amp4(v1=1,
#                  v2=1,
#                  mode="pha",
#                  spice_filename="input/spice/modo_comun_TL084.txt",
#                  medido_filename="input/mediciones/output/mode_comun_02.csv")
#

graficar_op_amp4(v1=1,
                 v2=0,
                 mode="mag",
                 spice_filename="input/spice/modo_comun_TL084.txt",
                 medido_filename="input/mediciones/output/mixtov2.csv")


graficar_op_amp4(v1=1,
                 v2=0,
                 mode="pha",
                 spice_filename="",
                 medido_filename="input/mediciones/output/mixtov2.csv")
