import transferencias
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from math import *
import datacursor_easy
from read_csv import read_csv_bode
from valores import *
from scipy import signal
import read_spice
import read_csv


f_range = np.logspace(2, 8, 10000)
w_range = [2 * pi * i for i in f_range]


def graficar_cmrr(mod, output_filename):
    fig, ax1 = plt.subplots()

    h10, h20, h30, h40 = transferencias.get_out(1/2, -1/2, r5)
    h11, h21, h31, h41 = transferencias.get_out(1,1, r5)

    s1 = signal.lti(h40[0], h40[1])
    s2 = signal.lti(h41[0], h41[1])

    w, mag, phase = signal.bode(s1, w_range)
    w2, mag2, phase2 = signal.bode(s2, w_range)

    cmrr = [mag[i] - mag2[i] for i in range(len(mag))]

    f = [i / 2 / pi for i in w]
    ax1.semilogx(f, cmrr, "green")

    datacursor_easy.add_legend_cmrr(
        my_mode=mod,
        ax=ax1,
        my_plt=plt)

    datacursor_easy.make_datacursor(
        my_mode=mod,
        filename="",
        my_plt=plt,
        my_fig=fig)



graficar_cmrr(
    mod="mag",
    output_filename="test.png")