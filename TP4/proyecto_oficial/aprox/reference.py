

from aprox.butter import Butter
from aprox.cheby import Cheby
from aprox.chebyinv import ChebyInv

mag_aprox = \
    {"Butterworth": Butter,
    "Chebycheff": Cheby,
    "Chebycheff inverso": ChebyInv,
    "Cauer": None,
    "Legendre": None}


pha_aprox = [
    "Bessel"
]
