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
bodede  = "modulo"


R = 12000
C = 2.2e-9
Rg = 47
Cg = 10e-9
Zg = 200e3
BWP = 3e6 * 2 * pi
sysposta = signal.lti(
    [C * Cg * Rg, BWP * C * Cg * Rg, BWP]
    ,
    [C ** 2 * Cg * R * Rg + C * Cg * R * Zg + C * Cg * Rg * Zg,
     BWP * C ** 2 * Cg * R * Rg + BWP * C * Cg * Rg * Zg + C * Cg * Rg + C * R + C * Rg + Cg * Zg,
     BWP * C * Cg * Rg + BWP * C * R + BWP * C * Rg + 1, BWP]
)

sys = signal.lti(
[1],
[(C *Rg) * Cg*Zg , C * R, 1]
)

simu = "spice_data/lowpass.csv"
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

wposta= 2 * pi * f
wposta, magposta, phaseposta = signal.bode(sysposta, wposta)


colorTeo="cyan";
colorTeo2="green";
colorSim="magenta";

font_size = 14;

if bodede == "modulo" :
    plt.title('Diagrama de Bode (Módulo)')
    plt.semilogx(f,mag,colorTeo, linewidth = 2)
    plt.semilogx(f,magposta,colorTeo2,linewidth = 2)

    # plt.semilogx(freq,amp,colorPrac,linewidth = 2.5)
    # plt.semilogx(freqsim,ampsim,colorSim)
    plt.ylabel('Módulo(dB)', fontsize=font_size)
    datacursor(display='multiple', tolerance=10, formatter="Frec: {x:.3e}  Hz \nAmp:{y:.1f} dB".format, draggable=True)
elif bodede == "fase" :
    plt.title('Diagrama de Bode (Fase)')
    plt.semilogx(f, phase, colorTeo, linewidth = 4)
    plt.semilogx(freq, pha, colorTeo2)
    plt.semilogx(freqsim, phasim, colorSim)
    plt.ylabel('Fase(grados)', fontsize=font_size)
    datacursor(display='multiple', tolerance=10, formatter="Frec: {x:.3e}  Hz \nFase:{y:.1f} grados".format, draggable=True)

plt.grid(True, which="both")
blue_patch = mpatches.Patch(color=colorTeo, label='Teórico con aproximaciones')
green_patch = mpatches.Patch(color=colorTeo2, label='Teorico completo')
#red_patch = mpatches.Patch(color=colorSim, label='Simulación')
plt.legend(handles=[green_patch, blue_patch])
plt.xlabel('Frecuencia(Hz)', fontsize = font_size)
matplotlib.pyplot.subplots_adjust(left=0.180, bottom=0.110, right=0.835, top=0.880, wspace=0.200, hspace=0.200)
plt.xlim(100,2e7)
plt.show()
