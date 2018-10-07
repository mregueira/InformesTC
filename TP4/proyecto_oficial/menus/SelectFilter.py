

# Menu para seleccionar cual tipo de filtro se calculará
import config
import tkinter.ttk as ttk
from tkinter import Button,PhotoImage, StringVar, OptionMenu
from data import *
import tkinter
from tkinter import *


class SelectFilterMenu(ttk.Frame):
    def __init__(self, tabControl, updateFiltro):
        self.updateFiltro = updateFiltro
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

        self.rightFrame = ttk.Frame(self)
        self.leftFrame = ttk.Frame(self)

        self.var = StringVar(self)
        self.var.set("Pasa bajos")  # initial value

        self.option = OptionMenu(self.leftFrame, self.var, "Pasa bajos", "Pasa altos", "Pasa banda", "Rechaza banda")
        self.option.pack(side=TOP, expand=YES)

        self.addLabelFrame("Wa")
        self.addLabelFrame("Wp")
        self.addLabelFrame("Aa")
        self.addLabelFrame("Ap")

        buttonCommit = Button(self, height=1, width=10, text="Aplicar",
                              command=lambda: self.retrieve_input(), font=data.myFont)
        # command=lambda: retrieve_input() >>> just means do this when i press the button
        buttonCommit.pack(side=BOTTOM, pady=5)

        self.leftFrame.pack(side=LEFT, padx=100)
        self.rightFrame.pack(side=RIGHT, padx=100)

    def addLabelFrame(self, title):
        labelframe = LabelFrame(self.rightFrame, text=title)
        labelframe.pack(side=TOP, padx=30, expand="yes", fill="both")

        left = Text(labelframe, height=1, width=10, font=data.myFont)
        left.pack()

    def retrieve_input(self):
        self.updateFiltro(str(self.var.get()))

    def onChange(self, v):
        print("change")

