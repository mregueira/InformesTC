from scipy import signal
import matplotlib.pyplot as plt
from numpy import *
import cmath
from numpy.polynomial import polynomial as P
from numpy import *
from scipy import signal
from control import *
from aprox import *
import control as ctrl
from control import matlab


EPS = 1e-15


class Butter(Aprox):
    def __init__(self):
        self.f = None
        self.mag = None
        self.phase = None
        self.fp = None
        self.fs = None
        self.Ap = None
        self.As = None
        self.n = None
        self.poles = None
        self.transferFunction = None
        self.wc = None

    def configure(self, Ap= -1, As= -1, fp=-1, fs=-1, filterType="No filter", n=-1):
        self.fp = fp
        self.fs = fs
        self.Ap = Ap
        self.As = As
        self.n = n
        self.filterType = filterType

    def areValidInputs(self, optionSelected):
        if optionSelected == "Con N":
            if self.n < 0:
                return 0
            if abs(self.n-int(self.n)) < EPS: #checkeo que sea entero
                return 0
        elif optionSelected == "Sin N":
            if self.fp > self.fs:
                return 0
            if self.fp < 0 or self.fs < 0:
                return 0
        return 1

    def computarN(self):
        normalization = self.fs / self.fp
        self.xi = ((10 ** (self.Ap / 10)) - 1) ** (1 / 2)
        num=log10((10**(self.As/10))-1)-log10((10**(self.Ap/10))-1)
        den=log10(self.fs/self.fp)
        self.n= math.ceil(0.5* (num)/(den))

    def getBodeData(self, filterType, f_range):
        self.getNormalizedPoles(self.n)
        self.transferFunction = self.denormalizar()
        if len(f_range) > 0:
            w_range = [2*pi*i for i in f_range]
            w, mag, phase = signal.bode(self.transferFunction, w_range)
        else:
            w, mag, phase = signal.bode(self.transferFunction)
        f = w/(2*pi)
        self.f = f
        self.mag = mag
        self.phase = phase

    def getNormalizedPoles(self, n):
        poles = []
        for k in range(1, n + 1):
            poles.append((cmath.exp(1j * (2 * k + n - 1) * (pi / (2 * n)))))
        self.poles = poles

    def denormalizar(self):
        self.wc = ((1/self.xi) ** (1 / (2*self.n))) * self.fp * 2 * pi
        x = ctrl.TransferFunction([1], [1])
        self.poles = self.gather1stand2ndOrder()
        if self.filterType == "Pasa Bajos" or self.filterType == "Pasa bajos":
            for i in range(len(self.poles)):
                if self.poles[i].imag > EPS:
                    num, den = self.LP_FreqTransform2ndOrd(self.poles[i], self.wc)
                elif self.poles[i].imag <= EPS:
                    num, den = self.LP_FreqTransform1stdOrd(self.poles[i], self.wc)
                x *= ctrl.TransferFunction(num, den)
        num, den = matlab.tfdata(x)
        transferFunction = signal.TransferFunction(num[0][0], den[0][0])
        return transferFunction

    def gather1stand2ndOrder(self):
        newPoles = []
        for i in range(len(self.poles)):
            if self.poles[i].imag >= 0:
                newPoles.append(self.poles[i])
        return newPoles

    def LP_FreqTransform2ndOrd(self, sk, wp):  # esta funcion necesita un solo conjugado!!
        num = [1]
        den = [1 / wp ** 2, -2 * sk.real / wp, abs(sk) ** 2]
        return num, den

    def LP_FreqTransform1stdOrd(self,sk , wp):
        num = [wp]
        den = [1, -sk * wp]
        return num, den

    def computar(self, freqRange, filterType, optionSelected, f_range=[]):

        if self.areValidInputs(optionSelected):
            if optionSelected == "sin N":
                self.computarN()
            self.getBodeData(filterType, f_range)
