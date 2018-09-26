import valores
import transferencias
from scipy import signal
from math import *
from random import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import datacursor_easy

import numpy as np
import read_csv


data1 = read_csv.read_csv_bode("input/mediciones/output/aislacion.csv")
data2 = read_csv.read_csv_bode("input/mediciones/output/mixtov2.csv")


def plot_contraste_aislacion(mode, filename):
    fig, ax1 = plt.subplots()

    ax1.semilogx(data1["freq"], data1[mode], "green")
    ax1.semilogx(data2["freq"], data2[mode], "blue")

    patches = []

    patches.append(mpatches.Patch(color="green", label="con aislación"))
    patches.append(mpatches.Patch(color="blue", label="sin aislación"))

    plt.legend(handles=patches)
    plt.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (hz)")
    if mode == "mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")



    datacursor_easy.make_datacursor("mag" , "output/" + filename, plt, fig)


plot_contraste_aislacion("amp", "constraste_aislacion_amp.png")
plot_contraste_aislacion("pha", "constraste_aislacion_pha.png")