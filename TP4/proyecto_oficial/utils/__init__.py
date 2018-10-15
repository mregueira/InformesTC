from random import randrange
from math import floor
from numpy import log10


def random_color():
    return '#%02x%02x%02x' % (randrange(256),randrange(256),randrange(256))


def round_to_1(x):
    return round(x, -int(floor(log10(abs(x)))))
