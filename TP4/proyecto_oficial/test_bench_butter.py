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

Ap = 3
As = 20
wp = 1000
ws = 2000

BWImp= Butter()
BWImp.configure(Ap,As,wp/2*pi,ws/2*pi,"Pasa Bajos")
BWImp.computarN()
BWImp.computar(100,"Pasa Bajos","sin N")

b, a = signal.butter(BWImp.n, 1, 'low', analog=True)
w, h = signal.freqs(b, a)

#plt.plot(w, rad2deg(arctan(h.imag/h.real)))
plt.plot(BWImp.f*2*pi,BWImp.phase)
plt.xscale('log')
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green') # cutoff frequency
plt.show()