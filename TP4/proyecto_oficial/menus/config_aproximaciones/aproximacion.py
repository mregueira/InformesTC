import tkinter.ttk as ttk
import config
from tkinter import *
from menus.config_aproximaciones.agregar_aproximacion import AgregarAproximacionMenu
from menus.config_aproximaciones.aproximacion_tabla import AproximacionTabla


class AproximacionMenu(ttk.Frame):
    def __init__(self, tabControl, session_data):
        super(AproximacionMenu, self).__init__(tabControl)

        self.session_data = session_data
        self.tabControlB = ttk.Notebook(self)
        self.tabControlB.pack(expand=1, side=LEFT, fill=BOTH)

        self.tab2 = AproximacionTabla(self.tabControlB, session_data)
        self.tab1 = AgregarAproximacionMenu(self.tabControlB, session_data, self.tab2)

        self.addTab("AGREGAR", self.tab1)
        self.addTab("TABLA", self.tab2)

    def addTab(self, title, tabObject):
        if config.debug:
            print("Adding tab, title=", title)

        self.tabControlB.add(tabObject, text=title)

