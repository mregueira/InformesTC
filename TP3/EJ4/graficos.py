import valores
import transferencias
from scipy import signal
from math import *
from random import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import datacursor_easy
import read_spice
import numpy as np
import read_csv
import read_xls

k_vs = [0, 0.5, 1]
color = ["blue", "red", "green"]


f_range = np.logspace(0, 6, 10000)
w_range = [2 * pi * i for i in f_range]


def random_color():
    return '#%02x%02x%02x' % (randrange(256),randrange(256),randrange(256))


def add_legend(mode, ax):

    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (Hz)")
    if mode == "mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")


def plot_contraste(mode, filename):

    fig, ax1 = plt.subplots()
    patches = []

    for i in range(len(k_vs)):
        kvalue = k_vs[i]
        print(kvalue)
        cl = random_color()

        t = transferencias.get_transfer(kvalue)
        h = signal.lti(t[0], t[1])
        w, mag, pha = signal.bode(h, w_range)
        f = [i / 2 / pi for i in w]

        for j in range(len(pha)):
            if pha[j] < -180:
                pha[j] += 360

        if mode == "mag":
            ax1.semilogx(f, mag, cl)
        else:
            ax1.semilogx(f, pha, cl)

        patches.append(mpatches.Patch(color=cl, label="k="+str(int(kvalue*10)/10 )))


    plt.legend(handles=patches)
    add_legend(mode, ax1)

    datacursor_easy.make_datacursor("mag", "output/" + filename, plt, fig)

    plt.show()


# plot_contraste("mag", "distintos_k_mag.png")
# plot_contraste("pha", "distintos_k_pha.png")


def plot_mediciones(mode, mediciones_filename, spice_filename, output_filename, kvalue, tf=transferencias.get_transfer):

    fig, ax1 = plt.subplots()
    patches = []

    t = tf(kvalue)
    h = signal.lti(t[0], t[1])

    w, mag, pha = signal.bode(h, w_range)
    f = [i / 2 / pi for i in w]
    for j in range(len(pha)):
        if pha[j] < -180:
            pha[j] += 360

    if mode == "mag":
        ax1.semilogx(f, mag, "green")
    else:
        ax1.semilogx(f, pha, "green")
    patches.append(mpatches.Patch(color="green", label="Teórico"))

    data_spice = read_spice.read_file_spice("Data de Simulacion para graficos/" + spice_filename)

    if mode == "mag":
        ax1.semilogx(data_spice["f"], data_spice["abs"], "red")
    else:
        ax1.semilogx(data_spice["f"], data_spice["pha"], "red")

    patches.append(mpatches.Patch(color="red", label="Simulación"))

    data_mediciones = read_xls.read_excel_data("Mediciones/"+mediciones_filename)


    if mode == "mag":
        ax1.semilogx(data_mediciones["Freq"], data_mediciones["Ratio"], "blue")
    else:
        ax1.semilogx(data_mediciones["Freq"], data_mediciones["Fase"], "blue")

    patches.append(mpatches.Patch(color="blue", label="Mediciones"))

    plt.legend(handles=patches)
    add_legend(mode, ax1)

    datacursor_easy.make_datacursor(mode, "output/" + output_filename, plt, fig)


def plot_mediciones_zin(mode, mediciones_filename, spice_filename, output_filename, kvalue, tf, factor=1):
    fig, ax1 = plt.subplots()
    patches = []

    t = tf(kvalue)
    h = signal.lti(t[0], t[1])

    w, H = signal.freqresp(h, w_range)
    f = [i / 2 / pi for i in w]

    if mode == "mag":
        ax1.semilogx(f, abs(H), "green")
    else:
        angle = [atan2(H[i].imag, H[i].real)/pi*180.0 for i in range(len(H))]
        ax1.semilogx(f, angle, "green")

    patches.append(mpatches.Patch(color="green", label="Teórico"))

    data_spice = read_spice.read_file_spice("Data de Simulacion para graficos/"+spice_filename)

    if mode == "mag":
        ax1.semilogx(data_spice["f"], [10**(i/20.0) for i in data_spice["abs"]], "red")
    else:
        ax1.semilogx(data_spice["f"], data_spice["pha"], "red")

    patches.append(mpatches.Patch(color="red", label="Simulación"))

    data_medido = read_xls.read_excel_data("Mediciones/"+mediciones_filename)
    data_medido["Zfase"] = [i*factor for i in data_medido["Zfase"]]

    val = [data_medido["ZinR"][i] + data_medido["ZinIm"][i]*1j for i in range(len(data_medido["ZinR"]))]
    abs_val = [abs(i) for i in val]

    if mode == "mag":
        ax1.semilogx(data_medido["Freq"], abs_val, "blue")
    else:
        ax1.semilogx(data_medido["Freq"], data_medido["Zfase"], "blue")

    patches.append(mpatches.Patch(color="blue", label="Medido"))

    plt.legend(handles=patches)

    datacursor_easy.make_datacursor_zin(mode, "output/" + output_filename, plt, fig, plt)


#
# plot_mediciones(mode="mag",
#                 mediciones_filename="Ej4_Bode_k05.xlsx",
#                 spice_filename="Bode_K05.txt",
#                 output_filename="contraste_k=05_mag.png",
#                 kvalue=0.5)

# plot_mediciones(mode="mag",
#                 mediciones_filename="Ej4_Bode_k0.xlsx",
#                 spice_filename="Bode_K0.txt",
#                 output_filename="contraste_k=0_mag.png",
#                 kvalue=0)
#
#
# plot_mediciones(mode="mag",
#                 mediciones_filename="Ej4_Bode_k1.xlsx",
#                 spice_filename="Bode_K1.txt",
#                 output_filename="contraste_k=1_mag.png",
#                 kvalue=1)

# plot_mediciones(mode="pha",
#                 mediciones_filename="Ej4_Bode_k05.xlsx",
#                 spice_filename="Bode_K05.txt",
#                 output_filename="contraste_k=05_pha.png",
#                 kvalue=0.5)
#
# plot_mediciones(mode="pha",
#                 mediciones_filename="Ej4_Bode_k0.xlsx",
#                 spice_filename="Bode_K0.txt",
#                 output_filename="contraste_k=0_pha.png",
#                 kvalue=0)
#
#

# plot_mediciones_zin(mode="mag",
#                 mediciones_filename="Ej4_Bode_k1.xlsx",
#                 spice_filename="Zin_K1.txt",
#                 output_filename="contraste_zin_k=1_mag.png",
#                 kvalue=1,
#                 tf=transferencias.get_transfer_zin)
#
# plot_mediciones_zin(mode="pha",
#                 mediciones_filename="Ej4_Bode_k1.xlsx",
#                 spice_filename="Zin_K1.txt",
#                 output_filename="contraste_zin_k=1_pha.png",
#                 kvalue=1,
#                 tf=transferencias.get_transfer_zin,
#                 factor=-1)

#
# plot_mediciones_zin(mode="mag",
#                 mediciones_filename="Ej4_Bode_k0.xlsx",
#                 spice_filename="Zin_K0.txt",
#                 output_filename="contraste_zin_k=0_mag.png",
#                 kvalue=0,
#                 tf=transferencias.get_transfer_zin)

plot_mediciones_zin(mode="pha",
                mediciones_filename="Ej4_Bode_k0.xlsx",
                spice_filename="Zin_K0.txt",
                output_filename="contraste_zin_k=0_pha.png",
                kvalue=0,
                tf=transferencias.get_transfer_zin,
                factor=-1)

