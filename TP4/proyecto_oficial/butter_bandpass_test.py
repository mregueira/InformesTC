from aprox.butter import Butter
import matplotlib.pyplot as plt
from numpy import *
from control import *
from utils import random_color
import matplotlib.patches as mpatches

Ap = 5
Aa = 20

fa1 = 80
fa2 = 100
fa3 = 1000
fa4 = 1250


BWImp = Butter()
BWImp.configure({"filterType": "bp", "ap": Ap, "as": Aa, "fa-": fa1, "fp-": fa2, "fp+": fa3, "fa+": fa4})

patches = []
for n in range(1, 10):
    BWImp.setN(n)
    BWImp.computar(100, "con N", np.logspace(1, 6, 10000))
    val_col = random_color()

    plt.plot(BWImp.f, -BWImp.mag, linewidth=2 , color=val_col)
    patches.append(mpatches.Patch(color=val_col, label="n="+str(n)))

plt.legend(handles=patches)
plt.minorticks_on()


plt.plot([0, fa1, fa1], [Ap, Ap, 0], color="green")
plt.plot([fa2, fa2, fa3, fa3], [80, Aa, Aa, 80], color="green")
plt.plot([fa4, fa4, 200000], [0, Ap, Ap], color="green")

# plt.plot([0, fa, fa], [Aa, Aa, 0], color="green")
# plt.plot([fp, fp, 1000], [50, Ap, Ap], color="green")

plt.xscale('log')
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
#plt.axvline(wp, color='green') # cutoff frequency
plt.show()
