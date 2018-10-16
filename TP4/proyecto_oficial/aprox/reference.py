

from aprox.butter import Butter
from aprox.cheby import Cheby
from aprox.chebyinv import ChebyInv
from aprox.cauer import Cauer
from aprox.legendre import Legendre

mag_aprox = \
    {"Butterworth": Butter,
    "Chebycheff": Cheby,
    "Chebycheff inverso": ChebyInv,
    "Cauer": Cauer,
    "Legendre": Legendre}

pha_aprox = [
    "Bessel"
]
