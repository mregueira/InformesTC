import tkinter.ttk as ttk
from tkinter import *
from aprox import mag_aprox

from data import *


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
        self.addBar("N minimo", 1, 100)
        self.addBar("N maximo", 1, 100)

    def addBar(self, title, min_value, max_value):
        barTitle = Label(self, text=title, font=data.myFont2, width=25, height=2).grid(column=0, row=self.total)
        barSlide = Scale(self, from_=min_value, to=max_value, orient=HORIZONTAL
                             , background="dodger blue",
                             troughcolor="blue",
                             width=20,
                             font=data.myFont2, length=300).grid(column=1, row=self.total)
        self.total += 1

        self.bars[title] = {"title": barTitle, "slide": barSlide}


class AgregarAproximacionMenu(ttk.Frame):
    def __init__(self, tabControl):
        super(AgregarAproximacionMenu, self).__init__(tabControl)

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

        Label(self.rightFrame, text="Necesidades de plantilla", font=data.myFont).pack(side=TOP,fill=X,expand=1)
        InfoMenu(self.rightFrame).pack(side=TOP, fill=X, expand=1)
        Label(self.rightFrame, text="Configuraciones", font=data.myFont).pack(side=TOP, fill=X, expand=1)
        OptionsMenu(self.rightFrame).pack(side=TOP, fill=X, expand=1)

        buttonCommit = Button(self, height=1, width=10, text="Agregar aproximación",
                              command=lambda: self.retrieve_input(), font=data.myFont,
                              background="dark sea green")
        # command=lambda: retrieve_input() >>> just means do this when i press the button
        buttonCommit.pack(side=BOTTOM, fill=BOTH)


        self.leftFrame.pack(side=LEFT, fill=X)
        self.rightFrame.pack(side=LEFT, fill=BOTH, expand=1)


    def retrieve_input(self):
        pass

    def showChoice(self):
        pass

