from valores import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import signal
import datacursor_easy

import transferencias


f_range = np.logspace(2, 8, 10000)
w_range = [2 * pi * i for i in f_range]

tol = 0.5


def plot_tolerancia(mode, v1, v2, filename, iteraciones):
    print("Calculando ", filename)

    fig, ax1 = plt.subplots()

    for it1 in range(iteraciones):
        print(it1)
        for it2 in range(iteraciones):
            wp1 = wp - wp * tol + 2 * wp * tol * (it1/iteraciones)
            wp2 = wp - wp * tol + 2 * wp * tol * (it2/iteraciones)

            h = transferencias.get_out_wp(v1, v2, wp1, wp2)

            H = signal.lti(h[0], h[1])

            w, mag, pha = signal.bode(H, w_range)
            f = [i / 2 / pi for i in w]
            if mode == "mag":
                ax1.semilogx(f, mag, "cyan", linewidth=0.2, alpha=0.9)
            else:
                ax1.semilogx(f, pha, "cyan", linewidth=0.2, alpha=0.9)

    patch1 = mpatches.Patch(color="cyan", label="Desviaciones")
    patch2 = mpatches.Patch(color="blue", label="Teórico")

    plt.legend(handles=[patch1, patch2])

    h = transferencias.get_out_wp(v1, v2)
    H = signal.lti(h[0], h[1])

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


    datacursor_easy.make_datacursor(mode, "output/" + filename, plt, fig)

plot_tolerancia("mag", 1, 1, filename="asimetria_wp_comun_mag.png", iteraciones=12)
plot_tolerancia("pha", 1, 1, filename="asimetria_wp_comun_pha.png", iteraciones=12)

plot_tolerancia("mag", 1 / 2, -1 / 2, filename="asimetria_wp_dif_mag.png", iteraciones=12)
plot_tolerancia("pha", 1 / 2, -1 / 2, filename="asimetria_wp_dif_pha.png", iteraciones=12)