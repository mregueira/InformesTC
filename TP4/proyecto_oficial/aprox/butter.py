import aprox
from math import pi
from cmath import exp


class Butter(aprox.Aprox):
    def __init__(self, plantilla):
        super(Butter, self).__init__(plantilla)

    def getPoles(self, n):
        poles = []
        for k in range(1, n+1):
            poles.append(exp(1j * (2 * k + n - 1) * (pi / (2 * n))))

        return poles
