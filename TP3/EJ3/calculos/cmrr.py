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


    s1 = transferencias.get_out(1/2, -1/2, value.)
    s2 = transferencias.get_out(1/2, -1/2, value.)

    w, mag, phase = signal.bode(s1, w_range)
    w2, mag2, phase2 = signal.bode(s2, w_range)


    datacursor_easy.make_datacursor(
        my_mode=mod,
        filename="",
        my_plt=plt,
        my_fig=fig)



