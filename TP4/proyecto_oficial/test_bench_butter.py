from scipy import signal
import matplotlib.pyplot as plt
from numpy import *
import cmath
from numpy.polynomial import polynomial as P
from numpy import *
from scipy import signal
from aprox.butter import *
import math
from utils import random_color

import matplotlib.patches as mpatches

#Butter settea en sus variables la información necesaria para un bode
#Puede ser modificada con n o sin n
#Si no se dispone del n => se necesita Ap As fp fs
# si se dispone del n => se necesita el n y el Ap

Ap = 0.5
Aa = 20

fp = 200
fa = 20

BWImp = Butter()
BWImp.configure({"filterType": "lp", "ap": Ap, "as": Aa, "fp": fp, "fa": fa})

BWImp.computar(100, "sin N")


patches = []
for n in range(1, 10):
    BWImp.setN(n)
    BWImp.computar(100, "con N", np.logspace(2, 3.3, 10000))
    val_col = random_color()

    plt.plot(BWImp.f, -BWImp.mag, linewidth=2 , color=val_col)
    patches.append(mpatches.Patch(color=val_col, label="n="+str(n)))

plt.legend(handles=patches)
plt.minorticks_on()


#plt.plot([1, fp, fp], [Ap, Ap, 30], color="green")
#plt.plot([fa, fa, 1000], [0, Aa, Aa], color="green")

#plt.plot([0, fa, fa], [Aa, Aa, 0], color="green")
#plt.plot([fp, fp, 1000], [50, Ap, Ap], color="green")

plt.xscale('log')
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
#plt.axvline(wp, color='green') # cutoff frequency
plt.show()
