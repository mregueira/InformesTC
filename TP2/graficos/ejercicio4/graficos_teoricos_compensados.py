### Derivador compensado teorico

from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from random import *

k = 10**3
m = 10**6


a0 = 10**(110/20)
bwp = 15*(10**6)

fp = bwp / a0
wp = fp * 2 * pi

fig, ax1 = plt.subplots()

def random_color():
    return '#%02x%02x%02x' % (randrange(256),randrange(256),randrange(256))

def function_derivador(r , r2 , c):
    return [[-a0 * c * (r + r2) / (a0 + 1), 0],
     [c * (r + 2 * r2) / (wp * (a0 + 1)), (a0 * c * r2 * wp + c * r * wp + 2 * c * r2 * wp + 1) / (wp * (a0 + 1)), 1]]

def function_integrador(r, r2 , c):
    return [[-a0*r2*wp], [c*r*r2, a0*c*r*r2*wp + c*r*r2*wp + r + r2, a0*r*wp + r*wp + r2*wp]]

def graficar_compensado(r,c,variable_component , h_func ,mode,f_range,output_filename):
    w_range = [i * (2 * pi) for i in f_range]

    patches = []

    for r2 in variable_component:
        func = h_func(r,r2,c)

        H = signal.lti(func[0],func[1])
        w,mag,pha=signal.bode(H,w_range)
        f = [i / 2 / pi for i in w]
        val_col = random_color()
        if mode == "mag":
            ax1.semilogx(f, mag, val_col, linewidth=3)
        #elif mode == "mag_no_log":
        #    ax1.semilogx(f, mag , val_col,linewidth=3)

        name = str("r2="+str(round(r2))+" ohm" )

        patches.append(mpatches.Patch(color=val_col,label=name))

    plt.legend(handles=patches)
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (hz)")
    plt.ylabel("Amplitud (dB)")
    plt.savefig("output/teoricos/" + output_filename, dpi=300)
    plt.cla()

    #plt.show()

res_values = np.logspace(0,4,5)


print(res_values)

graficar_compensado(r=1800,c=56*10**(-9),
                              variable_component=res_values,
                              h_func=function_derivador,
                              mode = "mag",
                              f_range=np.logspace(2,8,1000),
                              output_filename="derivador_compensado.png")


#graficar_compensado(r=1800,c=56*10**(-9),
#                    variable_component=res_values,
#                    h_func=function_integrador,
#                    mode="mag",
#                    f_range=np.logspace(-2,8,1000),
#                    output_filename="output.png")