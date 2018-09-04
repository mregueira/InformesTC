from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


SR = 0.3 * (10**6)

fig, ax1 = plt.subplots()

def plot_SR( frec_range , output_filename):


    out = [SR / (i*2*pi) for i in frec_range]

    ax1.minorticks_on()
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud máxima (V)")

    ax1.semilogx( frec_range , out , "green" )

    fig.savefig("output/teoricos/" + output_filename, dpi=300)

    plt.show()

plot_SR( frec_range= np.logspace(5,8,10000) ,output_filename="slew_rate2.png")