import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import control
from scipy import signal
import sympy as sp
import matplotlib.patches as mpatches
from pylab import *
from mpldatacursor import datacursor
import numpy as np
import matplotlib.pyplot as plt

medicion = "meas_data/low_pass.csv"
bodede  = "fase"


if medicion == "meas_data/low_pass.csv" :
    R = 12000
    C = 2.2e-9
    Rg = 47
    Cg = 10e-9
    Zg = 200e3
    BWP = 3e6 * 2 * pi
    # sys = signal.lti(
    #     [C * Cg * Rg, BWP * C * Cg * Rg, BWP]
    #     ,
    #     [C ** 2 * Cg * R * Rg + C * Cg * R * Zg + C * Cg * Rg * Zg,
    #      BWP * C ** 2 * Cg * R * Rg + BWP * C * Cg * Rg * Zg + C * Cg * Rg + C * R + C * Rg + Cg * Zg,
    #      BWP * C * Cg * Rg + BWP * C * R + BWP * C * Rg + 1, BWP]
    # )

    sys = signal.lti(
    [1],
    [(C*Cg*R*Zg)/BWP,((1/BWP)+C *Rg) * Cg*Zg , C * R, 1]
    )


    simu = "spice_data/lowpass.csv"
elif medicion == "meas_data/high_pass.csv" :
    R = 680
    C = 470e-9
    Rg = 100
    Cg = 6.8e-9
    Zg = 51e3
    BWP = 3e6 * 2 * pi

    sys = signal.lti(
        [C * Cg * Rg * Zg, BWP * C * Cg * Rg * Zg + C * Rg, BWP * C * Rg, 0]
        ,
        [C * Cg * R * Rg + C * Cg * R * Zg + C * Cg * Rg * Zg,
         BWP * C * Cg * R * Rg + BWP * C * Cg * Rg * Zg + C * R + C * Rg + Cg * Rg + Cg * Zg,
         BWP * C * R + BWP * C * Rg + BWP * Cg * Rg + 1, BWP]
    )
    simu = "spice_data/highpass.csv"
elif medicion == "meas_data/band_pass.csv" :
    R = 1000
    C = 5.6e-9
    Rg = 100
    Cg = 470e-12
    Zg = 510e3
    BWP = 3e6 * 2 * pi
    sys = signal.lti(

        [Cg * Rg * Zg, BWP * Cg * Rg * Zg + Rg, BWP * Rg]
        ,
        [C * Cg * R * Rg * Zg, BWP * C * Cg * R * Rg * Zg + C * R * Rg + Cg * R * Rg + Cg * R * Zg + Cg * Rg * Zg,
         BWP * C * R * Rg + BWP * Cg * R * Rg + BWP * Cg * Rg * Zg + R + Rg, BWP * R + BWP * Rg]
    )
    simu = "spice_data/bandpass.csv"
elif medicion == "meas_data/band_reject.csv" :

    R = 1000
    C = 470e-9
    Rg = 100
    Cg = 1e-9
    Zg = 510e3
    BWP = 3e6 * 2 * pi

    sys = signal.lti(
        [C * Cg * Rg * Zg, BWP * C * Cg * Rg * Zg + C * Rg + Cg * Rg + Cg * Zg, BWP * C * Rg + BWP * Cg * Rg + 1, BWP]
        ,
        [C * Cg * R * Rg + C * Cg * R * Zg + C * Cg * Rg * Zg,
         BWP * C * Cg * R * Rg + BWP * C * Cg * Rg * Zg + C * R + C * Rg + Cg * Rg + Cg * Zg,
         BWP * C * R + BWP * C * Rg + BWP * Cg * Rg + 1, BWP]
    )
    simu = "spice_data/bandreject.csv"

df = pd.read_csv(medicion)
freq = df["freq"]
amp = df["amp"]
pha = df["pha"]

if medicion == "meas_data/low_pass.csv" :
    amp = -amp
    pha= -pha


sim = pd.read_csv(simu)
freqsim=sim["freq"]
ampsim=sim["amp"]
phasim=sim["phase"]


if(medicion== "meas_data/low_pass.csv"):
    for i in range(len(pha)):
        if pha[i] > 0 :
            pha[i] = pha[i]-360

    for i in range(len(phasim)):
        if phasim[i] > 0:
            phasim[i] = phasim[i] - 360



f=logspace(2,7.30102999566,1000)
w= 2 * pi * f
w, mag, phase = signal.bode(sys, w)


colorTeo="cyan";
colorPrac="green";
colorSim="magenta";

font_size = 14;

if bodede == "modulo" :
    plt.title('Diagrama de Bode (Módulo)')
    plt.semilogx(f,mag,colorTeo, linewidth = 4)
    plt.semilogx(freq,amp,colorPrac,linewidth = 2.5)
    plt.semilogx(freqsim,ampsim,colorSim)
    plt.ylabel('Módulo(dB)', fontsize=font_size)
    datacursor(display='multiple', tolerance=10, formatter="Frec: {x:.3e}  Hz \nAmp:{y:.1f} dB".format, draggable=True)
elif bodede == "fase" :
    plt.title('Diagrama de Bode (Fase)')
    plt.semilogx(f, phase, colorTeo, linewidth = 4)
    plt.semilogx(freq, pha, colorPrac)
    plt.semilogx(freqsim, phasim, colorSim)
    plt.ylabel('Fase(grados)', fontsize=font_size)
    datacursor(display='multiple', tolerance=10, formatter="Frec: {x:.3e}  Hz \nFase:{y:.1f} grados".format, draggable=True)

plt.grid(True, which="both")
blue_patch = mpatches.Patch(color=colorTeo, label='Teórico')
green_patch = mpatches.Patch(color=colorPrac, label='Práctica')
red_patch = mpatches.Patch(color=colorSim, label='Simulación')
plt.legend(handles=[green_patch, blue_patch, red_patch])
plt.xlabel('Frecuencia(Hz)', fontsize = font_size)
matplotlib.pyplot.subplots_adjust(left=0.180, bottom=0.110, right=0.835, top=0.880, wspace=0.200, hspace=0.200)
plt.xlim(100,2e7)
plt.show()
