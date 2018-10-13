# En este modulo estarán programadas todas las aproximaciones


# Listado de aproximaciones disponibles
mag_aprox = [
    "Butterworth",
    "Chebycheff",
    "Chebycheff inverso",
    "Cauer",
    "Legendre"
]

pha_aprox = [
    "Bessel"
]


class Aprox:
    def __init__(self):
        self.f = None
        self.mag = None
        self.phase = None

    def computar(self, freq_range, n=-1):
        pass
