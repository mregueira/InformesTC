from transferencias import *

from scipy.signal import *
import numpy as np
from math import *

f_range = np.logspace(2, 8, 10000)
w_range = [2 * pi * i for i in f_range]


def plot_aol(mode= "mag"):
    h1, h2, h3, h4 = get_out_a0_bwp(1, 1, 100*k, 3*m)

    w, pha, mag = lti(h4[0], h4[1], w_range)

    fig, ax1 = plt.subplots()

    if mode == "mag":
        ax1.semilogx(f, mag, val_col, linewidth=3)
    elif mode == "pha":
        ax1.semilogx(f, pha, val_col, linewidth=3)

    plt.legend(handles=patches)
    plt.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (Hz)")
    if mode == "mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")

    plt.show()


plot_aol()