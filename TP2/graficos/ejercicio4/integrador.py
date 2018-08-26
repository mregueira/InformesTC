
from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


f_range = np.logspace(-11,15,100)
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

    w0 = sqrt(wp/RC)
    xi = 1.0/2.0 * w0 * RC * (a0+1+1/wp)
    print("Integrador caso 3,f0=",w0/(2*pi))
    print("Integrador caso 3,xi=",xi)

    s3 = signal.lti([k],[1/(w0**2),2*xi/w0,1])



    ### Caso 1
    w, mag, pha = signal.bode(s1, w_range)
    f = [i / 2 / pi for i in w]
    ax1.semilogx(f, mag, "black", linewidth=2,alpha=1)

    ### Caso 2
    w, mag, pha = signal.bode(s2, w_range)
    f = [i / 2 / pi for i in w]
    ax1.semilogx(f, mag, "yellow", linewidth=6,alpha=0.5)

    ### Caso 3
    w, mag, pha = signal.bode(s3, w_range)
    f = [i / 2 / pi for i in w]
    ax1.semilogx(f,mag,"red",linewidth=2,alpha=1)

    ax1.set_axisbelow(True)
    ax1.minorticks_on()
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')



intergrador_bode_teorico(1800,56*(10**(-9) ),
                       mode = "mag",
                       input_filename="",
                       spice_filename="input/caso1_derivador_sc.txt",
                       output_filename="integrador_teoricoA.png")


plt.show()