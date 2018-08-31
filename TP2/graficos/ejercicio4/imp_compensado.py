from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


k = 10**3
m = 10**6

mili = 10**(-3)
a0 = 10**(110/20)
bwp = 15*pow(10,6)

fp = bwp / a0
wp = fp * 2 * pi

fig, ax1 = plt.subplots()


def convert_map_der(datos):
    ans = dict()
    ans["f"] = [datos[i][0] for i in range(len(datos))]
    ans["abs"] = [ datos[i][2] /  (datos[i][1]  / 33.0) for i in range(len(datos))]

    return ans
def convert_map_int(datos):
    ans = dict()
    ans["f"] = [datos[i][0] for i in range(len(datos))]
    ans["abs"] = [ 1800*datos[i][1]/datos[i][2]  for i in range(len(datos))]

    return ans



datos_derivador = [
    [1*k , 9*mili,423.8*mili],
    [2*k , 12.3*mili,424.0*mili],
    [3*k, 18.35*mili,423.2*mili],
    [4*k, 20.96*mili,422.1*mili],
    [5*k, 25.50*mili,420.6*mili],
    [6*k, 30.02*mili,418.8*mili],
    [7*k, 34.53*mili,417*mili],
    [8*k, 38.97*mili,410.7*mili],
    [9*k, 43.38*mili,412.4*mili],
    [10*k,47.71*mili,409.6*mili],
    [15*k,67.9*mili,393.5*mili],
    [20*k,85.6*mili,374.7*mili],
    [30*k,112.6*mili,334.6*mili],
    [40*k,130.8*mili,297.2*mili],
    [50*k,142.8*mili,265.8*mili],
    [60*k,151.3*mili,240.6*mili],
    [80*k,161.8*mili,202.9*mili],
    [100*k,55.15*mili,61.0*mili],
    [150*k,26.83*mili,27.24*mili],
    [200*k,30.34*mili,28.32*mili],
    [300*k,54.27*mili,34.74*mili],
    [400*k,37.80*mili,21.07*mili],
    [500*k,48.9*mili,25.88*mili],
    [600*k,58.33*mili,29.35*mili],
    [700*k,64.7*mili,32.36*mili],
    [800*k,60.89*mili,32.22*mili],
    [1*m,73.8*mili,36.1*mili],
    [1.5*m,71.7*mili,36.04*mili],
    [2*m,68.9*mili,34.9*mili],
    [3*m,61.3*mili,31.8*mili],
    [5*m,23*mili,12*mili]
]
datos_derivador = convert_map_der(datos_derivador)

datos_integrador = [
    [50,173.8*mili,178.7*mili],
    [100,174.6*mili,176.7*mili],
    [200,174.4*mili, 176.1*mili],
    [500,174.2*mili, 175.5*mili],
    [800,174.4*mili, 175.8*mili],
    [1*k,173.8*mili,176.4*mili],
    [2*k,174*mili,176.7*mili],
    [3*k,174*mili,176.7*mili],
    [4*k,174.8*mili,176.2*mili],
    [5*k,174.8*mili,176.2*mili],
    [7*k,174.8*mili,176.4*mili],
    [10*k,174.8*mili,176.1*mili],
    [20*k,174.8*mili,176*mili],
    [40*k,175*mili,176.3*mili],
    [70*k,175.2*mili,177*mili],
    [100*k,175.2*mili,177.9*mili],
    [150*k,174.8*mili,179.8*mili],
    [200*k,174.1*mili,182*mili],
    [300*k,172*mili,188*mili]
]

#
#    [700*k,156.1*mili,221.5*mili],
#    [m,141*mili,245.6*mili],
#    [2*m,97.8*mili,287.2*mili],
#    [5*m,42*mili,272.4*mili],
#    [10*m,18*mili,204.8*mili],
#    [20*m,6.8*mili,141*mili]
datos_integrador = convert_map_int(datos_integrador)



def graficar_imp(mode,f_range,datos_medidos,spice_filename ,output_filename,data):
    w_range = [i * (2 * pi) for i in f_range]
    num = data[0]
    den = data[1]

    s1 = signal.lti(num, den)

    w, H = signal.freqresp(s1, w_range)

    f = [i / 2 / pi for i in w]
    Ha = [abs(i) for i in H]

    if mode=="mag":
        ax1.semilogx(f, abs(H), "yellow", linewidth=3)
    else:
        pass

    if mode == "mag":
        ax1.semilogx(datos_medidos["f"], datos_medidos["abs"], "cyan", linewidth=2)
    else:
        pass
        #ax1.semilogx(datos_medidos["f"], datos_medidos["pha"], "cyan", linewidth=2)



    spice_data = read_file_spice("input/spice_data/" + spice_filename)

    for i in range(len(spice_data["abs"])):
        spice_data["abs"][i] = 10**(spice_data["abs"][i]/20.0)

    if mode == "mag":
        ax1.semilogx(spice_data["f"], spice_data["abs"], "magenta", linewidth=1, alpha=0.9)
    else:
        ax1.semilogx(spice_data["f"], spice_data["pha"], "magenta", linewidth=1, alpha=0.9)


    ax1.minorticks_on()
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')

    blue_patch = mpatches.Patch(color='yellow', label='Teoria')
    green_patch = mpatches.Patch(color='magenta', label='Simulacion')
    medido_patch = mpatches.Patch(color='cyan',label='Experimental')

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Impedancia (ohms)")

    plt.legend(handles=[green_patch, blue_patch,medido_patch])

    plt.savefig("output/contraste/" + output_filename, dpi=300)
    plt.cla()

r = 1800
c = 56 * (10**(-9))
r2 = 33
graficar_imp(
    mode="mag",
    data=[[-c*r - 2*c*r2, a0*c*r2*wp - 2*c*r*wp - 4*c*r2*wp - 1, a0*c*r2*wp**2 + a0*wp - c*r*wp**2 - 2*c*r2*wp**2 - 2*wp, a0*wp**2 - wp**2], [c, a0*c*wp + 2*c*wp, a0*c*wp**2 + c*wp**2, 0]],
    f_range=np.logspace(3,7,1000),
    datos_medidos=datos_derivador,
    spice_filename="derivador_caso2imp.txt",
    output_filename="derivador_imp_compensado.png"
)


r = 1800
c = 56 * (10**(-9))
r2 = 82*k
graficar_imp(
    mode="mag",
    data=[[-c**2*r*r2, a0*c**2*r*r2*wp - 2*c**2*r*r2*wp - c*r - c*r2, a0*c**2*r*r2*wp**2 + a0*c*r*wp - c**2*r*r2*wp**2 - 2*c*r*wp - 2*c*r2*wp, a0*c*r*wp**2 - c*r*wp**2 - c*r2*wp**2, 0], [c**2*r2, a0*c**2*r2*wp + 2*c**2*r2*wp + c, a0*c**2*r2*wp**2 + a0*c*wp + c**2*r2*wp**2 + 2*c*wp, a0*c*wp**2 + c*wp**2, 0]],
    f_range=np.logspace(2,7,1000),
    datos_medidos=datos_integrador,
    spice_filename="integrador_caso2imp.txt",
    output_filename="integrador_imp_compensado.png"
)