

# Menu para seleccionar cual tipo de filtro se calculará
import config
import tkinter.ttk as ttk
from tkinter import Button,PhotoImage, StringVar, OptionMenu
from data import *
import tkinter
from tkinter import *


class SelectFilterMenu(ttk.Frame):
    def __init__(self, tabControl):
        super(SelectFilterMenu, self).__init__(tabControl)
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


        var = StringVar(self)
        var.set("Pasa bajos")  # initial value

        option = OptionMenu(self, var, "Pasa bajos", "Pasa altos")
        option.pack(side=TOP, expand=YES)
