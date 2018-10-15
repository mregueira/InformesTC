import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import Progressbar

import tkinter
from threading import Thread

from aprox import mag_aprox, butter
import config
from data import *
from utils import random_color

class InfoMenu(ttk.Frame):
    def __init__(self, container):
        super(InfoMenu, self).__init__(container)
        self.total = 0

        self.addText("Valor de N minimo: ")
        self.addText("Valor de Q minimo: ")

    def addText(self, title):
        Label(self, text=title, font=data.myFont2, height=2, width=25).grid(column=0, row=self.total)
        Label(self, text="5", font=data.myFont2, height=2, width=25).grid(column=1, row=self.total)
        self.total += 1


class OptionsMenu(ttk.Frame):
    def __init__(self, container):
        super(OptionsMenu, self).__init__(container)

        self.bars = dict()
        self.total = 0

        self.addBar("Q Máximo", 0, 100)
        self.addBar("Denormalización", 0, 100)
        self.addBar("N mínimo", 1, 100)
        self.addBar("N máximo", 1, 100)

    def addBar(self, title, min_value, max_value):
        barTitle = Label(self, text=title, font=data.myFont2, width=25, height=2).grid(column=0, row=self.total)
        barSlide = Scale(self, from_=min_value, to=max_value, orient=HORIZONTAL
                             , background="dodger blue",
                             troughcolor="blue",
                             width=20,
                             font=data.myFont2, length=300)
        barSlide.grid(column=1, row=self.total)
        self.total += 1

        self.bars[title] = {"title": barTitle, "slide": barSlide}


class AgregarAproximacionMenu(ttk.Frame):
    def __init__(self, tabControl, session_data, tableReference):
        super(AgregarAproximacionMenu, self).__init__(tabControl)
        self.session_data = session_data
        self.tableReference = tableReference

        self.leftFrame = ttk.Frame(self)
        self.rightFrame = ttk.Frame(self)

        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_columnconfigure(1, weight=1, uniform="group1")

        self.var = StringVar()

        for aprox in mag_aprox:
            Radiobutton(self.leftFrame,
                            text=aprox,
                            indicatoron=0,
                            width=20,
                            font=data.myFont3,
                            variable=self.var,
                            command=self.showChoice,
                            background="cyan2",
                            selectcolor="cyan4",
                            value=aprox).pack(fill=BOTH, expand=1)

        Label(self.rightFrame, text="Necesidades de plantilla", font=data.myFont).pack(side=TOP, fill=X, expand=1)
        InfoMenu(self.rightFrame).pack(side=TOP, fill=X, expand=1)
        Label(self.rightFrame, text="Configuraciones", font=data.myFont).pack(side=TOP, fill=X, expand=1)

        self.optionMenu = OptionsMenu(self.rightFrame)
        self.optionMenu.pack(side=TOP, fill=X, expand=1)

        self.downFrame = ttk.Frame(self, height=40)

        self.downFrame.pack(side=BOTTOM, fill=X, expand=False)

        self.addButtonCommit()

        self.leftFrame.pack(side=LEFT, fill=X)
        self.rightFrame.pack(side=LEFT, fill=BOTH, expand=1)


    def addButtonCommit(self):
        self.buttonCommit = Button(self.downFrame, height=1, width=10, text="Agregar aproximación",
                                   command=lambda: self.retrieve_input(), font=data.myFont,
                                   background="dark sea green")
        # command=lambda: retrieve_input() >>> just means do this when i press the button
        self.buttonCommit.pack(side=TOP, fill=BOTH)

    def destroyButtonCommit(self):
        self.buttonCommit.destroy()

    def addLoadingBar(self):
        self.progress = Progressbar(self.downFrame, orient=HORIZONTAL,
                                    length=100, mode='determinate',
                                    style="red.Horizontal.TProgressbar")
        self.progress.pack(side=TOP, fill=BOTH, expand=1)

    def destroyLoadingBar(self):
        self.progress.destroy()

    def retrieve_input(self):
        if config.debug:
            print("Agregando aproximacion")

        self.session_data.topBar.updateText("Agregando aproximacion ...")


        plotData = dict()

        plotData["Q"] = self.optionMenu.bars["Q Máximo"]["slide"].get()
        plotData["maxN"] = self.optionMenu.bars["N máximo"]["slide"].get()
        plotData["minN"] = self.optionMenu.bars["N mínimo"]["slide"].get()
        plotData["D"] = self.optionMenu.bars["Denormalización"]["slide"].get()
        plotData["color"] = random_color()

        if config.debug:
            print(plotData)

        self.destroyButtonCommit()
        self.addLoadingBar()
        thread = Thread(target= self.computarAproximacion, args = (plotData, ))
        thread.start()

    def computarAproximacion(self, plotData):
        if config.debug:
            print("empezamos el thread")
        number = self.session_data.addPlot(plotData, self.updateStatusFunc)

        plotData["number"] = number

        plotData["aprox"] = "Butter"

        self.tableReference.addItem(number, "Butter", plotData["minN"], plotData["maxN"], plotData["Q"],
                                    plotData["color"])

        n_values = str(plotData["minN"]) + "-" + str(plotData["maxN"])

        self.session_data.topBar.setSucessText(
            "Aproxmacion agregada: Butter n=" + n_values )
        if config.debug:
            print("Terminamos el thread")

        self.destroyLoadingBar()
        self.addButtonCommit()

    def updateStatusFunc(self, value):
        self.progress["value"] = value

    def showChoice(self):
        pass

