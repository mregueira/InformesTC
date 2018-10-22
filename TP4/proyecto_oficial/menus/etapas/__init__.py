# coding=utf-8

import tkinter.ttk as ttk
from menus.etapas.select_aprox import *
from menus.etapas.plot_etapas import *
from menus.etapas.select_etapas import *

import config
from tkinter import *




class Etapas(ttk.Frame):
    def __init__(self, container, session_data):
        super(Etapas, self).__init__(container)

        self.session_data = session_data

        self.cont = dict()

        self.tabMenu = ttk.Notebook(self)

        self.tab1 = SelectAprox(self, self.session_data)
        self.tab2 = SelectEtapas(self, self.session_data)
        self.tab3 = PlotEtapas(self, self.session_data)

        self.addTab("APROXIMACIÓN", self.tab1)
        self.addTab("ETAPAS", self.tab2)
        self.addTab("GRÁFICOS", self.tab3)

        self.tabMenu.pack(expand=1, side=LEFT, fill=BOTH)
        #self.tab1 = ConfiguracionGraficos(self, session_data, self.tab3)
        #self.tab2 = ConfiguracionGraficos(self, session_data, self.tab3)


    def addTab(self, title, tabObject):
        if config.debug:
            print("Adding tab, title=", title)

        self.tabMenu.add(tabObject, text=title)
