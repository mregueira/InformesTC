

from aprox.butter import Butter
from aprox.cheby import Cheby
from aprox.chebyinv import ChebyInv
from aprox.cauer import Cauer
from aprox.legendre import Legendre
from aprox.bessel import Bessel

mag_aprox = \
    {"Butterworth": Butter,
    "Chebycheff": Cheby,
    "Chebycheff inverso": ChebyInv,
    "Cauer": Cauer,
    "Legendre": Legendre}

<<<<<<< HEAD

pha_aprox = {
    "Bessel": Bessel,
    "Gauss": None
}
=======
pha_aprox = [
    "Bessel"
]
>>>>>>> cced17e376fb1068b70cc3308f58a11742a1ef05
