from valores import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import signal

import transferencias


f_range = np.logspace(2, 8, 10000)
w_range = [2 * pi * i for i in f_range]

tol = 0.02

#r3,r4,r6,r7
total_it = 5


def plot_tolerancia(mode, v1, v2, filename, iteraciones):
    print("Calculando ", filename)

    fig, ax1 = plt.subplots()
    for it1 in range(iteraciones):
        print(it1)
        for it2 in range(iteraciones):
            for it3 in range(iteraciones):
                for it4 in range(iteraciones):
                    r3v = (r3-r3*tol) + 2*r3*tol*(it1/total_it)
                    r4v = (r4 - r4 * tol) + 2 * r4 * tol * (it2 / total_it)
                    r6v = (r6 - r6 * tol) + 2 * r6 * tol * (it3 / total_it)
                    r7v = (r7 - r7 * tol) + 2 * r7 * tol * (it4 / total_it)

                    h1, h2, h3, h4 = transferencias.get_out_rs(r3v, r4v, r6v, r7v, v1 ,v2)
                    H = signal.lti(h4[0], h4[1])
                    w, mag, pha = signal.bode(H, w_range)
                    f = [i / 2 / pi for i in w]
                    if mode == "mag":
                        ax1.semilogx(f, mag, "cyan", linewidth=0.1, alpha=0.5)
                    else:
                        ax1.semilogx(f, pha, "cyan", linewidth=0.1, alpha=0.5)

    patch1 = mpatches.Patch(color="cyan", label="Desviaciones")
    patch2 = mpatches.Patch(color="blue", label="Teórico")

    plt.legend(handles=[patch1,patch2])

    h1, h2, h3, h4 = transferencias.get_out_rs(r3, r4, r6, r7, v1, v2)
    H = signal.lti(h4[0], h4[1])
    w, mag, pha = signal.bode(H, w_range)
    f = [i / 2 / pi for i in w]
    if mode == "mag":
        ax1.semilogx(f, mag, "blue", linewidth=1, alpha=1)
    else:
        ax1.semilogx(f, pha, "blue", linewidth=1, alpha=1)


    plt.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
    plt.xlabel("Frecuencia (hz)")
    if mode == "mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")

    plt.savefig("output/" + filename, dpi=300)
    plt.cla()
    plt.close()


plot_tolerancia("mag", 1, 1, filename="asimetria_comun_mag.png", iteraciones=6)
plot_tolerancia("pha", 1, 1, filename="asimetria_comun_pha.png", iteraciones=6)

plot_tolerancia("mag", 1/2, -1/2, filename="asimetria_dif_mag.png", iteraciones=6)
plot_tolerancia("pha", 1/2, -1/2, filename="asimetria_dif_pha.png", iteraciones=6)