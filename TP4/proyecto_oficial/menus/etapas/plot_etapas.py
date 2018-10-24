# coding=utf-8

import tkinter.ttk as ttk
from tkinter import *
from utils.gui.button_array import ButtonArray

class PlotEtapas(ttk.Frame):
    def __init__(self, container, session_data):
        super(PlotEtapas, self).__init__(container)
        self.session_data = session_data

        self.leftFrame = ttk.Frame(self)
        self.rightFrame = ttk.Frame(self)

        self.buttonArray = ButtonArray(self)
        self.buttonArray.addBlueButton("Graficar fase")
        self.buttonArray.addGreenButton("Green magnitud")

        self.buttonArray.pack(side=BOTTOM, fill=BOTH, expand=1)

        self.leftFrame.pack(side=LEFT , fill=BOTH, expand=1)
        self.rightFrame.pack(side=LEFT, fill=BOTH, expand=1)





