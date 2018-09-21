import valores
import transferencias
from scipy import signal
from math import *
from random import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import read_csv


def plot_bode(file):
    data = read_csv.read_csv(file)


    fig, ax1 = plt.subplots()



    plt.legend(handles=patches)
    plt.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (hz)")
    plt.ylabel("Amplitud (dB)")

    #plt.show()

plot_bode("")
plot_bode()




