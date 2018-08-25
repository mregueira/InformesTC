from read_spice import *
import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

a0 = 1e5
w_all = 10.0**np.arange(3, 9, 0.01)
fp = 12
wp = fp * 2 * pi
fig, ax1 = plt.subplots()
k = 1e3

def dibujar_bode(r1,r2,r3,r4, spice_filename ,output_filename):
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

    ax1.semilogx(f, mag, "blue", linewidth="2")

    data_spice = read_file_spice("input/EJ_1_simulaciones.txt")

    ax1.semilogx(data_spice["f"],data_spice["abs"],"green",linewidth="2")

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud (dB)")

    blue_patch = mpatches.Patch(color='blue', label='Teorico')
    green_patch = mpatches.Patch(color='green', label='Simulado')
    plt.legend(handles=[ green_patch, blue_patch])


dibujar_bode(r1=1.2*k,r2=12*k,r3=1.2*k,r4=4.99*k,spice_filename="input/EJ_1_simulaciones.txt",output_filename="output11.txt")


plt.show()
