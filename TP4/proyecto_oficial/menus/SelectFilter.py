

# Menu para seleccionar cual tipo de filtro se calculará
import config
import tkinter.ttk as ttk
from tkinter import Button,PhotoImage
import data
import tkinter

filtros = \
    ["Pasa bajo",
     "Pasa alto"]


class SelectFilterMenu(ttk.Frame):
    def __init__(self, tabControl):
        super(SelectFilterMenu, self).__init__(tabControl)
        if config.debug:
            print("Inicializando menu de tipo de filtro")

        for filtro in filtros:
            button = Button(self, text=filtro)
            button.config(image=data.fonts.photo,activebackground="black")
            button.pack(side=tkinter.TOP)
