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


data1 = read_csv.read_csv_bode("input/mediciones/output/comun/comun_12k.csv")
data2 = read_csv.read_csv_bode("input/mediciones/output/comun_02.csv")


def plot_contraste_aislacion(mode, filename):
    fig, ax1 = plt.subplots()

    ax1.semilogx(data1["freq"], data1[mode], "green")
    ax1.semilogx(data2["freq"], data2[mode], "blue")

    patches = []

    patches.append(mpatches.Patch(color="green", label="antes de cambiar las resistencias"))
    patches.append(mpatches.Patch(color="blue", label="luego de cambiar las resistencias"))

    plt.legend(handles=patches)
    plt.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
    plt.xlabel("Frecuencia (hz)")
    if mode == "mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")


    datacursor_easy.make_datacursor(mode, "output/" + filename, plt, fig)


plot_contraste_aislacion("amp", filename="constraste_ajuste_amp.png")
plot_contraste_aislacion("pha", filename="constraste_ajuste_pha.png")

