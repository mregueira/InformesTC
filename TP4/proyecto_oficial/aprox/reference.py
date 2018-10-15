

from aprox.butter import Butter
from aprox.cheby import Cheby

mag_aprox = \
    {"Butterworth": Butter,
    "Chebycheff": Cheby,
    "Chebycheff inverso": None,
    "Cauer": None,
    "Legendre": None}


pha_aprox = [
    "Bessel"
]
