import tkinter.ttk as ttk
import config
from tkinter import *
from data import *


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
        Label(self, text="Ajustes",width=20, font=data.myFont).pack(fill=BOTH, expand=1)

    def addText(self, title):
        Label(self, text=title, font=data.myFont2, height=2, width=25).grid(column=0, row=self.total)
        Label(self, text="5", font=data.myFont2, height=2, width=25).grid(column=1, row=self.total)
        self.total += 1

    def addTickBox(self):
        self.var["plantilla"] = IntVar()
        c = Checkbutton(self, text="Mostrar plantilla", variable=self.var["plantilla"], width=30, font=data.myFont2)
        c.pack(fill=BOTH, expand=1)
        self.widgets.append(c)

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
        if self.var.get() == "Ganancia":
            self.plotReference.plotGanancia()

    def showChoice(self):
        self.menu.eraseWidgets()
        if self.var.get() == "Atenuación":
            self.menu.addTickBox()
        elif self.var.get() == "Ganancia":
            pass
        elif self.var.get() == "Fase":
            pass
        elif self.var.get() == "Polos y ceros":
            pass


