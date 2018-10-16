#from scipy import signal
from scipy import signal
from scipy import pi
import matplotlib.pyplot as plt
import numpy as np
fa = (10+1.1/2)*1e3
fp = fa * 2

wp = 2*pi*fp
wa = 2*pi*fa

Ap =2
Aa = 40



N, Wn = signal.ellipord(wp,wa,Ap,Aa,True)
b, a = signal.ellip(N, Ap, Aa, Wn, 'low', True)
print(N)
w, h = signal.freqs(b, a, np.logspace(np.log10(0.1*wp),np.log10(10*wa), 100000))
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Elliptical highpass filter fit to constraints')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.grid(which='both', axis='both')
plt.show()