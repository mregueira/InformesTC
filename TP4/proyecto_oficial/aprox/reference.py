

from aprox.butter import Butter
from aprox.cheby import Cheby
from aprox.chebyinv import ChebyInv
from aprox.legendre import Legendre
from aprox.bessel import Bessel

mag_aprox = \
    {"Butterworth": Butter,
    "Chebycheff": Cheby,
    "Chebycheff inverso": ChebyInv,
    "Cauer": None,
    "Legendre": Legendre}


pha_aprox = {
    "Bessel": Bessel,
    "Gauss": None
}
