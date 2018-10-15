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
    "Retraso de grupo",
    "Respuesta al impulso",
    "Respuesta al escalon",
    "Desactivar"
]


class SubMenu(ttk.Frame):
    #Clase para armar menus particulares para graficos

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

    # def addText(self, title):
    #     Label(self.downFrame, text=title, font=data.myFont2, height=2, width=25).grid(column=0, row=self.total)
    #     Label(self.downFrame, text="5", font=data.myFont2, height=2, width=25).grid(column=1, row=self.total)
    #     self.total += 1

    def addTickBox(self, title):
        self.var[title] = IntVar()
        c = Checkbutton(self.topFrame, text=title, variable=self.var[title], width=20, font=data.myFont2)
        c.pack(side=TOP, fill=X, expand=1)

        self.widgets.append(c)

    def addSlider(self, title, min_value, max_value):
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
        if config.debug:
            print("Agregando grafico")

        regnumber = re.compile(r'^\d+(?:.\d*)?$')

        if self.var.get() == "Ganancia":
            min_freq = self.menu.var["Frecuencia mínima (hz)"].get("1.0", 'end-1c')
            max_freq = self.menu.var["Frecuencia máxima (hz)"].get("1.0", 'end-1c')
            if not regnumber.match(min_freq):
                self.session_data.topBar.setErrorText("Entrada invalida")
                return 0
            if not regnumber.match(max_freq):
                self.session_data.topBar.setErrorText("Entrada invalida")
                return 0
            if self.menu.var["Escala lineal"].get():
                mode = "lineal"
            else:
                mode = "log"

            self.plotReference.plotMagnitud("ganancia", 1, float(min_freq), float(max_freq), mode)
        elif self.var.get() == "Atenuación":
            min_freq = self.menu.var["Frecuencia mínima (hz)"].get("1.0", 'end-1c')
            max_freq = self.menu.var["Frecuencia máxima (hz)"].get("1.0", 'end-1c')
            if not regnumber.match(min_freq):
                self.session_data.topBar.setErrorText("Entrada invalida")
                return 0
            if not regnumber.match(max_freq):
                self.session_data.topBar.setErrorText("Entrada invalida")
                return 0
            if self.menu.var["Escala lineal"].get():
                mode = "lineal"
            else:
                mode = "log"

            self.plotReference.plotMagnitud("atenuacion", 1, float(min_freq), float(max_freq), mode)
        self.session_data.topBar.setSucessText("Graficando " + self.var.get())

    def showChoice(self):
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
            self.menu.addTextInput("Frecuencia mánima (hz)", max_freq)

        elif self.var.get() == "Polos y ceros":
            pass


