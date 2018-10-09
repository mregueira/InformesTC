
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


def denormalizar(self):
    print(self.poles)

    sn, s = sp.symbols("sn s")
    h = 1
    for pl in self.poles:
        h = h * (sn - pl)

    wc = self.fp * 2 * pi

    h = h.subs(sn, s / wc)

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
    # transferFunction = signal.lti(num[0][0], den[0][0])
    transferFunction = signal.lti([1], value)

    return transferFunction