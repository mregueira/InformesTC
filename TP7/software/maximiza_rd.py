# coding=utf-8
import sympy as sp
from numpy import pi
from utils import etapas, algebra
from utils.computeRD import computeRD, setGain
import itertools
from scipy import signal
from numpy import logspace

s = sp.symbols('s')
wp = 2*pi*13250
SHP = wp/s

H1 = 1/(SHP**2 + SHP*0.5548 + 0.2702)
H2 = 1/(SHP**2 + SHP*0.0918 + 0.9870)
H3 = 1/(SHP**2 + SHP*0.4284 + 0.5282)
H4 = 1/(SHP**2 + SHP*0.2650 + 0.8013)
H5 = 1/(SHP**2 + SHP*0.6344 + 0.1218)

conjunto = H1 * H2 * H3 * H4 * H5

w, mag, pha = signal.bode(algebra.conseguir_tf(conjunto, s), [1e7*2*pi])
total_gain = -mag[0]

#
# print("total_gain = ", total_gain)
# conjunto = H1 * H2 * H3 * H4 * H5 * total_gain
#
# mag, pha, w = signal.bode(algebra.conseguir_tf(conjunto, s),1e6)
# total_gain = -mag[0]
print("total_gain = ", total_gain)
#
#
transf = [H1, H2, H3, H4, H5]

transf = [etapas.EtapaEA(i, s) for i in transf]
transf[0].name = "1"
transf[1].name = "2"
transf[2].name = "3"
transf[3].name = "4"
transf[4].name = "5"

for i in transf:
    i.getMaxMinGain()

# transf[0].gain = -30
# transf[1].gain = -7.23513357298833
# transf[2].gain = 0
# transf[3].gain = 0
# transf[4].gain = 0

for it in itertools.permutations(transf):
    #setGain(it, total_gain)
    #print("Rango dinamico : ", computeRD(it)[2])
    for i in it:
        i.getMaxMinGain()
    setGain(it, total_gain)

    print("Rango dinamico : ", computeRD(it)[2])

    print("Gains : ")
    for j in it:
       print("T["+j.name+"] " ,j.gain)
