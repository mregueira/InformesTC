from aprox.butter import Butter
import matplotlib.pyplot as plt
from numpy import *
from control import *
from utils import random_color
import matplotlib.patches as mpatches

Ap = 0.5
Aa = 20

fa1 = 20
fa2 = 200
fa3 = 2000
fa4 = 20000


BWImp = Butter()
BWImp.configure({"filterType": "bp", "ap": Ap, "as": Aa, "fa-": fa1, "fp-": fa2, "fp+": fa3, "fa+": fa4})
BWImp.computar(100, "sin N")

patches = []
for n in range(1, 10):
    BWImp.setN(n)
    BWImp.computar(100, "con N", np.logspace(0, 8, 10000))
    val_col = random_color()

    plt.plot(BWImp.f, -BWImp.mag, linewidth=2 , color=val_col)
    patches.append(mpatches.Patch(color=val_col, label="n="+str(n)))

plt.legend(handles=patches)
plt.minorticks_on()


# plt.plot([1, fp, fp], [Ap, Ap, 30], color="green")
# plt.plot([fa, fa, 1000], [0, Aa, Aa], color="green")

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
