from math import pi, sqrt
import config

# Esta plantilla sirve para filtros que tengan restricciones sobre la atenuacion
# Cumple la funcion de recopilar los datos, y colocarlos de manera comoda para su uso
# Tambien se encarga de las sustituciones algebraicas para las denormalizaciones,
# que son comunes a todas las aproximaciones de magnitud


class PlantillaMagnitud:
    f0 = None
    w0 = None
    b = None
    deltaFa = None
    deltaFp = None
    denorm = None

    def __init__(self, data):
        self.data = data

        if config.debug:
            print("Inicializando plantilla con data = ",data)
        if data["type"] == "pb":
            self.wan = data["fp"] / data["fa"]
            self.wpn = 1
            self.wa = data["fa"] * 2 * pi
            self.wp = data["fp"] * 2 * pi

        elif data["type"] == "pa":
            self.wan = data["fa"] / data["fp"]
            self.wpn = 1
            self.wa = data["fa"] * 2 * pi
            self.wp = data["fp"] * 2 * pi

        elif data["type"] == "bp":
            self.calcularDatos2doOrden(data)
            self.ajustarAsimetria()

            self.wan = self.deltaFa / self.deltaFp

        elif data["type"] == "br":
            self.calcularDatos2doOrden(data)
            self.ajustarAsimetria()

            self.wan = self.deltaFa / self.deltaFp

        else:
            print("Plantilla de magnitud llamada erroneamente")

    def ajustarAsimetria(self):
        # Se ajusta en caso de que el filtro pasabanda o rechaza banda no cumpla
        # simetria geometrica

        fa_mas = self.w0 / self.data["fa-"]
        fa_menos = self.w0 / self.data["fa+"]

        if fa_mas < self.data["fa+"]:
            self.data["fa+"] = fa_mas
        else:
            self.data["fa-"] = fa_menos

    def calcularDatos2doOrden(self, data):
        self.deltaFa = data["fa+"] - data["fa-"]
        self.deltaFp = data["fp+"] - data["fp-"]
        self.f0 = sqrt(self.filterData["fp+"] * self.filterData["fp-"])
        self.w0 = self.f0
        self.b = self.deltaFp / self.f0

    def denormalizarFrecuencias(self, exp, s, sn):
        # se inserta un polinomio normalizado expresado en la variable s y se aplica la
        # sustitucion necesaria para la plantilla para la denormalizacion por frecuencaias
        # var: variable simbolica (s)
        return exp.subs(sn, self.getSubsExpression(s))

    def denormalizarAmplitud(self, exp, s, sn, n, tn_wan, denorm= 0):
        # se inserta un polinomino normalizado con ganancia 3db en wp en la variable s y se aplica la denormalizacion
        # de amplitud para tener la ganancia correcta en wp
        # Es necesario insertar el valor de Tn en wan, el cual depende de la aproximacion usada

        return exp.subs(sn, self.getSubsExpressionAmplitude(s, tn_wan, denorm))

    def getSubsExpression(self, s):
        if self.data["type"] == "pb":
            return s / self.wp
        elif self.data["type"] == "pa":
            return self.wp / s
        elif self.data["type"] == "bp":
            return

    def getSubExpressionAmplitude(self, n, tn_wan, denorm):

        xi_1 = sqrt((10 ** (self.data["ap"] / 10)) - 1)
        xi_2 = sqrt(((10 ** (self.data["aa"] / 10)) - 1)/tn_wan**2)

        factor_1 = xi_1 ** (1/n)
        factor_2 = xi_2 ** (1/n)

        max_factor = max(factor_1, factor_2)
        min_factor = min(factor_1, factor_2)

        return (max_factor - min_factor) * (denorm / 100.0) + min_factor
