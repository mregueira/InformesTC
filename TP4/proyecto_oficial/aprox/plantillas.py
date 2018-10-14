from math import pi, sqrt
import config

# Esta plantilla sirve para filtros que tengan restricciones sobre la atenuacion
# Cumple la funcion de recopilar los datos, y colocarlos de manera comoda para su uso
# Tambien se encarga de las sustituciones algebraicas para las denormalizaciones,
# que son comunes a todas las aproximaciones de magnitud


class PlantillaMagnitud:
    aa, ap, b, w0, f0 = None, None, None, None, None
    fa0, fa1, fp0, fp1 = None, None, None, None
    deltaFa, deltaFp = None, None
    denorm = None

    def __init__(self, data):
        self.data = data

        if config.debug:
            print("Inicializando plantilla con data = ",data)
        if data["type"] == "pb":
            self.wan = data["fp"] / data["fa"]
            self.wpn = 1
            self.ap = data["ap"]
            self.aa = data["aa"]

            self.wa = data["fa"] * 2 * pi
            self.wp = data["fp"] * 2 * pi

        elif data["type"] == "pa":
            self.wan = data["fa"] / data["fp"]
            self.wpn = 1
            self.ap = data["ap"]
            self.aa = data["aa"]
            self.wa = data["fa"] * 2 * pi
            self.wp = data["fp"] * 2 * pi

        elif data["type"] == "bp":
            self.ap = data["ap"]
            self.aa = data["aa"]

            self.calcularDatos2doOrden(data)
            self.ajustarAsimetria()

            self.wan = self.deltaFa / self.deltaFp

        elif data["type"] == "br":
            self.ap = data["ap"]
            self.aa = data["aa"]

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
            self.fa1 = fa_mas
        else:
            self.data["fa-"] = fa_menos
            self.fa0 = fa_menos

    def calcularDatos2doOrden(self, data):
        self.deltaFa = data["fa+"] - data["fa-"]
        self.deltaFp = data["fp+"] - data["fp-"]
        self.f0 = sqrt(data["fp+"] * data["fp-"])
        self.w0 = self.f0
        self.b = self.deltaFp / self.f0

        self.fa0 = data["fa-"]
        self.fa1 = data["fa+"]
        self.fp0 = data["fp-"]
        self.fp1 = data["fp+"]

    def denormalizarFrecuencias(self, exp, s, sn):
        # se inserta un polinomio normalizado expresado en la variable s y se aplica la
        # sustitucion necesaria para la plantilla para la denormalizacion por frecuencaias
        # var: variable simbolica (s)
        return exp.subs(sn, self.getSubExpression(s))

    def denormalizarAmplitud(self, exp, s, sn, n, tn_wan, denorm= 0):
        # se inserta un polinomino normalizado con ganancia 3db en wp en la variable s y se aplica la denormalizacion
        # de amplitud para tener la ganancia correcta en wp
        # Es necesario insertar el valor de Tn en wan, el cual depende de la aproximacion usada

        return exp.subs(sn, self.getSubExpressionAmplitude(s, n, tn_wan, denorm))

    def getSubExpression(self, s):
        if self.data["type"] == "pb":
            return s / self.wp
        elif self.data["type"] == "pa":
            return self.wp / s
        elif self.data["type"] == "bp":
            return 1 / self.b * (s / self.w0 + self.w0 / s)
        elif self.data["type"] == "br":
            return self.b * 1 / (s / self.w0 + self.w0 / s)

    def getSubExpressionAmplitude(self, s, n, tn_wan, denorm):

        xi_1 = sqrt((10 ** (self.data["ap"] / 10)) - 1)
        xi_2 = sqrt(((10 ** (self.data["aa"] / 10)) - 1)/tn_wan**2)

        factor_1 = xi_1 ** (1/n)
        factor_2 = xi_2 ** (1/n)

        max_factor = max(factor_1, factor_2)
        min_factor = min(factor_1, factor_2)

        factor = (max_factor - min_factor) * (denorm / 100.0) + min_factor

        return s * factor

    def getPlantillaPoints(self, min_freq, max_freq, min_amp, max_amp):
        # Obtener las coordenadas para dibujar la plantilla
        x_points = []
        y_points = []

        x_points_b = []
        y_points_b = []

        if self.data["type"] == "pb":
            x_points = [min_freq, self.wp, self.wp]
            y_points = [self.ap, self.ap, max_amp]

            x_points_b = [self.wa, self.wa, max_freq]
            y_points_b = [min_amp, self.aa, self.aa]
        elif self.data["type"] == "pa":
            x_points = [min_freq, self.wp, self.wp]
            y_points = [self.aa, self.aa, min_amp]

            x_points_b = [self.wa, self.wa, max_freq]
            y_points_b = [max_amp, self.ap, self.ap]
        elif self.data["type"] == "bp":
            x_points = [min_freq, self.fa0, self.fa0, self.fa1, self.fa1, max_freq]
            y_points = [self.aa, self.aa, min_freq, min_freq, self.aa, self.aa]

            x_points_b = [self.fp0, self.fp0, self.fp1, self.fp1]
            y_points_b = [max_amp, self.ap, self.ap, max_amp]

        elif self.data["type"] == "br":
            x_points = [min_freq, self.fp0, self.fp0, self.fp1, self.fp1, max_freq]
            y_points = [self.ap, self.ap, max_amp, max_amp, self.ap, self.ap]

            x_points_b = [self.fa0, self.fa0, self.fa1, self.fa1]
            y_points_b = [min_amp, self.aa, self.aa, min_amp]

        data1 = dict()
        data1["A"] = x_points, y_points
        data1["B"] = x_points_b, y_points_b

        return data1