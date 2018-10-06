import cmath
from numpy.polynomial import polynomial as P
from numpy import *
from scipy import signal
from aprox.aprox import Aprox

EPS = 1e-15

#Butter settea en sus variables la información necesaria para un bode
#Puede ser modificada con n o sin n
#Si no se dispone del n => se necesita Ap As fp fs
# si se dispone del n => se necesita el n y el Ap

#["mag","pha","f"]

class Butter(Aprox):
    def __init__(self):
        self.fp=None
        self.fs=None
        self.Ap=None
        self.As=None
        self.n=None
        self.poles = None

    def configure(self, fp= -1, fs= -1, n=-1, Ap=-1, As=-1):
        self.fp = fp
        self.fs = fs
        self.Ap = Ap
        self.As = As
        self.n = n
    def areValidInputs(self,optionSelected):
        if optionSelected=="Con N":
            if self.n<0:
                return 0
            if abs(self.n-int(self.n))< EPS: #checkeo que sea entero
                return 0
        elif optionSelected == "Sin N":
            if self.fp>self.fs:
                return 0
            if self.fp<0 or self.fs<0:
                return 0
        return 1

    def computarN(self):
        normalization = self.fs / self.fp
        self.xi = ((10 ** (self.Ap / 10)) - 1) ** (1 / 2)
        self.n = math.ceil(log10(((10**(self.As/10)) - 1)**(1/2)/ self.xi) / log10(normalization))

    def getBodeData(self):
        n=self.n
        xi=self.xi
        poles = []
        for k in range(0, n):
            poles.append((xi ** (1 / n)) * (cmath.exp(1j * (2 * k + 1 + n) * (pi / (2 * n)))))
        polescoeff = P.polyfromroots(poles)
        transferFunction = signal.TransferFunction(1, polescoeff)
        w, mag, phase = signal.bode(transferFunction)
        f= w/(2*pi)
        self.f=f
        self.mag=mag
        self.phase=phase
        self.poles = poles

    def computar(self, freqRange,filterType,optionSelected):
        if self.areValidInputs(optionSelected):
            if optionSelected=="sin N":
                self.computarN()
            self.getBodeData()