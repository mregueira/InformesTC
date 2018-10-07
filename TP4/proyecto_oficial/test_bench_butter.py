from scipy import signal
import matplotlib.pyplot as plt
from numpy import *
import cmath
from numpy.polynomial import polynomial as P
from numpy import *
from scipy import signal
from aprox.butter import *

EPS = 1e-15

#Butter settea en sus variables la información necesaria para un bode
#Puede ser modificada con n o sin n
#Si no se dispone del n => se necesita Ap As fp fs
# si se dispone del n => se necesita el n y el Ap

Ap = 1.5
As = 35
fp = 5000
fs = 10000

BWImp= Butter()
BWImp.configure(Ap,As,fp,fs,"Pasa Bajos")
BWImp.computarN()
print(BWImp.n)
BWImp.computar(100,"Pasa Bajos","sin N")

b, a = signal.butter(BWImp.n, 2*pi*fp, 'low', analog=True)
w, h = signal.freqs(b, a)

#plt.plot(w, rad2deg(arctan(h.imag/h.real)))
plt.plot(w, 20*log10(abs(h)))
plt.plot(BWImp.f*2*pi,BWImp.mag)

plt.xscale('log')
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green') # cutoff frequency
plt.show()