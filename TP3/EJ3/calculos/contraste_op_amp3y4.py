import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from math import *
import datacursor_easy

from read_csv import read_csv_bode
from valores import *
from scipy import signal
import read_spice
import read_csv



def get_out(v1, v2 ):
    h1 = [[
              r1 * r4 ** 2 * r5 * r6 * v2 + r1 * r4 ** 2 * r6 ** 2 * v2 + r1 * r4 ** 2 * r6 * r7 * v2 + r1 * r4 * r5 * r6 ** 2 * v2 - r1 * r4 * r5 * r6 * r7 * v1 + r1 * r4 * r5 * r6 * r7 * v2 - r2 * r3 * r4 * r5 * r6 * v1 + r2 * r3 * r4 * r5 * r6 * v2 - r2 * r3 * r4 * r6 ** 2 * v1 - r2 * r4 ** 2 * r5 * r6 * v1 + r2 * r4 ** 2 * r5 * r6 * v2 - r2 * r4 ** 2 * r6 ** 2 * v1 + r2 * r4 ** 2 * r6 ** 2 * v2 + r2 * r4 ** 2 * r6 * r7 * v2 - r2 * r4 * r5 * r6 ** 2 * v1 + r2 * r4 * r5 * r6 ** 2 * v2 - r2 * r4 * r5 * r6 * r7 * v1 + r2 * r4 * r5 * r6 * r7 * v2,
              a0 * r2 * r3 * r4 * r6 ** 2 * v2 * wp - a0 * r2 * r3 * r4 * r6 * r7 * v1 * wp + a0 * r2 * r3 * r4 * r6 * r7 * v2 * wp - a0 * r2 * r4 ** 2 * r6 * r7 * v1 * wp + r1 * r4 ** 2 * r5 * r6 * v2 * wp + r1 * r4 ** 2 * r6 ** 2 * v2 * wp + r1 * r4 ** 2 * r6 * r7 * v2 * wp + r1 * r4 * r5 * r6 ** 2 * v2 * wp - r1 * r4 * r5 * r6 * r7 * v1 * wp + r1 * r4 * r5 * r6 * r7 * v2 * wp - r2 * r3 * r4 * r5 * r6 * v1 * wp + r2 * r3 * r4 * r5 * r6 * v2 * wp - r2 * r3 * r4 * r6 ** 2 * v1 * wp - r2 * r4 ** 2 * r5 * r6 * v1 * wp + r2 * r4 ** 2 * r5 * r6 * v2 * wp - r2 * r4 ** 2 * r6 ** 2 * v1 * wp + r2 * r4 ** 2 * r6 ** 2 * v2 * wp + r2 * r4 ** 2 * r6 * r7 * v2 * wp - r2 * r4 * r5 * r6 ** 2 * v1 * wp + r2 * r4 * r5 * r6 ** 2 * v2 * wp - r2 * r4 * r5 * r6 * r7 * v1 * wp + r2 * r4 * r5 * r6 * r7 * v2 * wp],
          [r1 * r4 ** 2 * r5 * r6 + r1 * r4 ** 2 * r6 ** 2 + r1 * r4 * r5 * r6 ** 2,
           a0 * r1 * r4 ** 2 * r6 * r7 * wp + r1 * r4 ** 2 * r5 * r6 * wp + r1 * r4 ** 2 * r6 ** 2 * wp + r1 * r4 * r5 * r6 ** 2 * wp]]
    h2 = [[
              a0 * r2 * r3 * r6 * v2 * wp - a0 * r2 * r3 * r7 * v1 * wp + a0 * r2 * r3 * r7 * v2 * wp - a0 * r2 * r4 * r7 * v1 * wp],
          [r1 * r4 * r7 + r2 * r4 * r7, a0 * r1 * r4 * r7 * wp + r1 * r4 * r7 * wp + r2 * r4 * r7 * wp]]
    h3 = [[
              a0 * r1 * r4 * r5 * r6 * v2 * wp + 2 * a0 * r1 * r4 * r6 ** 2 * v2 * wp - a0 * r1 * r4 * r6 * r7 * v1 * wp + 2 * a0 * r1 * r4 * r6 * r7 * v2 * wp - a0 * r2 * r3 * r5 * r6 * v1 * wp + a0 * r2 * r3 * r5 * r6 * v2 * wp - a0 * r2 * r3 * r6 ** 2 * v1 * wp - a0 * r2 * r4 * r5 * r6 * v1 * wp + a0 * r2 * r4 * r5 * r6 * v2 * wp - 2 * a0 * r2 * r4 * r6 ** 2 * v1 * wp + 2 * a0 * r2 * r4 * r6 ** 2 * v2 * wp - a0 * r2 * r4 * r6 * r7 * v1 * wp + 2 * a0 * r2 * r4 * r6 * r7 * v2 * wp,
              a0 ** 2 * r2 * r3 * r6 ** 2 * v2 * wp ** 2 - a0 ** 2 * r2 * r3 * r6 * r7 * v1 * wp ** 2 + a0 ** 2 * r2 * r3 * r6 * r7 * v2 * wp ** 2 - a0 ** 2 * r2 * r4 * r6 * r7 * v1 * wp ** 2 + a0 * r1 * r4 * r5 * r6 * v2 * wp ** 2 + 2 * a0 * r1 * r4 * r6 ** 2 * v2 * wp ** 2 - a0 * r1 * r4 * r6 * r7 * v1 * wp ** 2 + 2 * a0 * r1 * r4 * r6 * r7 * v2 * wp ** 2 - a0 * r2 * r3 * r5 * r6 * v1 * wp ** 2 + a0 * r2 * r3 * r5 * r6 * v2 * wp ** 2 - a0 * r2 * r3 * r6 ** 2 * v1 * wp ** 2 - a0 * r2 * r4 * r5 * r6 * v1 * wp ** 2 + a0 * r2 * r4 * r5 * r6 * v2 * wp ** 2 - 2 * a0 * r2 * r4 * r6 ** 2 * v1 * wp ** 2 + 2 * a0 * r2 * r4 * r6 ** 2 * v2 * wp ** 2 - a0 * r2 * r4 * r6 * r7 * v1 * wp ** 2 + 2 * a0 * r2 * r4 * r6 * r7 * v2 * wp ** 2],
          [r1 * r4 * r5 * r6 + 2 * r1 * r4 * r6 ** 2 + r2 * r4 * r5 * r6 + 2 * r2 * r4 * r6 ** 2,
           a0 * r1 * r4 * r5 * r6 * wp + 2 * a0 * r1 * r4 * r6 ** 2 * wp + a0 * r1 * r4 * r6 * r7 * wp + a0 * r2 * r4 * r6 * r7 * wp + 2 * r1 * r4 * r5 * r6 * wp + 4 * r1 * r4 * r6 ** 2 * wp + 2 * r2 * r4 * r5 * r6 * wp + 4 * r2 * r4 * r6 ** 2 * wp,
           a0 ** 2 * r1 * r4 * r6 * r7 * wp ** 2 + a0 * r1 * r4 * r5 * r6 * wp ** 2 + 2 * a0 * r1 * r4 * r6 ** 2 * wp ** 2 + a0 * r1 * r4 * r6 * r7 * wp ** 2 + a0 * r2 * r4 * r6 * r7 * wp ** 2 + r1 * r4 * r5 * r6 * wp ** 2 + 2 * r1 * r4 * r6 ** 2 * wp ** 2 + r2 * r4 * r5 * r6 * wp ** 2 + 2 * r2 * r4 * r6 ** 2 * wp ** 2]]
    h4 = [[
              a0 ** 2 * r1 * r3 * r4 * r5 * r6 * v2 * wp ** 2 + a0 ** 2 * r1 * r3 * r4 * r6 ** 2 * v2 * wp ** 2 + a0 ** 2 * r1 * r3 * r4 * r6 * r7 * v2 * wp ** 2 + a0 ** 2 * r1 * r4 ** 2 * r5 * r6 * v2 * wp ** 2 + a0 ** 2 * r1 * r4 ** 2 * r6 ** 2 * v2 * wp ** 2 + a0 ** 2 * r1 * r4 ** 2 * r6 * r7 * v2 * wp ** 2 + a0 ** 2 * r1 * r4 * r5 * r6 ** 2 * v2 * wp ** 2 + a0 ** 2 * r1 * r4 * r5 * r6 * r7 * v2 * wp ** 2 - a0 ** 2 * r2 * r3 * r4 * r5 * r6 * v1 * wp ** 2 + a0 ** 2 * r2 * r3 * r4 * r5 * r6 * v2 * wp ** 2 - a0 ** 2 * r2 * r3 * r4 * r6 ** 2 * v1 * wp ** 2 + a0 ** 2 * r2 * r3 * r4 * r6 ** 2 * v2 * wp ** 2 - a0 ** 2 * r2 * r3 * r4 * r6 * r7 * v1 * wp ** 2 + a0 ** 2 * r2 * r3 * r4 * r6 * r7 * v2 * wp ** 2 - a0 ** 2 * r2 * r4 ** 2 * r5 * r6 * v1 * wp ** 2 + a0 ** 2 * r2 * r4 ** 2 * r5 * r6 * v2 * wp ** 2 - a0 ** 2 * r2 * r4 ** 2 * r6 ** 2 * v1 * wp ** 2 + a0 ** 2 * r2 * r4 ** 2 * r6 ** 2 * v2 * wp ** 2 - a0 ** 2 * r2 * r4 ** 2 * r6 * r7 * v1 * wp ** 2 + a0 ** 2 * r2 * r4 ** 2 * r6 * r7 * v2 * wp ** 2 - a0 ** 2 * r2 * r4 * r5 * r6 ** 2 * v1 * wp ** 2 + a0 ** 2 * r2 * r4 * r5 * r6 ** 2 * v2 * wp ** 2 - a0 ** 2 * r2 * r4 * r5 * r6 * r7 * v1 * wp ** 2 + a0 ** 2 * r2 * r4 * r5 * r6 * r7 * v2 * wp ** 2,
              a0 ** 3 * r1 * r4 ** 2 * r5 * r6 * v2 * wp ** 3 + a0 ** 3 * r1 * r4 ** 2 * r6 ** 2 * v2 * wp ** 3 + a0 ** 3 * r1 * r4 ** 2 * r6 * r7 * v2 * wp ** 3 + a0 ** 3 * r1 * r4 * r5 * r6 ** 2 * v2 * wp ** 3 - a0 ** 3 * r1 * r4 * r5 * r6 * r7 * v1 * wp ** 3 + a0 ** 3 * r1 * r4 * r5 * r6 * r7 * v2 * wp ** 3 - a0 ** 3 * r2 * r3 * r4 * r5 * r6 * v1 * wp ** 3 + a0 ** 3 * r2 * r3 * r4 * r5 * r6 * v2 * wp ** 3 - a0 ** 3 * r2 * r3 * r4 * r6 ** 2 * v1 * wp ** 3 - a0 ** 3 * r2 * r4 ** 2 * r5 * r6 * v1 * wp ** 3 + a0 ** 3 * r2 * r4 ** 2 * r5 * r6 * v2 * wp ** 3 - a0 ** 3 * r2 * r4 ** 2 * r6 ** 2 * v1 * wp ** 3 + a0 ** 3 * r2 * r4 ** 2 * r6 ** 2 * v2 * wp ** 3 + a0 ** 3 * r2 * r4 ** 2 * r6 * r7 * v2 * wp ** 3 - a0 ** 3 * r2 * r4 * r5 * r6 ** 2 * v1 * wp ** 3 + a0 ** 3 * r2 * r4 * r5 * r6 ** 2 * v2 * wp ** 3 - a0 ** 3 * r2 * r4 * r5 * r6 * r7 * v1 * wp ** 3 + a0 ** 3 * r2 * r4 * r5 * r6 * r7 * v2 * wp ** 3 + 2 * a0 ** 2 * r1 * r3 * r4 * r5 * r6 * v2 * wp ** 3 + 2 * a0 ** 2 * r1 * r3 * r4 * r6 ** 2 * v2 * wp ** 3 + 2 * a0 ** 2 * r1 * r3 * r4 * r6 * r7 * v2 * wp ** 3 + 2 * a0 ** 2 * r1 * r4 ** 2 * r5 * r6 * v2 * wp ** 3 + 2 * a0 ** 2 * r1 * r4 ** 2 * r6 ** 2 * v2 * wp ** 3 + 2 * a0 ** 2 * r1 * r4 ** 2 * r6 * r7 * v2 * wp ** 3 + 2 * a0 ** 2 * r1 * r4 * r5 * r6 ** 2 * v2 * wp ** 3 + 2 * a0 ** 2 * r1 * r4 * r5 * r6 * r7 * v2 * wp ** 3 - 2 * a0 ** 2 * r2 * r3 * r4 * r5 * r6 * v1 * wp ** 3 + 2 * a0 ** 2 * r2 * r3 * r4 * r5 * r6 * v2 * wp ** 3 - 2 * a0 ** 2 * r2 * r3 * r4 * r6 ** 2 * v1 * wp ** 3 + 2 * a0 ** 2 * r2 * r3 * r4 * r6 ** 2 * v2 * wp ** 3 - 2 * a0 ** 2 * r2 * r3 * r4 * r6 * r7 * v1 * wp ** 3 + 2 * a0 ** 2 * r2 * r3 * r4 * r6 * r7 * v2 * wp ** 3 - 2 * a0 ** 2 * r2 * r4 ** 2 * r5 * r6 * v1 * wp ** 3 + 2 * a0 ** 2 * r2 * r4 ** 2 * r5 * r6 * v2 * wp ** 3 - 2 * a0 ** 2 * r2 * r4 ** 2 * r6 ** 2 * v1 * wp ** 3 + 2 * a0 ** 2 * r2 * r4 ** 2 * r6 ** 2 * v2 * wp ** 3 - 2 * a0 ** 2 * r2 * r4 ** 2 * r6 * r7 * v1 * wp ** 3 + 2 * a0 ** 2 * r2 * r4 ** 2 * r6 * r7 * v2 * wp ** 3 - 2 * a0 ** 2 * r2 * r4 * r5 * r6 ** 2 * v1 * wp ** 3 + 2 * a0 ** 2 * r2 * r4 * r5 * r6 ** 2 * v2 * wp ** 3 - 2 * a0 ** 2 * r2 * r4 * r5 * r6 * r7 * v1 * wp ** 3 + 2 * a0 ** 2 * r2 * r4 * r5 * r6 * r7 * v2 * wp ** 3,
              a0 ** 4 * r2 * r3 * r4 * r6 ** 2 * v2 * wp ** 4 - a0 ** 4 * r2 * r3 * r4 * r6 * r7 * v1 * wp ** 4 + a0 ** 4 * r2 * r3 * r4 * r6 * r7 * v2 * wp ** 4 - a0 ** 4 * r2 * r4 ** 2 * r6 * r7 * v1 * wp ** 4 + a0 ** 3 * r1 * r4 ** 2 * r5 * r6 * v2 * wp ** 4 + a0 ** 3 * r1 * r4 ** 2 * r6 ** 2 * v2 * wp ** 4 + a0 ** 3 * r1 * r4 ** 2 * r6 * r7 * v2 * wp ** 4 + a0 ** 3 * r1 * r4 * r5 * r6 ** 2 * v2 * wp ** 4 - a0 ** 3 * r1 * r4 * r5 * r6 * r7 * v1 * wp ** 4 + a0 ** 3 * r1 * r4 * r5 * r6 * r7 * v2 * wp ** 4 - a0 ** 3 * r2 * r3 * r4 * r5 * r6 * v1 * wp ** 4 + a0 ** 3 * r2 * r3 * r4 * r5 * r6 * v2 * wp ** 4 - a0 ** 3 * r2 * r3 * r4 * r6 ** 2 * v1 * wp ** 4 - a0 ** 3 * r2 * r4 ** 2 * r5 * r6 * v1 * wp ** 4 + a0 ** 3 * r2 * r4 ** 2 * r5 * r6 * v2 * wp ** 4 - a0 ** 3 * r2 * r4 ** 2 * r6 ** 2 * v1 * wp ** 4 + a0 ** 3 * r2 * r4 ** 2 * r6 ** 2 * v2 * wp ** 4 + a0 ** 3 * r2 * r4 ** 2 * r6 * r7 * v2 * wp ** 4 - a0 ** 3 * r2 * r4 * r5 * r6 ** 2 * v1 * wp ** 4 + a0 ** 3 * r2 * r4 * r5 * r6 ** 2 * v2 * wp ** 4 - a0 ** 3 * r2 * r4 * r5 * r6 * r7 * v1 * wp ** 4 + a0 ** 3 * r2 * r4 * r5 * r6 * r7 * v2 * wp ** 4 + a0 ** 2 * r1 * r3 * r4 * r5 * r6 * v2 * wp ** 4 + a0 ** 2 * r1 * r3 * r4 * r6 ** 2 * v2 * wp ** 4 + a0 ** 2 * r1 * r3 * r4 * r6 * r7 * v2 * wp ** 4 + a0 ** 2 * r1 * r4 ** 2 * r5 * r6 * v2 * wp ** 4 + a0 ** 2 * r1 * r4 ** 2 * r6 ** 2 * v2 * wp ** 4 + a0 ** 2 * r1 * r4 ** 2 * r6 * r7 * v2 * wp ** 4 + a0 ** 2 * r1 * r4 * r5 * r6 ** 2 * v2 * wp ** 4 + a0 ** 2 * r1 * r4 * r5 * r6 * r7 * v2 * wp ** 4 - a0 ** 2 * r2 * r3 * r4 * r5 * r6 * v1 * wp ** 4 + a0 ** 2 * r2 * r3 * r4 * r5 * r6 * v2 * wp ** 4 - a0 ** 2 * r2 * r3 * r4 * r6 ** 2 * v1 * wp ** 4 + a0 ** 2 * r2 * r3 * r4 * r6 ** 2 * v2 * wp ** 4 - a0 ** 2 * r2 * r3 * r4 * r6 * r7 * v1 * wp ** 4 + a0 ** 2 * r2 * r3 * r4 * r6 * r7 * v2 * wp ** 4 - a0 ** 2 * r2 * r4 ** 2 * r5 * r6 * v1 * wp ** 4 + a0 ** 2 * r2 * r4 ** 2 * r5 * r6 * v2 * wp ** 4 - a0 ** 2 * r2 * r4 ** 2 * r6 ** 2 * v1 * wp ** 4 + a0 ** 2 * r2 * r4 ** 2 * r6 ** 2 * v2 * wp ** 4 - a0 ** 2 * r2 * r4 ** 2 * r6 * r7 * v1 * wp ** 4 + a0 ** 2 * r2 * r4 ** 2 * r6 * r7 * v2 * wp ** 4 - a0 ** 2 * r2 * r4 * r5 * r6 ** 2 * v1 * wp ** 4 + a0 ** 2 * r2 * r4 * r5 * r6 ** 2 * v2 * wp ** 4 - a0 ** 2 * r2 * r4 * r5 * r6 * r7 * v1 * wp ** 4 + a0 ** 2 * r2 * r4 * r5 * r6 * r7 * v2 * wp ** 4],
          [
              r1 * r3 * r4 * r5 * r6 + r1 * r3 * r4 * r6 ** 2 + r1 * r3 * r4 * r6 * r7 + r1 * r4 ** 2 * r5 * r6 + r1 * r4 ** 2 * r6 ** 2 + r1 * r4 ** 2 * r6 * r7 + r1 * r4 * r5 * r6 ** 2 + r1 * r4 * r5 * r6 * r7 + r2 * r3 * r4 * r5 * r6 + r2 * r3 * r4 * r6 ** 2 + r2 * r3 * r4 * r6 * r7 + r2 * r4 ** 2 * r5 * r6 + r2 * r4 ** 2 * r6 ** 2 + r2 * r4 ** 2 * r6 * r7 + r2 * r4 * r5 * r6 ** 2 + r2 * r4 * r5 * r6 * r7,
              2 * a0 * r1 * r3 * r4 * r5 * r6 * wp + 2 * a0 * r1 * r3 * r4 * r6 ** 2 * wp + a0 * r1 * r3 * r4 * r6 * r7 * wp + 3 * a0 * r1 * r4 ** 2 * r5 * r6 * wp + 3 * a0 * r1 * r4 ** 2 * r6 ** 2 * wp + 2 * a0 * r1 * r4 ** 2 * r6 * r7 * wp + 3 * a0 * r1 * r4 * r5 * r6 ** 2 * wp + 2 * a0 * r1 * r4 * r5 * r6 * r7 * wp + a0 * r2 * r3 * r4 * r5 * r6 * wp + a0 * r2 * r3 * r4 * r6 ** 2 * wp + 2 * a0 * r2 * r4 ** 2 * r5 * r6 * wp + 2 * a0 * r2 * r4 ** 2 * r6 ** 2 * wp + a0 * r2 * r4 ** 2 * r6 * r7 * wp + 2 * a0 * r2 * r4 * r5 * r6 ** 2 * wp + a0 * r2 * r4 * r5 * r6 * r7 * wp + 4 * r1 * r3 * r4 * r5 * r6 * wp + 4 * r1 * r3 * r4 * r6 ** 2 * wp + 4 * r1 * r3 * r4 * r6 * r7 * wp + 4 * r1 * r4 ** 2 * r5 * r6 * wp + 4 * r1 * r4 ** 2 * r6 ** 2 * wp + 4 * r1 * r4 ** 2 * r6 * r7 * wp + 4 * r1 * r4 * r5 * r6 ** 2 * wp + 4 * r1 * r4 * r5 * r6 * r7 * wp + 4 * r2 * r3 * r4 * r5 * r6 * wp + 4 * r2 * r3 * r4 * r6 ** 2 * wp + 4 * r2 * r3 * r4 * r6 * r7 * wp + 4 * r2 * r4 ** 2 * r5 * r6 * wp + 4 * r2 * r4 ** 2 * r6 ** 2 * wp + 4 * r2 * r4 ** 2 * r6 * r7 * wp + 4 * r2 * r4 * r5 * r6 ** 2 * wp + 4 * r2 * r4 * r5 * r6 * r7 * wp,
              a0 ** 2 * r1 * r3 * r4 * r5 * r6 * wp ** 2 + a0 ** 2 * r1 * r3 * r4 * r6 ** 2 * wp ** 2 + a0 ** 2 * r1 * r3 * r4 * r6 * r7 * wp ** 2 + 3 * a0 ** 2 * r1 * r4 ** 2 * r5 * r6 * wp ** 2 + 3 * a0 ** 2 * r1 * r4 ** 2 * r6 ** 2 * wp ** 2 + 2 * a0 ** 2 * r1 * r4 ** 2 * r6 * r7 * wp ** 2 + 3 * a0 ** 2 * r1 * r4 * r5 * r6 ** 2 * wp ** 2 + a0 ** 2 * r1 * r4 * r5 * r6 * r7 * wp ** 2 + a0 ** 2 * r2 * r3 * r4 * r6 * r7 * wp ** 2 + a0 ** 2 * r2 * r4 ** 2 * r5 * r6 * wp ** 2 + a0 ** 2 * r2 * r4 ** 2 * r6 ** 2 * wp ** 2 + a0 ** 2 * r2 * r4 ** 2 * r6 * r7 * wp ** 2 + a0 ** 2 * r2 * r4 * r5 * r6 ** 2 * wp ** 2 + 6 * a0 * r1 * r3 * r4 * r5 * r6 * wp ** 2 + 6 * a0 * r1 * r3 * r4 * r6 ** 2 * wp ** 2 + 3 * a0 * r1 * r3 * r4 * r6 * r7 * wp ** 2 + 9 * a0 * r1 * r4 ** 2 * r5 * r6 * wp ** 2 + 9 * a0 * r1 * r4 ** 2 * r6 ** 2 * wp ** 2 + 6 * a0 * r1 * r4 ** 2 * r6 * r7 * wp ** 2 + 9 * a0 * r1 * r4 * r5 * r6 ** 2 * wp ** 2 + 6 * a0 * r1 * r4 * r5 * r6 * r7 * wp ** 2 + 3 * a0 * r2 * r3 * r4 * r5 * r6 * wp ** 2 + 3 * a0 * r2 * r3 * r4 * r6 ** 2 * wp ** 2 + 6 * a0 * r2 * r4 ** 2 * r5 * r6 * wp ** 2 + 6 * a0 * r2 * r4 ** 2 * r6 ** 2 * wp ** 2 + 3 * a0 * r2 * r4 ** 2 * r6 * r7 * wp ** 2 + 6 * a0 * r2 * r4 * r5 * r6 ** 2 * wp ** 2 + 3 * a0 * r2 * r4 * r5 * r6 * r7 * wp ** 2 + 6 * r1 * r3 * r4 * r5 * r6 * wp ** 2 + 6 * r1 * r3 * r4 * r6 ** 2 * wp ** 2 + 6 * r1 * r3 * r4 * r6 * r7 * wp ** 2 + 6 * r1 * r4 ** 2 * r5 * r6 * wp ** 2 + 6 * r1 * r4 ** 2 * r6 ** 2 * wp ** 2 + 6 * r1 * r4 ** 2 * r6 * r7 * wp ** 2 + 6 * r1 * r4 * r5 * r6 ** 2 * wp ** 2 + 6 * r1 * r4 * r5 * r6 * r7 * wp ** 2 + 6 * r2 * r3 * r4 * r5 * r6 * wp ** 2 + 6 * r2 * r3 * r4 * r6 ** 2 * wp ** 2 + 6 * r2 * r3 * r4 * r6 * r7 * wp ** 2 + 6 * r2 * r4 ** 2 * r5 * r6 * wp ** 2 + 6 * r2 * r4 ** 2 * r6 ** 2 * wp ** 2 + 6 * r2 * r4 ** 2 * r6 * r7 * wp ** 2 + 6 * r2 * r4 * r5 * r6 ** 2 * wp ** 2 + 6 * r2 * r4 * r5 * r6 * r7 * wp ** 2,
              a0 ** 3 * r1 * r3 * r4 * r6 * r7 * wp ** 3 + a0 ** 3 * r1 * r4 ** 2 * r5 * r6 * wp ** 3 + a0 ** 3 * r1 * r4 ** 2 * r6 ** 2 * wp ** 3 + 2 * a0 ** 3 * r1 * r4 ** 2 * r6 * r7 * wp ** 3 + a0 ** 3 * r1 * r4 * r5 * r6 ** 2 * wp ** 3 + a0 ** 3 * r2 * r4 ** 2 * r6 * r7 * wp ** 3 + 2 * a0 ** 2 * r1 * r3 * r4 * r5 * r6 * wp ** 3 + 2 * a0 ** 2 * r1 * r3 * r4 * r6 ** 2 * wp ** 3 + 2 * a0 ** 2 * r1 * r3 * r4 * r6 * r7 * wp ** 3 + 6 * a0 ** 2 * r1 * r4 ** 2 * r5 * r6 * wp ** 3 + 6 * a0 ** 2 * r1 * r4 ** 2 * r6 ** 2 * wp ** 3 + 4 * a0 ** 2 * r1 * r4 ** 2 * r6 * r7 * wp ** 3 + 6 * a0 ** 2 * r1 * r4 * r5 * r6 ** 2 * wp ** 3 + 2 * a0 ** 2 * r1 * r4 * r5 * r6 * r7 * wp ** 3 + 2 * a0 ** 2 * r2 * r3 * r4 * r6 * r7 * wp ** 3 + 2 * a0 ** 2 * r2 * r4 ** 2 * r5 * r6 * wp ** 3 + 2 * a0 ** 2 * r2 * r4 ** 2 * r6 ** 2 * wp ** 3 + 2 * a0 ** 2 * r2 * r4 ** 2 * r6 * r7 * wp ** 3 + 2 * a0 ** 2 * r2 * r4 * r5 * r6 ** 2 * wp ** 3 + 6 * a0 * r1 * r3 * r4 * r5 * r6 * wp ** 3 + 6 * a0 * r1 * r3 * r4 * r6 ** 2 * wp ** 3 + 3 * a0 * r1 * r3 * r4 * r6 * r7 * wp ** 3 + 9 * a0 * r1 * r4 ** 2 * r5 * r6 * wp ** 3 + 9 * a0 * r1 * r4 ** 2 * r6 ** 2 * wp ** 3 + 6 * a0 * r1 * r4 ** 2 * r6 * r7 * wp ** 3 + 9 * a0 * r1 * r4 * r5 * r6 ** 2 * wp ** 3 + 6 * a0 * r1 * r4 * r5 * r6 * r7 * wp ** 3 + 3 * a0 * r2 * r3 * r4 * r5 * r6 * wp ** 3 + 3 * a0 * r2 * r3 * r4 * r6 ** 2 * wp ** 3 + 6 * a0 * r2 * r4 ** 2 * r5 * r6 * wp ** 3 + 6 * a0 * r2 * r4 ** 2 * r6 ** 2 * wp ** 3 + 3 * a0 * r2 * r4 ** 2 * r6 * r7 * wp ** 3 + 6 * a0 * r2 * r4 * r5 * r6 ** 2 * wp ** 3 + 3 * a0 * r2 * r4 * r5 * r6 * r7 * wp ** 3 + 4 * r1 * r3 * r4 * r5 * r6 * wp ** 3 + 4 * r1 * r3 * r4 * r6 ** 2 * wp ** 3 + 4 * r1 * r3 * r4 * r6 * r7 * wp ** 3 + 4 * r1 * r4 ** 2 * r5 * r6 * wp ** 3 + 4 * r1 * r4 ** 2 * r6 ** 2 * wp ** 3 + 4 * r1 * r4 ** 2 * r6 * r7 * wp ** 3 + 4 * r1 * r4 * r5 * r6 ** 2 * wp ** 3 + 4 * r1 * r4 * r5 * r6 * r7 * wp ** 3 + 4 * r2 * r3 * r4 * r5 * r6 * wp ** 3 + 4 * r2 * r3 * r4 * r6 ** 2 * wp ** 3 + 4 * r2 * r3 * r4 * r6 * r7 * wp ** 3 + 4 * r2 * r4 ** 2 * r5 * r6 * wp ** 3 + 4 * r2 * r4 ** 2 * r6 ** 2 * wp ** 3 + 4 * r2 * r4 ** 2 * r6 * r7 * wp ** 3 + 4 * r2 * r4 * r5 * r6 ** 2 * wp ** 3 + 4 * r2 * r4 * r5 * r6 * r7 * wp ** 3,
              a0 ** 4 * r1 * r4 ** 2 * r6 * r7 * wp ** 4 + a0 ** 3 * r1 * r3 * r4 * r6 * r7 * wp ** 4 + a0 ** 3 * r1 * r4 ** 2 * r5 * r6 * wp ** 4 + a0 ** 3 * r1 * r4 ** 2 * r6 ** 2 * wp ** 4 + 2 * a0 ** 3 * r1 * r4 ** 2 * r6 * r7 * wp ** 4 + a0 ** 3 * r1 * r4 * r5 * r6 ** 2 * wp ** 4 + a0 ** 3 * r2 * r4 ** 2 * r6 * r7 * wp ** 4 + a0 ** 2 * r1 * r3 * r4 * r5 * r6 * wp ** 4 + a0 ** 2 * r1 * r3 * r4 * r6 ** 2 * wp ** 4 + a0 ** 2 * r1 * r3 * r4 * r6 * r7 * wp ** 4 + 3 * a0 ** 2 * r1 * r4 ** 2 * r5 * r6 * wp ** 4 + 3 * a0 ** 2 * r1 * r4 ** 2 * r6 ** 2 * wp ** 4 + 2 * a0 ** 2 * r1 * r4 ** 2 * r6 * r7 * wp ** 4 + 3 * a0 ** 2 * r1 * r4 * r5 * r6 ** 2 * wp ** 4 + a0 ** 2 * r1 * r4 * r5 * r6 * r7 * wp ** 4 + a0 ** 2 * r2 * r3 * r4 * r6 * r7 * wp ** 4 + a0 ** 2 * r2 * r4 ** 2 * r5 * r6 * wp ** 4 + a0 ** 2 * r2 * r4 ** 2 * r6 ** 2 * wp ** 4 + a0 ** 2 * r2 * r4 ** 2 * r6 * r7 * wp ** 4 + a0 ** 2 * r2 * r4 * r5 * r6 ** 2 * wp ** 4 + 2 * a0 * r1 * r3 * r4 * r5 * r6 * wp ** 4 + 2 * a0 * r1 * r3 * r4 * r6 ** 2 * wp ** 4 + a0 * r1 * r3 * r4 * r6 * r7 * wp ** 4 + 3 * a0 * r1 * r4 ** 2 * r5 * r6 * wp ** 4 + 3 * a0 * r1 * r4 ** 2 * r6 ** 2 * wp ** 4 + 2 * a0 * r1 * r4 ** 2 * r6 * r7 * wp ** 4 + 3 * a0 * r1 * r4 * r5 * r6 ** 2 * wp ** 4 + 2 * a0 * r1 * r4 * r5 * r6 * r7 * wp ** 4 + a0 * r2 * r3 * r4 * r5 * r6 * wp ** 4 + a0 * r2 * r3 * r4 * r6 ** 2 * wp ** 4 + 2 * a0 * r2 * r4 ** 2 * r5 * r6 * wp ** 4 + 2 * a0 * r2 * r4 ** 2 * r6 ** 2 * wp ** 4 + a0 * r2 * r4 ** 2 * r6 * r7 * wp ** 4 + 2 * a0 * r2 * r4 * r5 * r6 ** 2 * wp ** 4 + a0 * r2 * r4 * r5 * r6 * r7 * wp ** 4 + r1 * r3 * r4 * r5 * r6 * wp ** 4 + r1 * r3 * r4 * r6 ** 2 * wp ** 4 + r1 * r3 * r4 * r6 * r7 * wp ** 4 + r1 * r4 ** 2 * r5 * r6 * wp ** 4 + r1 * r4 ** 2 * r6 ** 2 * wp ** 4 + r1 * r4 ** 2 * r6 * r7 * wp ** 4 + r1 * r4 * r5 * r6 ** 2 * wp ** 4 + r1 * r4 * r5 * r6 * r7 * wp ** 4 + r2 * r3 * r4 * r5 * r6 * wp ** 4 + r2 * r3 * r4 * r6 ** 2 * wp ** 4 + r2 * r3 * r4 * r6 * r7 * wp ** 4 + r2 * r4 ** 2 * r5 * r6 * wp ** 4 + r2 * r4 ** 2 * r6 ** 2 * wp ** 4 + r2 * r4 ** 2 * r6 * r7 * wp ** 4 + r2 * r4 * r5 * r6 ** 2 * wp ** 4 + r2 * r4 * r5 * r6 * r7 * wp ** 4]]
    return h1, h2, h3, h4


def add_legend(mode, l1, l2, l3, l4, ax):
    blue_patch = mpatches.Patch(color='blue', label=l1)
    red_patch = mpatches.Patch(color='red', label=l2)
    green_patch = mpatches.Patch(color='green', label=l3)
    cyan_patch = mpatches.Patch(color='cyan', label=l4)

    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    ax.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.xlabel("Frecuencia (Hz)")
    if mode == "mag":
        plt.ylabel("Amplitud (dB)")
    else:
        plt.ylabel("Fase (grados)")

    plt.legend(handles=[green_patch, blue_patch, red_patch, cyan_patch])


def plot_contraste(v1, v2, mode, filename):
    fig, ax1 = plt.subplots()

    h1, h2, h3, h4 = get_out(v1, v2)

    f_range = np.logspace(2, 8, 10000)

    w_range = [2 * pi * i for i in f_range]

    s1 = signal.lti(h1[0], h1[1])
    s2 = signal.lti(h2[0], h2[1])
    s3 = signal.lti(h3[0], h3[1])
    s4 = signal.lti(h4[0], h4[1])

    w, mag, pha = signal.bode(s1, w_range)
    for i in range(len(pha)):
        if pha[i] < -150:
            pha[i] += 360

    f = [i / 2 / pi for i in w]
    if mode == "mag":
        ax1.semilogx(f, mag, "blue")
    else:
        ax1.semilogx(f, pha, "blue")

    #print(h2)
    w, mag, pha = signal.bode(s2, w_range)
    f = [i / 2 / pi for i in w]
    if mode == "mag":
        ax1.semilogx(f, mag, "red")
    else:
        ax1.semilogx(f, pha, "red")

    w, mag, pha = signal.bode(s3, w_range)
    f = [i / 2 / pi for i in w]
    if mode == "mag":
        ax1.semilogx(f, mag, "green")
    else:
        ax1.semilogx(f, pha, "green")

    w, mag, pha = signal.bode(s4, w_range)
    f = [i / 2 / pi for i in w]
    if mode == "mag":
        ax1.semilogx(f, mag, "cyan")
    else:
        ax1.semilogx(f, pha, "cyan")

    add_legend(mode, l1="4 - no ideal", l2="3 - no ideal", l3="3y4 - no ideal", l4="nada ideal", ax=ax1)

    datacursor_easy.make_datacursor(mode, "output/" + filename + "_" + mode + ".png", plt, fig)



plot_contraste(
    v1=1/2,
    v2=-1/2,
    mode="mag",
    filename="modo_diferencial")

plot_contraste(
    v1=1/2,
    v2=-1/2,
    mode="pha",
    filename="modo_diferencial")


plot_contraste(
    v1= 1,
    v2= 1,
    mode="mag",
    filename="modo_comun"
)

plot_contraste(
    v1= 1,
    v2= 1,
    mode="pha",
    filename="modo_comun"
)
