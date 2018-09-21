from transferencias import *

from scipy import signal
import numpy as np
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from random import *

f_range = np.logspace(2, 6, 10000)
w_range = [2 * pi * i for i in f_range]

a0values = np.logspace(4.69, 5.69, 7)


def random_color():
    return '#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256))


def plot_aol(mode= "mag"):

    fig, ax1 = plt.subplots()
    patches = []

    for a0v in a0values:
        h1, h2, h3, h4 = get_out_a0_bwp(1, 1, a0v, 3*m)

        h = signal.lti(h4[0], h4[1])
        w, mag, pha = signal.bode(h, w_range)
        f = [i / 2 / pi for i in w]



        val_col = random_color()


        if mode == "mag":
            ax1.semilogx(f, mag, val_col, linewidth=1)
        elif mode == "pha":
            ax1.semilogx(f, pha, val_col, linewidth=1)

        name = str("$a_0=" + str(round(a0v))+"$")

        patches.append(mpatches.Patch(color=val_col, label=name))
    plt.legend(handles=patches)

    plt.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (Hz)")
    if mode == "mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")

    # plt.legend(handles=patches)
    plt.show()


plot_aol()