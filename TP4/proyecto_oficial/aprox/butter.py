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
        normalization = self.fs / self.fp
        self.xi = ((10 ** (self.Ap / 10)) - 1) ** (1 / 2)
        num=log10((10**(self.As/10))-1)-log10((10**(self.Ap/10))-1)
        den=log10(self.fs/self.fp)
        self.n= math.ceil(0.5* (num)/(den))

    def getBodeData(self,filterType):
        xi=self.xi
        self.getNormalizedPoles(self.n)
        self.transferFunction= self.denormalizar()
        w, mag, phase = signal.bode(self.transferFunction)
        f= w/(2*pi)
        self.f = f
        self.mag = mag
        self.phase = phase
    def getNormalizedPoles(self,n):
        self.poles = []

        for k in range(1, n + 1):
            self.poles.append(1 / (e ** (1/self.n)) *(cmath.exp(1j * (2 * k + n - 1) * (pi / (2 * n)))))

    def denormalizar(self):
        print(self.poles)

        sn, s = sp.symbols("sn s")
        h = 1
        for pl in self.poles:
            h = h * (sn/pl + 1)

        wc = self.fp * 2 * pi

        h = h.subs(sn, s/wc)
        print(h)

        value = algebra.expand_and_get_coef(h, s)

        x = ctrl.TransferFunction([1], [1])
        self.poles = self.gather1stand2ndOrder()
        if self.filterType == "Pasa Bajos":
            for i in range(len(self.poles)):
                if self.poles[i].imag > 0:
                    num, den = self.LP_FreqTransform2ndOrd(self.poles[i], wc)
                elif self.poles[i].imag == 0:
                    num, den = self.LP_FreqTransform1ndOrd(self.poles[i], wc)
                x *= ctrl.TransferFunction(num, den)
        num, den = matlab.tfdata(x)
        print(num[0][0], den[0][0])
        print(value)
        transferFunction = signal.lti(num[0][0], den[0][0])
        #signal.lti([1], value)#
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

    def computar(self, freqRange,filterType,optionSelected):
        if self.areValidInputs(optionSelected):
            if optionSelected=="sin N":
                self.computarN()
            self.getBodeData(filterType)