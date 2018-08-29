from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def convert_map(datos):
    ans = dict()
    ans["f"] = [datos[i][0] for i in range(len(datos))]
    ans["abs"] = [datos[i][1] for i in range(len(datos))]
    ans["pha"] = [datos[i][2] for i in range(len(datos))]

    return ans

k = 10**3
m = 10**6

datos_puros = [
    [1*k,4.2,90],
    [10*k,-15.8,85],
    [40*k,-0.1,0]
]

datos_integrador = convert_map(datos_puros)


a0 = 10**(110/20)
bwp = 15*pow(10,6)

fp = bwp / a0
wp = fp * 2 * pi

fig, ax1 = plt.subplots()

def integrador_contraste(r,c, mode,f_range,input_filename,spice_filename ,output_filename):
    w_range = [i * (2 * pi) for i in f_range]
    RC = r * c

    s1 = signal.lti([-1 / RC], [1, 0])
    k = -a0
    wp_p = 1 / (RC * (a0 + 1))
    print("Intadegror caso 2, fp_p=", (wp_p / (2 * pi)))
    s2 = signal.lti([k], [1 / wp_p, 1])

    k = -a0
    print("k=", 20 * np.log10(abs(k)))
    print("tend=", 20 * np.log10(abs(k * wp / RC)))


    #print("poles=", s3.poles)
    s3 = signal.lti([-a0, 0], [c*r/wp, a0*c*r + c*r + 1/wp, 1, 0])

    f,mag,pha = signal.bode(s3,w_range)

    ### Teorico
    if mode=="mag":
        ax1.semilogx(f, mag, "red", linewidth=3)
    else:
        ax1.semilogx(f, pha, "red",linewidth=3)

    ### Simulado

    spice_data = read_file_spice("input/spice_data/"+spice_filename)

    #for i in range(len(spice_data["pha"])):
    #    if spice_data["pha"][i] > 0:
    #        spice_data["pha"][i] -= 360
    if mode=="mag":
        ax1.semilogx(spice_data["f"], spice_data["abs"], "magenta", linewidth=1,alpha=0.9)
    else:
        ax1.semilogx(spice_data["f"], spice_data["pha"], "magenta",linewidth=1,alpha=0.9)

    if mode=="mag":
        ax1.semilogx(datos_integrador["f"],datos_integrador["abs"],"black",linewidth=1.5,alpha=1)
    else:
        ax1.semilogx(datos_integrador["f"],datos_integrador["pha"],"black",linewidth=1.5,alpha=1)

    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (Hz)")
    if mode=="mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")

    magenta_patch = mpatches.Patch(color='magenta', label='Simulado')
    yellow_patch = mpatches.Patch(color='red', label='Teorico')
    cyan_patch = mpatches.Patch(color='black',label='Practico')
    plt.legend(handles=[yellow_patch, magenta_patch,cyan_patch])
    #plt.show()
    plt.savefig("output/contraste/" + output_filename, dpi=300)
    plt.cla()


integrador_contraste(r=1800,c=56*10**(-9),
                    mode="mag",
                    f_range=np.logspace(-10,6,1000),
                    input_filename="",
                    spice_filename="integrador_caso1.txt",
                    output_filename="integrador_contrasteA.png")
integrador_contraste(r=1800,c=56*10**(-9),
                    mode="pha",
                    f_range=np.logspace(-10,6,1000),
                    input_filename="",
                    spice_filename="integrador_caso1.txt",
                    output_filename="integrador_contrasteA_fase.png")




