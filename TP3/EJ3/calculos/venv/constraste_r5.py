import valores
import transferencias
from scipy import signal
from math import *
from random import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import numpy as np

r5_values = np.logspace(3, 6, 10)
f_range = np.logspace(2, 8, 10000)
w_range = [2 * pi * i for i in f_range]


def random_color():
    return '#%02x%02x%02x' % (randrange(256),randrange(256),randrange(256))


def plot_constraste_r5(mode, filename):

    fig, ax1 = plt.subplots()

    patches = []
    for r5v in r5_values:

        h1, h2, h3, h4 = transferencias.get_out(1, 1, r5v)

        H = signal.lti(h4[0], h4[1])
        w, mag, pha = signal.bode(H, w_range)
        f = [i / 2 / pi for i in w]
        val_col = random_color()

        if mode == "mag":
            ax1.semilogx(f, mag, val_col, linewidth=3)
        elif mode == "pha":
            ax1.semilogx(f, pha, val_col, linewidth=3)

        name = str("r5=" + str(round(r5v)) + " ohm")

        patches.append(mpatches.Patch(color=val_col, label=name))

    plt.legend(handles=patches)
    plt.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (hz)")
    plt.ylabel("Amplitud (dB)")

    plt.show()


plot_constraste_r5(mode="mag", filename="test_file")

