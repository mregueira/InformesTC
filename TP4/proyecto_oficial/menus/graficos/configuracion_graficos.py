import tkinter.ttk as ttk
import config
from tkinter import *
from data import *
from utils import round_to_1

buttonList = [
    "Atenuación",
    "Ganancia",
    "Fase",
    "Polos y ceros",
    "Retardo de grupo",
    "Respuesta al impulso",
    "Respuesta al escalón",
    "Gráfico Q",
    "Desactivar"
]


class SubMenu(ttk.Frame):
    #Clase para el meno en el que se configura que graficos mostrar

    def __init__(self, container):
        super(SubMenu, self).__init__(container)
        self.var = dict()
        self.widgets = []

        self.topFrame = ttk.Frame(self)

        Label(self.topFrame, text="Ajustes", width=40, font=data.myFont).pack(side=TOP, fill=BOTH, expand=1)

        self.topFrame.pack(side=TOP, fill=BOTH, expand=1)

        self.downFrame = ttk.Frame(self)

        self.downFrame.pack(side=TOP, fill=BOTH, expand=1)
        self.total = 1

    def addTickBox(self, title):
        # Agregar un tickbox en el menu
        self.var[title] = IntVar()
        c = Checkbutton(self.topFrame, text=title, variable=self.var[title], width=20, font=data.myFont2)
        c.pack(side=TOP, fill=X, expand=1)

        self.widgets.append(c)

    def addSlider(self, title, min_value, max_value):
        # Agregar un slider en el menu
        label = Label(self.downFrame, text=title, font=data.myFont2, width=20, height=2)
        label.grid(column=0, row=self.total)
        self.var[title] = IntVar()
        barSlide = Scale(self.downFrame, from_=min_value, to=max_value, orient=HORIZONTAL
                         , background="dodger blue",
                         variable = self.var[title],
                         troughcolor="blue",
                         width=20,
                         font=data.myFont2, length=300)

        barSlide.grid(column=1, row=self.total)
        self.widgets.append(label)
        self.widgets.append(barSlide)

        self.total += 1

    def addTextInput(self, title, default_text):
        # Agregar un text input en el menu
        label = Label(self.downFrame, text=title, font=data.myFont2, width=30, height=2)
        label.grid(column=0, row=self.total)

        text = Text(self.downFrame, width=20, height=1, font=data.myFont2, background="peach puff")
        text.delete(1.0, 'end-1c')
        text.insert('end-1c', default_text)

        text.grid(column=1, row=self.total)

        self.var[title] = text

        self.widgets.append(label)
        self.widgets.append(text)

        self.total += 1

    def eraseWidgets(self):
        for w in self.widgets:
            w.destroy()
        self.widgets = []


class ConfiguracionGraficos(ttk.Frame):
    # Menu para configurar los graficos
    def __init__(self, container, session_data, plotReference):
        super(ConfiguracionGraficos, self).__init__(container)

        self.plotReference = plotReference
        self.session_data = session_data
        self.leftFrame = ttk.Frame(self)
        self.rightFrame = ttk.Frame(self)
        self.var = StringVar()

        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_columnconfigure(1, weight=1, uniform="group1")

        for mode in buttonList:
            Radiobutton(self.leftFrame,
                            text=mode,
                            indicatoron=0,
                            width=20,
                            font=data.myFont3,
                            variable=self.var,
                            command=self.showChoice,
                            background="cyan2",
                            selectcolor="cyan4",
                            value=mode).pack(fill=BOTH, expand=1)

        self.menu = SubMenu(self.rightFrame)
        self.menu.pack(side=TOP, fill=X, expand=1)

        buttonCommit = Button(self, height=1, width=10, text="Aplicar",
                              command=lambda: self.retrieve_input(), font=data.myFont,
                              background="dark sea green")
        # command=lambda: retrieve_input() >>> just means do this when i press the button
        buttonCommit.pack(side=BOTTOM, fill=BOTH)

        self.leftFrame.pack(side=LEFT, expand=1, fill=X)
        self.rightFrame.pack(side=LEFT, expand=1, fill=BOTH)

    def retrieve_input(self):
        # Actualizamos los graficos seleccionados a los datos de session
        if config.debug:
            print("Agregando grafico")

        if self.var.get() == "Ganancia":
            data = self.classicalPlotValidation()
            if not data:
                return 0
            mode, min_freq, max_freq = data

            self.plotReference.plotMagnitud("ganancia", 1, float(min_freq), float(max_freq), mode)
        elif self.var.get() == "Atenuación":
            data = self.classicalPlotValidation()
            if not data:
                return 0
            mode, min_freq, max_freq = data

            self.plotReference.plotMagnitud("atenuacion", 1, float(min_freq), float(max_freq), mode)

        elif self.var.get() == "Fase":
            data = self.classicalPlotValidation()
            if not data:
                return 0
            mode, min_freq, max_freq = data

            self.plotReference.plotMagnitud("fase", 1, float(min_freq), float(max_freq), mode)

        elif self.var.get() == "Polos y ceros":
            self.plotReference.plotPolesAndZeros()

        elif self.var.get() == "Retardo de grupo":
            data = self.classicalPlotValidation()
            if not data:
                return 0
            mode, min_freq, max_freq = data
            self.plotReference.plotMagnitud("retardo de grupo", 1, float(min_freq), float(max_freq), mode)

        elif self.var.get() == "Respuesta al impulso":
            data = self.classicalPlotValidationTime()
            if not data:
                return 0
            mode, min_t, max_t = data
            self.plotReference.plotRtaImpulso( float(min_t), float(max_t), mode)
        elif self.var.get() == "Respuesta al escalón":
            data = self.classicalPlotValidationTime()
            if not data:
                return 0
            mode, min_t, max_t = data
            self.plotReference.plotRtaEscalon( float(min_t), float(max_t), mode)
        elif self.var.get() == "Gráfico Q":
            self.plotReference.plotQ()

        self.session_data.topBar.setSucessText("Graficando " + self.var.get())



    def classicalPlotValidation(self):
        regnumber = re.compile(r'^\d+(?:.\d*)?$')

        min_freq = self.menu.var["Frecuencia mínima (hz)"].get("1.0", 'end-1c')
        max_freq = self.menu.var["Frecuencia máxima (hz)"].get("1.0", 'end-1c')
        if not regnumber.match(min_freq):
            self.session_data.topBar.setErrorText("Entrada invalida")
            return None
        if not regnumber.match(max_freq):
            self.session_data.topBar.setErrorText("Entrada invalida")
            return None

        if max_freq < min_freq:
            self.session_data.topBar.setErrorText("Entrada invalida")
            return None

        if self.menu.var["Escala lineal"].get():
            mode = "lineal"
        else:
            mode = "log"
        return mode, min_freq, max_freq

    def classicalPlotValidationTime(self):
        regnumber = re.compile(r'^\d+(?:.\d*)?$')

        min_t = self.menu.var["Tiempo mínimo (s)"].get("1.0", 'end-1c')
        max_t = self.menu.var["Tiempo máximo (s)"].get("1.0", 'end-1c')
        if not regnumber.match(min_t):
            self.session_data.topBar.setErrorText("Entrada invalida")
            return None
        if not regnumber.match(max_t):
            self.session_data.topBar.setErrorText("Entrada invalida")
            return None
        if max_t < min_t:
            self.session_data.topBar.setErrorText("Entrada invalida")
            return None
        if self.menu.var["Escala lineal"].get():
            mode = "lineal"
        else:
            mode = "log"
        return mode, min_t, max_t

    def showChoice(self):
        # Actualizamos el menu mostrado segun el boton de tipo de grafico que se presiono
        if self.session_data.plantilla:
            default_freq = self.session_data.plantilla.getDefaultFreqRange()
            min_freq = str(round_to_1(float(default_freq[0])))
            max_freq = str(round_to_1(float(default_freq[-1])))
        else:
            if config.debug:
                print("No hay plantilla seleccionada")
            min_freq = 1
            max_freq = 10

        self.menu.eraseWidgets()
        if self.var.get() == "Atenuación":
            self.menu.addTickBox("Mostrar plantilla")
            self.menu.addTickBox("Escala lineal")
            self.menu.addTextInput("Frecuencia mínima (hz)", min_freq)
            self.menu.addTextInput("Frecuencia máxima (hz)", max_freq)

        elif self.var.get() == "Ganancia":
            self.menu.addTickBox("Mostrar plantilla")
            self.menu.addTickBox("Escala lineal")
            self.menu.addTextInput("Frecuencia mínima (hz)", min_freq)
            self.menu.addTextInput("Frecuencia máxima (hz)", max_freq)

        elif self.var.get() == "Fase":
            self.menu.addTextInput("Frecuencia mínima (hz)", min_freq)
            self.menu.addTextInput("Frecuencia máxima (hz)", max_freq)

        elif self.var.get() == "Polos y ceros":
            pass

        elif self.var.get() == "Retardo de grupo":
            self.menu.addTextInput("Frecuencia mínima (hz)", min_freq)
            self.menu.addTextInput("Frecuencia máxima (hz)", max_freq)

            self.menu.addTickBox("Escala lineal")

        elif self.var.get() == "Respuesta al impulso":
            self.menu.addTextInput("Tiempo mínimo (s)", min_freq)
            self.menu.addTextInput("Tiempo máximo (s)", max_freq)

            self.menu.addTickBox("Escala lineal")
        elif self.var.get() == "Respuesta al escalón":
            self.menu.addTextInput("Tiempo mínimo (s)", min_freq)
            self.menu.addTextInput("Tiempo máximo (s)", max_freq)

            self.menu.addTickBox("Escala lineal")

        elif self.var.get() == "Gráfico Q":
            pass



