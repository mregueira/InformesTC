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
    w_all = [i * (2*pi) for i in f_all]

    print("r1 = ", r1)
    print("r2 = ", r2)
    print("r3 = ", r3)

    g_ideal = r4 * (r1 + r2) / (r1 * (r3 + r4))
    q = r1 * r2 + r2 * r3 + r1 * r3

    G_ac = r4 * (r1 + r2) / ((r3 + r4) * (r1 + (r1 + r2) / a0))

    fp = 12
    wp = 12 / 2 / pi

    fp_p = fp * a0 / (r1 + r2) * (r1 + (r1 + r2) / a0)
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

    data_spice = read_file_spice("input/Ej1_Spice/"+spice_filename)

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



    ### impedancia de entrada

    #### Teorico #####


    s1 = signal.lti([r3+r4], [1])
    w, H = signal.freqresp(s1, w_all)
    f = [i / 2 / pi for i in w]
    # axes.figure()
    ax1.semilogx(f, abs(H), 'blue', linewidth=2)

    #### Practico #####
    # print (data_excel)
    vin = data_excel["amp usada"]
    vd = data_excel["vd"]

    zin = [vin[i] * r3 / (vin[i] - vd[i]) for i in range(len(vin))]

    ax1.semilogx(data_excel["freq"], zin, 'green', linewidth=2)

    #### Simulado ####
    data_spice = read_file_spice("input/Ej1_SpiceImp/" + spice_filename)
    zin = [10 ** (data_spice["abs"][i] / 20) for i in range(len(data_spice["abs"]))]

    ax1.semilogx(data_spice["f"], zin, "red", linewidth=2)

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Impedancia (ohms)")

    blue_patch = mpatches.Patch(color='blue', label='Teorico')
    green_patch = mpatches.Patch(color='green', label='Practica')
    red_patch = mpatches.Patch(color='red', label='Simulacion')
    plt.legend(handles=[green_patch, blue_patch, red_patch])

    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.savefig("output/imp/" + output_filename)
    plt.cla()


dibujar_bode(r1=1.2*k,r2=12*k,r3=1.2*k,r4=4.99*k, # caso 10
             excel_filename="input/Ej1_Bodes/NoInversor_G8.8_OK.xlsx",
             spice_filename="NoInversor_G8.8_OK.txt",
             output_filename="NoInversor_G8.8.png",
             log_range=(3,7))

dibujar_bode(r1=1.2*k,r2=1.2*k,r3=1.2*k,r4=4.99*k, # caso 10
              excel_filename="input/Ej1_Bodes/NoInversor_G1.6_OK.xlsx",
              spice_filename="NoInversor_G1.6_OK.txt",
              output_filename="NoInversor_G1.6.png",
              log_range=(3,7))

dibujar_bode(r1=12*k,r2=1.2*k,r3=12*k,r4=49.9*k, # caso 10
              excel_filename="input/Ej1_Bodes/NoInversor_G0.88_OK.xlsx",
              spice_filename="NoInversor_G0.88_OK.txt",
              output_filename="NoInversor_G0.88.png",
              log_range=(3,7))

#plt.show()
