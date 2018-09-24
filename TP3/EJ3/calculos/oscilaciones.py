import read_spice
import transferencias
from scipy import signal
from math import *
from random import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import datacursor_easy

import numpy as np


data1 = read_spice.read_file_spice_time("input/spice/oscila.txt")
data2 = read_spice.read_file_spice_time("input/spice/no_oscila.txt")



def plot_oscila(filename):
    fig, ax1 = plt.subplots()
    data1["time"] = [i * 1000000 for i in data1["time"]]
    data2["time"] = [i * 1000000 for i in data2["time"]]

    ax1.plot(data1["time"], data1["vin"], color="green", linewidth=2)
    ax1.plot(data1["time"], data1["vout"], color="blue", linewidth=2)
    ax1.plot(data2["time"], data2["vout"], color="red", linewidth=2)

    patches = []

    patches.append(mpatches.Patch(color="green", label="$v_{in}$"))
    patches.append(mpatches.Patch(color="blue", label="$v_{out}, R_5=5k$"))
    patches.append(mpatches.Patch(color="red", label="$v_{out}, R_5=8k$"))


    plt.legend(handles=patches)
    plt.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.ylabel("$Tensión (v)$")
    plt.xlabel("$Tiempo \; ( \mu s)$")

    fig.savefig("output/"+filename, dpi=300)
    plt.show()
    plt.cla()
    plt.close()


plot_oscila(filename = "oscilaciones_simuladas.png")