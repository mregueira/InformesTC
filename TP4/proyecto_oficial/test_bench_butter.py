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

fp = 20
fa = 200

filterType = "Pasa Altos"
BWImp = Butter()
BWImp.configure(Ap, Aa, fp, fa, "pb")
#BWImp.computarN()

BWImp.computar(100, "Pasa Bajos", "sin N")
#b, a = signal.butter(BWImp.n, fp, 'low', analog=True)
#w, h = signal.freqs(b, a)

patches = []
for n in range(1, 10):
    BWImp.setN(n)
    BWImp.computar(100, "Pasa Bajos", "con N", np.logspace(2, 3.3, 10000))
    val_col = random_color()

    plt.plot(BWImp.f, -BWImp.mag, linewidth=2,color=val_col)
    patches.append(mpatches.Patch(color=val_col, label="n="+str(n)))

plt.legend(handles=patches)
plt.minorticks_on()

#plt.plot(w, -20*log10(abs(h)))

plt.plot([1, fp, fp],[Ap, Ap, 30], color="green")
plt.plot([fa, fa, 1000],[0, Aa, Aa], color="green")

plt.xscale('log')
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
#plt.axvline(wp, color='green') # cutoff frequency
plt.show()
