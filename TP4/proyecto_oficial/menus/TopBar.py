import tkinter.ttk as ttk
import config
from tkinter import *
import data


class TopBar(ttk.Frame):
    def __init__(self, frame):
        super(TopBar, self).__init__(frame)
        if config.debug:
            print("Inicializando top bar")

        self.w = Label(self, text="Filtro: Pasa bajos - Butterworth", fg="black",font=data.data.myFont2)
        self.w.pack(padx=0, pady=0, side=LEFT)

