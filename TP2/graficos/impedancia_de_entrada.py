import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from math import *
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


a0 = pow(10,5)
k = 1000
fig, ax1 = plt.subplots()

w_all = 10.0**np.arange(4, 9, 0.01)

def computar_datos(r1,r2,r3,r4,color):
    print("r1 = ",r1)
    print("r2 = ",r2)
    print("r3 = ",r3)

    g_ideal = -r2/r1
    q = r1*r2+r2*r3+r1*r3
    G_ac = -a0*r2*r3 / (q + a0 *r1 * r3)

    fp = 12
    wp = fp * 2 * pi

    fp_p = fp * (1+ r1*r3*a0/q)
    wp_p = fp_p * 2 * pi
    wp_pp = (G_ac / a0 + 1) / (1 / wp_p + G_ac / (a0 * wp))
    fp_pp = wp_pp / 2 / pi

    print("G_ideal=", g_ideal)
    print("G_ac=", G_ac)
    print("fp_p=", fp_p)
    print("fp_p[=", fp_pp)

    k = r1 / (G_ac/a0 +1)


    s1 = signal.lti([k/wp_p,k], [1/wp_pp , 1  ])

    w, H = signal.freqresp(s1, w_all)

    f = [i / 2 / pi for i in w]


    # axes.figure()


    ax1.semilogx(f, abs(H), color, linewidth="2")


plt.xlabel ("Frecuencia (Hz)")
plt.ylabel ("Impedancia (ohm)")


computar_datos(r1=1.2*k,r2=12*k,r3=1.2*k,r4=4.99*k , color='r')
computar_datos(r1=1.2*k,r2=1.2*k,r3=1.2*k,r4=4.99*k ,color='g')
computar_datos(r1=12*k,r2=1.2*k,r3=12*k,r4=49.9*k ,color='b')
ax1.grid(which='major', linestyle='-', linewidth='0.3', color='black')
ax1.grid(which='minor', linestyle=':', linewidth='0.1', color='black')
red_patch = mpatches.Patch(color='red', label='Caso 1')
green_patch = mpatches.Patch(color='green', label='Caso 2')
blue_patch = mpatches.Patch(color='blue', label='Caso 3')

plt.legend(handles=[red_patch,green_patch,blue_patch])

ax1.set_axisbelow(True)
ax1.minorticks_on()
ax1.grid(which='major', linestyle='-', linewidth='0.3', color='black')
ax1.grid(which='minor', linestyle=':', linewidth='0.1', color='black')

plt.savefig('bode_inversor_impedancia.png', format='png', dpi=300)
plt.show()