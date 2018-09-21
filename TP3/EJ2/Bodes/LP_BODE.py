import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import control
from scipy import signal
import sympy as sp
import matplotlib.patches as mpatches
from pylab import *
from mpldatacursor import datacursor


R = 12000
C = 2.2e-9
Rg = 47
Cg = 10e-9
Zg = 200e3
BWP = 3e6*2*pi

df = pd.read_csv("meas_data/low_pass.csv")
freq = df["freq"]
amp = df["amp"]
amp = -amp


sim = pd.read_csv("spice_data/lowpass.csv")
freqsim=sim["freq"]
ampsim=sim["amp"]

sys = signal.lti(
[C*Cg*Rg, BWP*C*Cg*Rg, BWP]
,
[C**2*Cg*R*Rg + C*Cg*R*Zg + C*Cg*Rg*Zg, BWP*C**2*Cg*R*Rg + BWP*C*Cg*Rg*Zg + C*Cg*Rg + C*R + C*Rg + Cg*Zg, BWP*C*Cg*Rg + BWP*C*R + BWP*C*Rg + 1, BWP]

)

f=logspace(2,7.30102999566,100)
w= 2 * pi * f
w, mag, phase = signal.bode(sys, w)

color1="blue";
color2="green";
color3="red";


plt.semilogx(f,mag,color1)
plt.semilogx(freq,amp,color2)
plt.semilogx(freqsim,ampsim,color3)
plt.grid(True, which="both")
blue_patch = mpatches.Patch(color=color1, label='Teórico')
green_patch = mpatches.Patch(color=color2, label='Práctica')
red_patch = mpatches.Patch(color=color3, label='Simulación')
plt.legend(handles=[green_patch, blue_patch, red_patch])
datacursor(display='multiple', tolerance=10, formatter="Frec: {x:.3e}  Hz \nAmp:{y:.1f} dB".format, draggable=True)
plt.show()