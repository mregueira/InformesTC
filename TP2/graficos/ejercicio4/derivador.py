from read_spice import *
import sympy as sp

import numpy as np
from scipy import signal
from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

w_range = np.logspace(4,11,10000)
a0 = 10**(110/20)
bwp = 15*pow(10,6)

fp = bwp / a0
wp = fp * 2 * pi

fig, ax1 = plt.subplots()

def get_rational_coeffs(expr,var):
    num, denom = expr.as_numer_denom()
    #print(num,denom)
    return [sp.Poly(num, var).all_coeffs(), sp.Poly(denom, var).all_coeffs()]

def derivador_bode_teorico(r,c, mode,input_filename,spice_filename ,output_filename):
    #a0, r , c , s , w_p , Z2 , Z1 , A = sp.symbols("a0 r c s w_p Z2 Z1 A")

    #Z1 = 1 / (s*c)
    #Z2 = r

    #A = A0 / (s / WP + 1)

    #H = (Z2/(Z1+Z2))/ (-1/A - Z1/(Z1+Z2))
    #print(H)

    #H = H.subs(r,R)
    #H = H.subs(c,C)
    #H = H.subs(a0,A0)
    #H = H.subs(w_p,WP)
    #print("fp=",FP)
    #print("1/RC=",1/(R*C)/2/pi)

    # coef = get_rational_coeffs(H,s)
    # for i in range(len(coef[0])):
    #     coef[0][i] = float(coef[0][i].evalf())
    # for i in range(len(coef[1])):
    #     coef[1][i] = float(coef[1][i].evalf())
    # print(coef)

    ### A infinito
    RC = r*c

    s1 = signal.lti([-RC, 0], [1])
    w, mag, pha = signal.bode(s1, w_range)
    f = [i / 2 / pi for i in w]
    if mode=="mag":
        ax1.semilogx(f, mag, "blue", linewidth=2)
    else:
        ax1.semilogx(f, pha, "blue",linewidth=2)

    ### A constante
    k = -RC * (a0/(a0+1))
    wp_p = (a0+1)/RC
    print("fp_p = ",wp_p/2/pi)
    s1 = signal.lti([k ,0],[1/wp_p,1])

    w, mag, pha = signal.bode(s1, w_range)
    f = [i / 2 / pi for i in w]
    if mode=="mag":
        ax1.semilogx(f, mag, "red", linewidth=2)
    else:
        ax1.semilogx(f, pha, "red",linewidth=2)


    ### A = A(w)
    k = -a0*RC/(a0+1)
    w0 = sqrt(wp*(a0+1)/RC)
    xi = 1.0/2.0 * w0 * (RC*wp+1)/(wp *(a0+1))
    print("k=",20*np.log10(abs(k)) )
    print("f0=",w0/(10**6)/(2*pi))
    print("xi=", xi)
    print("b^2-4ac=", (wp+1/RC)**2 - 4/RC * wp*(a0+1))
    s1 = signal.lti([k, 0], [1/w0**2,2*xi/w0 , 1])
    print("poles=",s1.poles)

    w, mag, pha = signal.bode(s1, w_range)
    f = [i / 2 / pi for i in w]
    if mode=="mag":
        ax1.semilogx(f, mag, "green", linewidth=2)
    else:
        ax1.semilogx(f, pha, "green",linewidth=2)

    spice_data = read_file_spice(spice_filename)

    #ax1.semilogx(spice_data["f"],spice_data["abs"])

    blue_patch = mpatches.Patch(color='blue', label='A finito')
    red_patch = mpatches.Patch(color='red', label='A infinito')
    green_patch = mpatches.Patch(color='green', label='A=A(w)')
    ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (Hz)")
    if mode=="mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")

    plt.legend(handles=[green_patch, blue_patch,red_patch])
    plt.savefig("output/teoricos/" + output_filename, dpi=300)
    plt.cla()


derivador_bode_teorico(1800,56*(10**(-9) ),
                       mode = "mag",
                       input_filename="",
                       spice_filename="input/caso1_derivador_sc.txt",
                       output_filename="derivador_teoricoA.png")
derivador_bode_teorico(1800,56*(10**(-9) ),
                       mode = "pha",
                       input_filename="",
                       spice_filename="input/caso1_derivador_sc.txt",
                       output_filename="derivador_teorico_faseA.png")

#dibujar_bode(1500,5.8*pow(10,-9),"","","")\

ax1.set_axisbelow(True)
ax1.minorticks_on()
ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

#plt.show()
