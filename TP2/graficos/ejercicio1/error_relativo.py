from read_spice import *
import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from read_xls import *
from cmath import *

from mpldatacursor import datacursor

a0 = 1e5

fp = 12
wp = fp * 2 * pi

k = 1e3

patches = []

fig, ax1 = plt.subplots()

def error_relativo(r1,r2,r3,r4,log_range, excel_filename, spice_filename ,output_filename , mcolor , name):
    (s, e) = log_range
    g_ideal = -r2 / r1
    q = r1 * r2 + r2 * r3 + r1 * r3
    G_ac = -a0 * r2 * r3 / (q + a0 * r1 * r3)

    fp = 12
    fp_p = fp * (1 + r1 * r3 * a0 / q)
    wp_p = fp_p * 2 * pi

    s1 = signal.lti([G_ac], [1 / wp_p, 1])
    s2 = signal.lti([g_ideal], [1 ])

    f_all = 10.0 ** np.arange(s, e, 0.01)
    w_all = [i * (2 * pi) for i in f_all]

    w1, mag1, phase1 = signal.bode(s1, w_all)

    w2 , mag2 , phase2 = signal.bode(s2, w_all)

    values = []
    for i in range(len(mag1)):
        n1 = mag1[i]* ( cos( phase1[i] * pi / 180.0) + 1j * sin(phase1[i]*pi/180.0) )
        n2 = mag2[i] * (cos(phase2[i] * pi / 180.0) + 1j * sin(phase2[i] * pi / 180.0))

        maxv = max(abs(n1),abs(n2))

        values.append( abs(n2-n1) / maxv * 100 )

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Error relativo (%)")



    f1 = [i / 2 / pi for i in w1]

    patches.append(mpatches.Patch(color=mcolor, label=name))
    ax1.semilogx(f1,values,mcolor, linewidth=2)



error_relativo(r1=1.2*k,r2=12*k,r3=1.2*k,r4=4.99*k, # caso 10
             excel_filename="input/Ej1_Bodes/Inversor_G10_OK.xlsx",
             spice_filename="Inversor_G10_OK.txt",
             output_filename="Error_relativo10.png",
             log_range=(3,7),
               mcolor = "red",
             name = "Caso 1")

error_relativo(r1=1.2*k,r2=1.2*k,r3=1.2*k,r4=4.99*k, # caso 10
              excel_filename="input/Ej1_Bodes/Inversor_G1_OK.xlsx",
              spice_filename="Inversor_G1_OK.txt",
              output_filename="Error_relativo1.png",
              log_range=(3,7),
               mcolor="blue",
               name="Caso 2")

error_relativo(r1=12*k,r2=1.2*k,r3=12*k,r4=49.9*k, # caso 10
              excel_filename="input/Ej1_Bodes/Inversor_G0.1_OK.xlsx",
              spice_filename="Inversor_G0.1_OK.txt",
              output_filename="Error_relativo10.png",
              log_range=(3,7),
               mcolor="green",
               name="Caso 3")


plt.legend(handles=patches)

ax1.set_axisbelow(True)
ax1.minorticks_on()
ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

plt.show()