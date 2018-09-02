from read_spice import *
import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from read_xls import *
from mpldatacursor import datacursor
import matplotlib
from read_spice import *

from read_csv import *


mili = 10**(-3)
maximo = 13.5
minimo = -13.5
def generar_teorico(ganancia):

    vin = np.arange(-15.0,15.0,0.01)

    vout = []
    for i in vin:
        value = i * ganancia
        if value > maximo:
            value = maximo
        if value < minimo:
            value = minimo

        vout.append( value )

    ans = dict()
    ans["vin"] = vin
    ans["vout"] = vout
    return ans

def computar_funcion(data):
    output = dict()
    output["vin"] = []
    output["vout"] = []

    vin = dict()

    for i in range(len(data["t"])):
        vin[str(data["vin"][i])] =  data["vout"][i]

    #for i in range(len(data["t"])):
    #    vin[str(data["vin"][i])].append( )

    ans = []

    for i in vin.keys():
        #print(i)
        #sum = vin[i][0]

        ans.append( [float(i) , vin[i]  ] )

    ans.sort()
    #print(ans)

    for i in range(len(ans)):
        output["vin"].append(ans[i][0])
        output["vout"].append(ans[i][1])

    return output
def draw_time(data,output_filename):
    fig, ax1 = plt.subplots()

    ax1.plot(data["t"], data["vin"], 'blue', linewidth=2)
    ax1.plot(data["t"], data["vout"], 'green', linewidth=2)

    plt.xlabel("Tiempo (t)")
    plt.ylabel("V (v)")

    blue_patch = mpatches.Patch(color='blue', label='Vin')
    green_patch = mpatches.Patch(color='green', label='Vout')
    # red_patch = mpatches.Patch(color='red', label='Simulación')

    plt.legend(handles=[green_patch, blue_patch])
    ax1.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    datacursor(display='multiple', tolerance=10, formatter="t: {x:.3e} s \nV:{y:.1f} v".format, draggable=True)

    plt.show()
    input("Press Enter ")

    fig.savefig("output/dc_sweep/time/" + output_filename1)

    plt.cla()
    plt.close()

def graficar_dc_sweep(spice_filename,input_file ,output_filename1,output_filename2 , ganancia,minv , maxv):

    data_basic = read_csv("input/Ej1_DCSweep/"+input_file)
    data = dict()
    data["t"] = []
    data["vin"] = []
    data["vout"] = []

    for i in range(len(data_basic["t"])):
        if minv < data_basic["t"][i] < maxv:
            for j in data_basic.keys():
                data[j].append(data_basic[j][i])


    #draw_time(data,output_filename1)

    data_vo = computar_funcion(data)
    spice_data = read_spice_vin_vout("input/Ej1_SpiceDCSweep/"+spice_filename)
    teorico_data = generar_teorico(ganancia)


    fig , ax1 = plt.subplots()

    ax1.plot(data_vo["vin"],data_vo["vout"],'blue',linewidth=3)
    ax1.plot(spice_data["vin"],spice_data["vout"],"green",linewidth=3)
    ax1.plot(teorico_data["vin"],teorico_data["vout"],"magenta",linewidth=1)


    plt.xlabel("Vin (V)")
    plt.ylabel("Vout (v)")

    blue_patch = mpatches.Patch(color='blue', label='Práctica')
    green_patch = mpatches.Patch(color='green', label='Simulación')
    red_patch = mpatches.Patch(color='magenta',label='Teoría')

    #red_patch = mpatches.Patch(color='red', label='Simulación')

    plt.legend(handles=[blue_patch,green_patch,red_patch])
    ax1.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    datacursor(display='multiple', tolerance=10, formatter="Vin: {x:.1f} v \nVout:{y:.1f} v".format, draggable=True)

    plt.show()
    input("Press Enter ")

    fig.savefig("output/dc_sweep/vinvout/" + output_filename2)

    plt.cla()
    plt.close()


graficar_dc_sweep(input_file="inv_c1.csv",
                  spice_filename="Inv_c1_spice.txt",
                  minv = 4.011*mili ,
                  maxv = 4.67*mili,
                  ganancia=-10,
                  output_filename1="inv_c1.png",
                  output_filename2="inv_c1.png")



graficar_dc_sweep(input_file="inv_c2.csv",
                  spice_filename="Inv_c2_spice.txt",
                  minv = 4.008*mili ,
                  maxv = 4.657*mili,
                  ganancia=-1,
                  output_filename1="inv_c2.png",
                  output_filename2="inv_c2.png")


graficar_dc_sweep(input_file="inv_c3.csv",
                  spice_filename="Inv_c3_spice.txt",
                  minv = 4*mili,
                  maxv = 4*671*mili,
                  ganancia=-0.1,
                  output_filename1="inv_c3.png",
                  output_filename2="inv_c3.png")


graficar_dc_sweep(input_file="noinv_c1.csv",
                  spice_filename="noInv_c1_spice.txt",
                  minv = 3.996*mili,
                  maxv = 4.644*mili,
                  ganancia=8.8,
                  output_filename1="noinv_c1.png",
                  output_filename2="noinv_c1.png")


graficar_dc_sweep(input_file="noinv_c2.csv",
                  spice_filename="noInv_c2_spice.txt",
                  minv = 4*mili ,
                  maxv = 4.6*mili,
                  ganancia=1.6,
                  output_filename1="noinv_c2.png",
                  output_filename2="noinv_c2.png")


graficar_dc_sweep(input_file="noinv_c3.csv",
                  spice_filename="noInv_c3_spice.txt",
                  minv = 3.955*mili,
                  maxv = 4.668*mili,
                  ganancia=0.88,
                  output_filename1="noinv_c3.png",
                  output_filename2="noinv_c3.png")

