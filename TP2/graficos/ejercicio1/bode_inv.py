from read_spice import *
import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from read_xls import *

a0 = 1e5

fp = 12
wp = fp * 2 * pi
fig, ax1 = plt.subplots()
k = 1e3

def dibujar_bode(r1,r2,r3,r4,log_range, excel_filename, spice_filename ,output_filename):
    (s,e) = log_range
    f_all = 10.0 ** np.arange(s, e, 0.01)
    w_all = [i * (2 * pi) for i in f_all]

    print("r1 = ", r1)
    print("r2 = ", r2)
    print("r3 = ", r3)

    g_ideal = -r2 / r1
    q = r1 * r2 + r2 * r3 + r1 * r3
    G_ac = -a0 * r2 * r3 / (q + a0 * r1 * r3)

    fp_p = fp * (1 + r1 * r3 * a0 / q)
    wp_p = fp_p * 2 * pi

    s1 = signal.lti([G_ac], [1/wp_p ,1])

    w, mag, phase = signal.bode(s1, w_all)

    f = [i / 2 / pi for i in w]

    data_excel = read_excel_data(excel_filename)


    ### Amplitud

    ax1.semilogx(f, mag, "blue", linewidth=2)
    #print (data_excel["freq"])
    #print (data_excel["Gain"])

    ax1.semilogx(data_excel["freq"], data_excel["ratio"], "green", linewidth=2)

    data_spice = read_file_spice(spice_filename)

    ax1.semilogx(data_spice["f"],data_spice["abs"],"red",linewidth=2)

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud (dB)")

    blue_patch = mpatches.Patch(color='blue', label='Teorico')
    green_patch = mpatches.Patch(color='green', label='Practica')
    red_patch = mpatches.Patch(color='red',label='Simulacion')

    plt.legend(handles=[ green_patch, blue_patch , red_patch])
    ax1.set_axisbelow(True)
    ax1.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.savefig("output/amp/"+output_filename)
    plt.cla()

    ### fase
    ax1.semilogx(f, phase, "blue", linewidth=2)
    ax1.semilogx(data_excel["freq"],data_excel["phase"],"green",linewidth=2)
    ax1.semilogx(data_spice["f"],data_spice["pha"],"red",linewidth=2)

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Fase (grados)")

    blue_patch = mpatches.Patch(color='blue', label='Teorico')
    green_patch = mpatches.Patch(color='green', label='Practica')
    red_patch = mpatches.Patch(color='red', label='Simulacion')

    plt.legend(handles=[green_patch, blue_patch, red_patch])
    ax1.set_axisbelow(True)
    ax1.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.savefig("output/pha/"+output_filename)
    plt.cla()


dibujar_bode(r1=1.2*k,r2=12*k,r3=1.2*k,r4=4.99*k, # caso 10
             excel_filename="input/Ej1_Bodes/Inversor_G10_OK.xlsx",
             spice_filename="input/Ej1_Spice/Inversor_G10_OK.txt",
             output_filename="Inversor_G10.png",
             log_range=(2,7))

dibujar_bode(r1=1.2*k,r2=1.2*k,r3=1.2*k,r4=4.99*k, # caso 10
             excel_filename="input/Ej1_Bodes/Inversor_G1_OK.xlsx",
             spice_filename="input/Ej1_Spice/Inversor_G1_OK.txt",
             output_filename="Inversor_G1.png",
             log_range=(3,7))

dibujar_bode(r1=12*k,r2=1.2*k,r3=12*k,r4=49.9*k, # caso 10
             excel_filename="input/Ej1_Bodes/Inversor_G0.1_OK.xlsx",
             spice_filename="input/Ej1_Spice/Inversor_G0.1_OK.txt",
             output_filename="Inversor_G0.1.png",
             log_range=(4,7))

#plt.show()