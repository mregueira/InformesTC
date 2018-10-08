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
        self.Q = None

<<<<<<< HEAD
    def configure(self, Ap= -1, As= -1, fp=-1, fs=-1,filterType="No filter", n=-1,Q=-1):
=======
    def configure(self, Ap= -1, As= -1, fp=-1, fs=-1, filterType="No filter", n=-1):
>>>>>>> 62f163fe9b831d2121cc4cf9331da2b8d8b09e28
        self.fp = fp
        self.fs = fs
        self.Ap = Ap
        self.As = As
        self.n = n
        self.Q = Q
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

    def computeNandXi(self):
        self.xi = ((10 ** (self.Ap / 10)) - 1) ** (1 / 2)
        self.n= math.ceil(0.5* (log10((10**(self.As/10))-1)-log10((10**(self.Ap/10))-1))/(log10(self.fs/self.fp)))

<<<<<<< HEAD
    def getBodeData(self,filterType):
        self.getNormalizedPoles()
        self.getDenormalizedTf()
        w, self.mag, self.phase = signal.bode(self.transferFunction)
        self.f= w/(2*pi)

    def getNormalizedPoles(self):
=======
    def getBodeData(self, filterType):
        self.getNormalizedPoles(self.n)
        self.transferFunction= self.denormalizar()
        w, mag, phase = signal.bode(self.transferFunction)
        f= w/(2*pi)
        self.f=f
        self.mag=mag
        self.phase=phase

    def getNormalizedPoles(self,n):
>>>>>>> 62f163fe9b831d2121cc4cf9331da2b8d8b09e28
        poles = []
        for k in range(1, self.n + 1):
            poles.append((cmath.exp(1j * (2 * k + self.n - 1) * (pi / (2 * self.n)))))
        self.poles = poles

    def getDenormalizedTf(self):
        num=None
        den=None
        self.wc = ((1 / self.xi) ** (1 / (2 * self.n))) * self.fp * 2 * pi
        self.gather1stAnd2ndOrderPoles()
        #fijo callbacks para rescalar y denormalizar
        FirstOrderFreqRescale = {
            "Pasa Bajos": self.FirstOrderLPRescale,
            "Pasa Altos": self.FirstOrderHPRescale,
            "Pasa Banda": self.FirstOrderBPRescale,
            "Rechaza Banda": self.FirstOrderBRRescale
        }
        SecondOrderFreqRescale={
            "Pasa Bajos": self.SecondOrderLPRescale,
            "Pasa Altos": self.SecondOrderHPRescale,
            "Pasa Banda": self.SecondOrderBPRescale,
            "Rechaza Banda": self.SecondOrderBRRescale
        }
        x = ctrl.TransferFunction([1], [1])
<<<<<<< HEAD
        for i in range(len(self.poles)):
            if self.poles[i].imag > EPS:
                num, den = SecondOrderFreqRescale[self.filterType](self.poles[i], self.wc)
            elif self.poles[i].imag <= EPS:
                num, den = FirstOrderFreqRescale[self.filterType](self.poles[i], self.wc)
            x *= ctrl.TransferFunction(num, den)
        num, den = self.getControlTfCoeffs(x)
        self.transferFunction = signal.TransferFunction(num,den)

    def SecondOrderLPRescale(self,sk, wp):  # esta funcion necesita un solo conjugado!!
        x = ctrl.TransferFunction([1,0], [wp])
        transf = 1/(x**2-2*sk.real*x+abs(sk)**2)
        num, den = self.getControlTfCoeffs(transf)
        return num,den
    def FirstOrderLPRescale(self,sk, wp):
        x = ctrl.TransferFunction([1, 0], [wp])
        transf = 1 / (x-sk)
        num, den = self.getControlTfCoeffs(transf)
        return num, den
    def SecondOrderHPRescale(self,sk, wp):  # esta funcion necesita un solo conjugado!!
        x = ctrl.TransferFunction([wp],[1, 0])
        transf = 1 / (x ** 2 - 2 * sk.real * x + abs(sk) ** 2)
        num, den = self.getControlTfCoeffs(transf)
        return num, den
    def FirstOrderHPRescale(self,sk, wp):
        x = ctrl.TransferFunction([wp], [1, 0])
        transf = 1 / (x - sk)
        num, den = self.getControlTfCoeffs(transf)
        return num, den
    def SecondOrderBPRescale(self,sk, wp):
        x = ctrl.TransferFunction([self.Q/wp,0, wp*self.Q], [1,0])
        transf = 1 / (x ** 2 - 2 * sk.real * x + abs(sk) ** 2)
        num, den = self.getControlTfCoeffs(transf)
        return num, den
    def FirstOrderBPRescale(self,sk, wp):
        x = ctrl.TransferFunction([self.Q / wp, 0, wp * self.Q], [1, 0])
        transf = 1 / (x-sk)
        num, den = self.getControlTfCoeffs(transf)
        return num, den
    def SecondOrderBRRescale(self,sk, wp):
        x = ctrl.TransferFunction([self.Q/wp,0, wp*self.Q], [1,0])
        x=1/x
        transf = 1 / (x ** 2 - 2 * sk.real * x + abs(sk) ** 2)
        num, den = self.getControlTfCoeffs(transf)
        return num, den
    def FirstOrderBRRescale(self,sk, wp):
        x = ctrl.TransferFunction([self.Q / wp, 0, wp * self.Q], [1, 0])
        x=1/x
        transf = 1 / (x-sk)
        num, den = self.getControlTfCoeffs(transf)
        return num, den

    def getControlTfCoeffs(self,x):
=======
        self.poles = self.gather1stand2ndOrder()
        if self.filterType == "Pasa Bajos" or self.filterType == "Pasa bajos":
            for i in range(len(self.poles)):
                if self.poles[i].imag > EPS:
                    num, den = self.LP_FreqTransform2ndOrd(self.poles[i], self.wc)
                elif self.poles[i].imag <= EPS:
                    num, den = self.LP_FreqTransform1stdOrd(self.poles[i], self.wc)
                x *= ctrl.TransferFunction(num, den)
>>>>>>> 62f163fe9b831d2121cc4cf9331da2b8d8b09e28
        num, den = matlab.tfdata(x)
        return num[0][0], den[0][0]

    def gather1stAnd2ndOrderPoles(self):
        newPoles = []
        for i in range(len(self.poles)):
            if self.poles[i].imag >= 0:
                newPoles.append(self.poles[i])
<<<<<<< HEAD
        self.poles=newPoles

    def compute(self, freqRange,filterType,optionSelected):
        if self.areValidInputs(optionSelected):
            if optionSelected=="sin N":
                self.computeNandXi()
            self.getBodeData(filterType)
=======
        return newPoles

    def LP_FreqTransform2ndOrd(self, sk, wp):  # esta funcion necesita un solo conjugado!!
        num = [1]
        den = [1 / wp ** 2, -2 * sk.real / wp, abs(sk) ** 2]
        return num, den

    def LP_FreqTransform1stdOrd(self,sk , wp):
        num = [wp]
        den = [1, -sk * wp]
        return num, den

    def computar(self, freqRange, filterType, optionSelected):
        if self.areValidInputs(optionSelected):
            if optionSelected=="sin N":
                self.computarN()
            self.getBodeData(filterType)
>>>>>>> 62f163fe9b831d2121cc4cf9331da2b8d8b09e28
