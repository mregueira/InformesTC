import tkinter.ttk as ttk
import config
from tkinter import *
import data


class TopBar(ttk.Frame):
    aproximacion = "Butter"
    filtro = ""

    def __init__(self, frame):
        super(TopBar, self).__init__(frame)
        if config.debug:
            print("Inicializando top bar")

        self.w = Label(self, text="Filtro: Pasa bajos - Butterworth", fg="black", font=data.data.myFont2)
        self.w.pack(fill=X, expand=1, side=TOP)

        self.notSelected()

    def notSelected(self):
        self.updateText("Ninguna aproximación seleccionada")

    def updateAproximacion(self, title):
        self.aproximacion = title
        self.updateText("Filtro: "+self.filtro+" - "+self.aproximacion)

    def updateFiltro(self, filtro):
        self.filtro = filtro
        self.updateText("Filtro: "+self.filtro+" - "+self.aproximacion)

    def updateText(self, title):
        self.w.configure(text=title, bg="AntiqueWhite1")

    def setErrorText(self, title):
        self.w.configure(text=title, bg="chocolate1")

    def setSucessText(self, title):
        self.w.configure(text=title, bg="spring green")
