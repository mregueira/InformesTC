

from aprox.butter import Butter
from aprox.cheby import Cheby
from aprox.chebyinv import ChebyInv
from aprox.legendre import Legendre

mag_aprox = \
    {"Butterworth": Butter,
    "Chebycheff": Cheby,
    "Chebycheff inverso": ChebyInv,
    "Cauer": None,
    "Legendre": Legendre}


pha_aprox = [
    "Bessel"
]
