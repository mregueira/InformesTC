from read_csv import *

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def armar_grafico_muestras(dir , output_filename):
    fig , ax1 = plt.subplots()
    data = read_csv("input/muestras/"+dir)

    ax1.plot(data["t"],data["vin"] , color='red')
    ax1.plot(data["t"],data["vout"], color='blue')

    red_patch = mpatches.Patch(color='red', label='In')
    green_patch = mpatches.Patch(color='blue', label='Out')

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Tensión (v)")

    plt.legend(handles=[red_patch, green_patch])


    ax1.minorticks_on()
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')

    fig.savefig("output/muestras/" + output_filename, dpi=300)
    plt.cla()

armar_grafico_muestras(dir="int01.csv",
                       output_filename="out01.png")

armar_grafico_muestras(dir="int04.csv",
                       output_filename="out02.png")

armar_grafico_muestras(dir="int05.csv",
                       output_filename="out03.png")

armar_grafico_muestras(dir="int09.csv",
                       output_filename="out04.png")

armar_grafico_muestras(dir="int10.csv",
                       output_filename="out05.png")

armar_grafico_muestras(dir="int11.csv",
                       output_filename="out06.png")