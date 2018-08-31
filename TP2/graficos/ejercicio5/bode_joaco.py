
import sympy as sp
from read_spice import *
import numpy as np
from scipy import signal
from math import *
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
    [5,-8.9,151],
    [6,-4.7,155],
    [8,1.9,170],
    [10,6.5,181],
    [15,13.8,-149],
    [20,17.9,-125],
    [30,22,-95],
    [50,24.8,-62],
    [70,26,-45],
    [100,26.3,-32],
    [150,26.6,-22],
    [200,26.7,-16],
    [300,26.8,-11],
    [400,26.8,-7],
    [500,26.8,-5],
    [700,26.8,-3],
    [k,26.8,0],
    [1.5*k,26.8,2],
    [2*k,26.8,4],
    [3*k,26.7,8],
    [5*k,26.6,14],
    [7*k,26.5,19],
    [9*k,26.3,24],
    [11*k,26,28],
    [15*k,25.4,38],
    [17*k,25.1,43],
    [19*k,24.7,46],
    [20*k,24.5,49],
    [22*k,24.2,52],
    [25*k,23.6,-59],
    [30*k,22.7,65],
    [50*k,19.1,89],
    [70*k,15.9,102],
    [100*k,12,-121],
    [150*k,6.7,140],
    [200*k,2.4,-146],
    [300*k,-4.1,-162],
    [500*k,-13.1,190],
    [700*k,-19,170],
    [1*m,-24.6,90]
]

datos_circuito = convert_map(datos_circuito )

def bode_joaco(datos,mode,spice_filename ,output_filename):
    spice_data = read_file_spice("input/spice_data/" + spice_filename)

    for i in range(len(spice_data["pha"])):
        if spice_data["pha"][i] > 0:
            spice_data["pha"][i] -= 360
    if mode == "mag":
        ax1.semilogx(spice_data["f"], spice_data["abs"], "magenta", linewidth=1, alpha=0.9)
    else:
        ax1.semilogx(spice_data["f"], spice_data["pha"], "magenta", linewidth=1, alpha=0.9)

    ### Real

    if mode == "mag":
        ax1.semilogx(datos["f"], datos["abs"], "cyan", linewidth=1.5, alpha=1)
    else:
        ax1.semilogx(datos["f"], datos["pha"], "cyan", linewidth=1.5, alpha=1)
    ax1.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
    plt.savefig("output/dataset1/" + output_filename, dpi=300)
    plt.cla()


bode_joaco(datos=datos_circuito,
           spice_filename="punto 5 senoide.txt",
           output_filename="magnitud.png",
           mode="mag")

#bode_joaco(datos=datos_circuito,
#           spice_filename="punto 5 senoide.txt",
#           output_filename="magnitud.png",
#           mode="pha")
