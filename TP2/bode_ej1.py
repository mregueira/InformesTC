import numpy
from scipy import signal
import matplotlib.pyplot as plt
from math import *

g_ac = -9.9979
w_p = 47629 * 2 * pi

s1 = signal.lti([g_ac], [1/w_p, 1])

w, mag, phase = signal.bode(s1)

plt.figure()
plt.semilogx(w, mag)
plt.figure()
plt.semilogx(w, phase)  # Bode phase plot
plt.show()