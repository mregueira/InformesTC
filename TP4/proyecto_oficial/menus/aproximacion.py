import tkinter.ttk as ttk
import config
from tkinter import *
from menus.agregar_aproximacion import AgregarAproximacionMenu
from menus.aproximacion_tabla import AproximacionTabla


class AproximacionMenu(ttk.Frame):
    def __init__(self, tabControl):
        super(AproximacionMenu, self).__init__(tabControl)

        self.tabControlB = ttk.Notebook(self)
        self.tabControlB.pack(expand=1, side=LEFT, fill=BOTH)

        self.tab1 = AgregarAproximacionMenu(self.tabControlB)
        self.tab2 = AproximacionTabla(self.tabControlB)

        self.addTab("AGREGAR", self.tab1)
        self.addTab("TABLA", self.tab2)

    def addTab(self, title, tabObject):
        if config.debug:
            print("Adding tab, title=", title)

        self.tabControlB.add(tabObject, text=title)

