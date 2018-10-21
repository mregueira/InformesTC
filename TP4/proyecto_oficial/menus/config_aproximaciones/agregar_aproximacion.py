import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import Progressbar
import tkinter
from threading import Thread

from aprox.reference import mag_aprox, pha_aprox

import config
from data import *
from utils import random_color


class InfoMenu(ttk.Frame):
    def __init__(self, container):
        super(InfoMenu, self).__init__(container)
        self.total = 0

        self.texts = dict()

        self.addText("Valor de N minimo: ")
        self.addText("Valor de Q minimo: ")


    def addText(self, title):
        Label(self, text=title, font=data.myFont2, height=2, width=25).grid(column=0, row=self.total)
        self.texts[title] = Label(self, text="5", font=data.myFont2, height=2, width=25)
        self.texts[title].grid(column=1, row=self.total)

        self.total += 1

    def updateValue(self, textTitle, value):
        self.texts[textTitle]['text'] = value


class OptionsMenu(ttk.Frame):
    def __init__(self, container, mode = "mag"):
        super(OptionsMenu, self).__init__(container)

        self.bars = dict()
        self.total = 0

        self.addBar("Q Máximo", 0, 100)
        if mode == "mag":
            self.addBar("Denormalización", 0, 100)
        self.addBar("N mínimo", 1, 20)
        self.addBar("N máximo", 1, 20)

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
    optionMenu = None

    def __init__(self, tabControl, session_data, tableReference):
        super(AgregarAproximacionMenu, self).__init__(tabControl)
        self.session_data = session_data
        self.tableReference = tableReference

        self.leftFrame = ttk.Frame(self)
        self.rightFrame = ttk.Frame(self)

        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_columnconfigure(1, weight=1, uniform="group1")

        self.var = StringVar()

        self.downFrame = ttk.Frame(self, height=40)

        self.downFrame.pack(side=BOTTOM, fill=X, expand=False)



        self.leftFrame.pack(side=LEFT, fill=X)
        self.rightFrame.pack(side=LEFT, fill=BOTH, expand=1)

        self.bind("<Visibility>", self.onVisibility)
        self.cont = dict()

        self.last = None

    def addButtonCommit(self):
        self.cont["commitButton"] = Button(self.downFrame, height=1, width=10, text="Agregar aproximación",
                                   command=lambda: self.retrieve_input(), font=data.myFont,
                                   background="dark sea green")
        # command=lambda: retrieve_input() >>> just means do this when i press the button
        self.cont["commitButton"].pack(side=TOP, fill=BOTH)

    def destroyButtonCommit(self):
        self.cont["commitButton"].destroy()

    def addLoadingBar(self):
        self.cont["progress"] = Progressbar(self.downFrame, orient=HORIZONTAL,
                                    length=100, mode='determinate',
                                    style="red.Horizontal.TProgressbar")
        self.cont["progress"].pack(side=TOP, fill=BOTH, expand=1)

    def destroyLoadingBar(self):
        self.cont["progress"].destroy()

    def addMagButtons(self):
        for aprox in mag_aprox.keys():
            self.cont[aprox] = Radiobutton(self.leftFrame,
                            text=aprox,
                            indicatoron=0,
                            width=20,
                            font=data.myFont3,
                            variable=self.var,
                            command=self.showChoice,
                            background="cyan2",
                            selectcolor="cyan4",
                            value=aprox)
            self.cont[aprox].pack(fill=BOTH, expand=1)

    def addPhaseButtons(self):
        for aprox in pha_aprox.keys():
            self.cont[aprox] = Radiobutton(self.leftFrame,
                        text=aprox,
                        indicatoron=0,
                        width=20,
                        font=data.myFont3,
                        variable=self.var,
                        command=self.showChoice,
                        background="cyan2",
                        selectcolor="cyan4",
                        value=aprox)
            self.cont[aprox].pack(fill=BOTH, expand=1)

    def retrieve_input(self):
        if config.debug:
            print("Agregando aproximacion")

        self.session_data.topBar.updateText("Agregando aproximacion ...")

        plotData = dict()

        plotData["Q"] = self.cont["optionMenu"].bars["Q Máximo"]["slide"].get()
        plotData["maxN"] = self.cont["optionMenu"].bars["N máximo"]["slide"].get()
        plotData["minN"] = self.cont["optionMenu"].bars["N mínimo"]["slide"].get()
        if self.last == "magnitud":
            plotData["D"] = self.cont["optionMenu"].bars["Denormalización"]["slide"].get()
        plotData["aprox"] = self.var

        if config.debug:
            print(plotData)

        self.destroyButtonCommit()
        self.addLoadingBar()
        thread = Thread(target=self.computarAproximacion, args= (plotData, ))
        thread.start()

    def onVisibility(self, event):
        # Actualización cuando el tab es abierto

        if not self.session_data.plantilla:
            if self.last != "none":
                for k in self.cont.keys():
                    self.cont[k].destroy()

                self.cont["labelNothing"] = Label(self.rightFrame,text="No fue seleccionada ninguna plantilla", font=data.myFont2)
                self.cont["labelNothing"].pack(side=LEFT, expand=1, fill=X)
                self.last = "none"

            return 0

        if self.last == self.session_data.plantilla.type:
            return 0

        for k in self.cont.keys():
            self.cont[k].destroy()

        if self.session_data.plantilla.type == "magnitud":

            self.cont["plantillaTitle"] = Label(self.rightFrame, text="Necesidades de plantilla", font=data.myFont)
            self.cont["plantillaTitle"].pack(side=TOP, fill=X, expand=1)
            self.cont["infoMenu"] = InfoMenu(self.rightFrame)
            self.cont["infoMenu"].pack(side=TOP, fill=X, expand=1)
            self.cont["configTitle"] = Label(self.rightFrame, text="Configuraciones", font=data.myFont)
            self.cont["configTitle"].pack(side=TOP, fill=X, expand=1)

            self.cont["optionMenu"] = OptionsMenu(self.rightFrame)
            self.cont["optionMenu"].pack(side=TOP, fill=X, expand=1)

            self.addMagButtons()
            self.addButtonCommit()
            self.last = "magnitud"

        elif self.session_data.plantilla.type == "fase":
            self.cont["plantillaTitle"] = Label(self.rightFrame, text="Necesidades de plantilla", font=data.myFont)
            self.cont["plantillaTitle"].pack(side=TOP, fill=X, expand=1)

            self.cont["infoMenu"] = InfoMenu(self.rightFrame)
            self.cont["infoMenu"].pack(side=TOP, fill=X, expand=1)

            self.cont["optionMenu"] = OptionsMenu(self.rightFrame, "pha")
            self.cont["optionMenu"].pack(side=TOP, fill=X, expand=1)

            self.addPhaseButtons()
            self.addButtonCommit()

            self.last = "fase"

    def computarAproximacion(self, plotData):
        if config.debug:
            print("empezamos el thread")
        plotData["aprox"] = self.var.get()

        minN = plotData["minN"]
        maxN = plotData["maxN"]

        for i in range(minN, maxN+1):
            plotData["minN"] = i
            plotData["maxN"] = i
            plotData["color"] = random_color()
            number = self.session_data.addPlot(plotData.copy(), self.updateStatusFunc)

            plotData["number"] = number

            self.tableReference.addItem(number, self.var.get(), i, plotData["Q"],
                                        plotData["color"])

        n_values = str(minN) + "-" + str(maxN)

        self.session_data.topBar.setSucessText("Aproxmacion agregada: "+self.var.get()+" n=" + n_values )
        if config.debug:
            print("Terminamos el thread")

        self.destroyLoadingBar()
        self.addButtonCommit()

    def updateStatusFunc(self, value):
        self.cont["progress"]["value"] = value

    def showChoice(self):
        min_n = mag_aprox[self.var.get()](self.session_data.plantilla).getMinNValue()
        if min_n == -1:
            min_n = "Not available"
        else:
            min_n = str(min_n)

        self.cont["infoMenu"].updateValue("Valor de N minimo: ", min_n)

