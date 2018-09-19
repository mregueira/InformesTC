import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import control
from scipy import signal
import sympy as sp
import matplotlib.patches as mpatches
from pylab import *

R = 1000
C = 5.6e-9
Rg = 100
Cg = 470e-12
Zg = 510e3
BWP = 3e6*2*pi

df = pd.read_csv("meas_data/bpconavg.csv")
freq = df["freq"]
amp = df["amp"]

sim = pd.read_csv("spice_data/bandpass.csv")
freqsim=sim["Freq"]
ampsim=sim["magn"]

sys = signal.lti(

[Cg*Rg*Zg, BWP*Cg*Rg*Zg + Rg, BWP*Rg]
,
[C*Cg*R*Rg*Zg, BWP*C*Cg*R*Rg*Zg + C*R*Rg + Cg*R*Rg + Cg*R*Zg + Cg*Rg*Zg, BWP*C*R*Rg + BWP*Cg*R*Rg + BWP*Cg*Rg*Zg + R + Rg, BWP*R + BWP*Rg]
)

f=logspace(1,6,100)
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
plt.show()