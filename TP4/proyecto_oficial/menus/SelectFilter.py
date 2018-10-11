

# Menu para seleccionar cual tipo de filtro se calculará
import config
import tkinter.ttk as ttk
from tkinter import Button,PhotoImage, StringVar, OptionMenu
from data import *
import tkinter
from tkinter import *


class SelectFilterMenu(ttk.Frame):
    def __init__(self, tabControl, updateFiltro, updatePlot):
        self.updateFiltro = updateFiltro
        self.updatePlot = updatePlot
        super(SelectFilterMenu, self).__init__(tabControl)
        self.tabControl = tabControl
        if config.debug:
            print("Inicializando menu de tipo de filtro")

        # filtros = \
        #     [
        #         {"name": "Pasa bajo",
        #          "img": data.pb},
        #         {"name": "Pasa alto",
        #          "img": data.pa}
        #     ]
        #
        # for filtro in filtros:
        #     print(filtro)
        #     button = Button(self)
        #     button.config(image=filtro["img"], activebackground="black", background="black")
        #     button.pack(side=tkinter.TOP, pady=100)

        self.inputs = dict()

        self.rightFrame = ttk.Frame(self)
        self.leftFrame = ttk.Frame(self)

        self.var = tkinter.IntVar()
        self.var.set(1)

        languages = [
            ("Pasa bajos", 1),
            ("Pasa altos", 2),
            ("Pasa bandas", 3),
            ("Rechaza bandas", 4)
        ]

        #frameSelect = tkinter.Frame(self)


        for lang in languages:
            language, val = lang
            tkinter.Radiobutton(self,
                            text=language,
                            indicatoron=0,
                            width=20,
                            font=data.myFont3,
                            variable=self.var,
                            command=self.ShowChoice,
                            background="cyan2",
                            selectcolor="cyan4",
                            value=val).pack(fill=BOTH, expand=1)
        #frameSelect.pack(side=TOP, anchor=CENTER)

        #self.addLabelFrame("Fa")
        #self.addLabelFrame("Fp")
        #self.addLabelFrame("Aa")
        #self.addLabelFrame("Ap")

        buttonCommit = Button(self, height=1, width=10, text="Aplicar",
                              command=lambda: self.retrieve_input(), font=data.myFont)
        # command=lambda: retrieve_input() >>> just means do this when i press the button
        buttonCommit.pack(side=BOTTOM, pady=5)

        self.leftFrame.pack(side=LEFT, padx=100)
        self.rightFrame.pack(side=RIGHT, padx=100)

    def ShowChoice(self):
        #print(self.var.get())
        pass

    def addLabelFrame(self, title):
        labelframe = LabelFrame(self.rightFrame, text=title)
        labelframe.pack(side=TOP, padx=30, expand="yes", fill="both")

        left = Text(labelframe, height=1, width=10, font=data.myFont)
        left.pack()
        self.inputs[title] = left

    def retrieve_input(self):
        self.updateFiltro(str(self.var.get()))
        data = dict()
        data["filter"] = str(self.var.get())
        data["aprox"] = "butter"

        #self.updatePlot(data)

    def onChange(self, v):
        print("change")

