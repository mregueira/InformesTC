import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from math import *
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pylab as pl

a0 = pow(10,5)
k = 1000
fig, ax1 = plt.subplots()

w_all = 10.0**np.arange(3, 9, 0.01)

def computar_datos(r1,r2,r3,r4,color):
    print("r1 = ",r1)
    print("r2 = ",r2)
    print("r3 = ",r3)

    g_ideal = -r2/r1
    q = r1*r2+r2*r3+r1*r3
    G_ac = -a0*r2*r3 / (q + a0 *r1 * r3)

    fp = 12
    fp_p = fp * (1+ r1*r3*a0/q)
    print("G_ideal=",g_ideal)
    print("G_ac=",G_ac)
    print("fp_p=",fp_p)
    wp_p = fp_p * 2 * pi

    s1 = signal.lti([G_ac], [1/wp_p,1])

    w, mag, phase = signal.bode(s1,w_all)

    f = [i/2/pi for i in w]

    #axes.figure()

    ax1.semilogx(f, mag , color, linewidth="2")



#computar_datos(r1=2*k,r2=20*k,r3=2*k,r4=10*k)


computar_datos(r1=1.2*k,r2=12*k,r3=1.2*k,r4=4.99*k , color='r')
computar_datos(r1=1.2*k,r2=1.2*k,r3=1.2*k,r4=4.99*k ,color='g')
computar_datos(r1=12*k,r2=1.2*k,r3=12*k,r4=49.9*k ,color='b')
plt.xlabel ("Frecuencia (Hz)")
plt.ylabel ("Amplitud (dB)")

red_patch = mpatches.Patch(color='red', label='Caso 1')
green_patch = mpatches.Patch(color='green', label='Caso 2')
blue_patch = mpatches.Patch(color='blue', label='Caso 3')

plt.legend(handles=[red_patch,green_patch,blue_patch])

ax1.set_axisbelow(True)
ax1.minorticks_on()
ax1.grid(which='major', linestyle='-', linewidth='0.3', color='black')
ax1.grid(which='minor', linestyle=':', linewidth='0.1', color='black')

plt.savefig('bode_inversor.png', format='png', dpi=300)
#plt.show()