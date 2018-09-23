import valores
import transferencias
from scipy import signal
from math import *
from random import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import read_csv

fig, ax1 = plt.subplots()


def random_color():
    return '#%02x%02x%02x' % (randrange(256),randrange(256),randrange(256))

patches = []

def plot_bode(file , name):
    data = read_csv.read_csv_bode(file)
    col = random_color()
    plt.semilogx(data["freq"], data["amp"], col)

    patches.append(mpatches.Patch(color=col, label=name))

    #plt.legend(handles=patches)


    plt.xlabel("Frecuencia (hz)")
    plt.ylabel("Amplitud (dB)")

    #plt.show()


plot_bode("input\mediciones\output\comun\comun_02.csv", "r5=10k")
plot_bode("input\mediciones\output\comun\comun_12k.csv", "r5=12k")
plot_bode("input\mediciones\output\comun\comun_21k.csv", "r5=21k")
plot_bode("input\mediciones\output\comun\comun_53k.csv", "r5=53k")
plot_bode("input\mediciones\output\comun\comun_78k.csv", "r5=78k")


plt.minorticks_on()
ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
plt.legend(handles=patches)

plt.show()
