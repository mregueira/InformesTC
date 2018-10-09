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
import sympy as sp
import utils.algebra as algebra
import config


sn, s = sp.symbols("sn s")


class Butter(Aprox):
    def __init__(self):
        self.f = None
        self.mag = None
        self.phase = None
        self.fp= None
        self.fs= None
        self.Ap=None
        self.As=None
        self.n=None
        self.poles = None
        self.symbolic_poles = None
        self.transferFunction = None

    def configure(self, Ap= -1, As= -1, fp=-1, fs=-1, filterType="No filter", n=-1):
        self.fp = fp
        self.fs = fs
        self.Ap = Ap
        self.As = As
        self.n = n
        self.filterType = filterType

    def areValidInputs(self,optionSelected):
        if optionSelected == "Con N":
            if self.n < 0:
                return 0
            if abs(self.n-int(self.n)) < EPS: #checkeo que sea entero
                return 0
        elif optionSelected == "Sin N":
            if self.fp>self.fs:
                return 0
            if self.fp<0 or self.fs<0:
                return 0
        return 1

    def computarN(self):
        print("Fs=", self.fs,"Fa=", self.fp)
        print("Ap=", self.Ap, ", As=", self.As)
        normalization = self.fs / self.fp
        self.xi = sqrt((10 ** (self.Ap / 10)) - 1)
        num = log10(sqrt((10**(self.As/10))-1) / self.xi)
        den = log10(self.fs/self.fp)
        #print(num/den)
        self.n = math.ceil(num/den)
        if config.debug:
            print("xi=",self.xi)
            print("n = ", self.n)

    def setN(self, n):
        self.n = n

    def getBodeData(self,filterType, points):
        self.getNormalizedPoles(self.n)
        if self.filterType == "pb":
            self.transferFunction = self.denormalizar(s/(self.fp * 2 * pi) * (self.xi ** (1/self.n)))
        elif self.filterType == "pa":
            self.transferFunction = self.denormalizar((self.fp * 2 * pi)/s * (self.xi ** (1 / self.n)))

        w, mag, phase = signal.bode(self.transferFunction, points)
        self.f = w/(2*pi)
        self.mag = mag
        self.phase = phase

    def getNormalizedPoles(self,n):
        self.poles = []
        #if config.debug:
        #    print("xi:", self.xi)

        for k in range(1, n + 1):
            self.poles.append((cmath.exp(1j * (2 * k + n - 1) * (pi / (2 * n)))))

    def denormalizar(self , substituteFactor):
        #print(self.poles)

        h = 1
        for pl in self.poles:
            h = h * 1 / ((sn - pl) / (-pl))

        h = h.subs(sn, substituteFactor)

        value = algebra.expand_and_get_coef(h, s)
        transferFunction = signal.lti(value[0], value[1])

        return transferFunction

    def gather1stand2ndOrder(self):
        newPoles = []
        for i in range(len(self.poles)):
            if self.poles[i].imag >= 0:
                newPoles.append(self.poles[i])
        return newPoles

    def LP_FreqTransform2ndOrd(self,sk, wp):  # esta funcion necesita un solo conjugado!!
        num = [1]
        den = [1 / wp ** 2, -2 * sk.real / wp, abs(sk) ** 2]
        return num, den

    def LP_FreqTransform1stdOrd(self,sk, wp):
        num = [wp]
        den = [1, -sk * wp]
        return num, den

    def computar(self, freqRange,filterType,optionSelected, points = []):
        if self.areValidInputs(optionSelected):
            if optionSelected == "sin N":
                self.computarN()
            self.getBodeData(filterType, points)