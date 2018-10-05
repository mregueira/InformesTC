
import cmath
from numpy.polynomial import polynomial as P
from numpy import *
from scipy import signal

EPS = 1e-15

class Butter(Aprox):
    def __init__(self):
        self.fp=None
        self.fa=None
        self.Ap=None
        self.As=None
        self.n=None

    def configure(self, fp= -1, fa= -1, n=-1, Ap=-1, As=-1):
        self.fp = fp
        self.fa = fa
        self.Ap = Ap
        self.As = As
        self.n = n
    def areValidInputs(self,optionSelected):
        if optionSelected=="Con N":
            if self.n<0:
                return 0
            if abs(self.n-int(self.n))< EPS:
                return 0
        elif optionSelected == "Sin N":
            if self.fp>self.fa:
                return 0
            if self.fp<0 or self.fa<0:
                return 0


    def computarConN(self,n=-1):
        xi = ((10 ** (self.Ap / 10)) - 1) ** (1 / 2)
        self.getBodeData(self,n,xi)
    def computarSinN(self):
        #esta funcion se llama despues de haber validado el input
        #hacemos un pasabajos y de ahi obtenemos todos los otros filtros con una transformación de frecuencia
        normalization = self.fa / self.fp
        xi = ((10 ** (self.Ap / 10)) - 1) ** (1 / 2)
        n = math.ceil(log10(((10**(self.As/10)) - 1)**(1/2)/ xi) / log10(normalization))
        self.getBodeData(self,n,xi)

    def getBodeData(self,n,xi):
        poles = []
        for k in range(0, n):
            poles.append((xi ** (1 / n)) * (cmath.exp(1j * (2 * k + 1 + n) * (pi / (2 * n)))))
        polescoeff = P.polyfromroots(poles)
        transferFunction = signal.TransferFunction(1, polescoeff)
        w, mag, phase = signal.bode(transferFunction)
        f= w/(2*pi)
        return f,mag,phase

    def computar(self, freqRange,filterType, optionSelected,xi=-1,n=-1):
        if self.areValidInputs():
            if optionSelected == "Con N":
                self.computarConN(self,n)
            if optionSelected == "Sin N":
                self.computarSinN(self)
        #ahora se pasaron los datos a f mag y phase del objeto