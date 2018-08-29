
from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


f_range = np.logspace(1,8,100)
w_range = [i * (2*pi) for i in f_range]
a0 = 10**(110/20)
bwp = 15*pow(10,6)

fp = bwp / a0
wp = fp * 2 * pi

fig, ax1 = plt.subplots()

def intergrador_bode_teorico(r,c, mode,input_filename,spice_filename ,output_filename):
    RC = r * c

    s1 = signal.lti([-1/RC], [1 ,0])
    k = -a0
    wp_p = 1/(RC*(a0+1))
    print("Intadegror caso 2, fp_p=",(wp_p/(2*pi)))
    s2 = signal.lti([k],[1/wp_p ,1])

    k = -a0
    print("k=",20*np.log10(abs(k)))
    print("tend=",20*np.log10(abs(k*wp/RC)))
    s3 = signal.lti([k],[r*c/wp , a0*r*c+r*c+1/wp,1])
    poles = s3.poles
    for i in range(len(poles)):
        poles[i] = poles[i] / 2 / pi
    print("poles=",poles)


    plt.xlabel("Frecuencia (Hz)")
    if mode == "mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")

    ### Caso 1
    w, mag, pha = signal.bode(s1, w_range)
    f = [i / 2 / pi for i in w]

    if mode == "mag":
        ax1.semilogx(f, mag, "black", linewidth=2,alpha=1)
    else:
        ax1.semilogx(f, pha, "black",linewidth=2,alpha=1)


    ### Caso 2
    w, mag, pha = signal.bode(s2, w_range)
    f = [i / 2 / pi for i in w]
    if mode == "mag":
        ax1.semilogx(f, mag, "yellow", linewidth=6,alpha=0.5)
    else:
        ax1.semilogx(f, pha, "yellow", linewidth=6,alpha=0.5)

    ### Caso 3
    w, mag, pha = signal.bode(s3, w_range)
    f = [i / 2 / pi for i in w]
    if mode == "mag":
        ax1.semilogx(f,mag,"red",linewidth=2,alpha=1)
    else:
        ax1.semilogx(f,pha,"red",linewidth=2,alpha=1)



    ax1.set_axisbelow(True)
    ax1.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    black_patch = mpatches.Patch(color='black', label='A finito')
    yellow_patch = mpatches.Patch(color='yellow', label='A infinito')
    red_patch = mpatches.Patch(color="red",label="A=A(w)")

    plt.legend(handles=[black_patch,yellow_patch,red_patch])

    plt.savefig("output/teoricos/" + output_filename, dpi=300)
    plt.cla()


intergrador_bode_teorico(1800,56*(10**(-9) ),
                       mode = "mag",
                       input_filename="",
                       spice_filename="input/caso1_derivador_sc.txt",
                       output_filename="integrador_teoricoA.png")

intergrador_bode_teorico(1800,56*(10**(-9) ),
                       mode = "pha",
                       input_filename="",
                       spice_filename="input/caso1_derivador_sc.txt",
                       output_filename="integrador_teoricoA_fase.png")

#plt.show()