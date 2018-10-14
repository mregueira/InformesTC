import tkinter.ttk as ttk

import matplotlib, sys
matplotlib.use('TkAgg')
from scipy import signal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
import config
from tkinter import *
from menus.configuracion_graficos import ConfiguracionGraficos
import matplotlib.pyplot as plt


class Graficos(ttk.Frame):
    def __init__(self, tabControl):
        super(Graficos, self).__init__(tabControl)

        if config.debug:
            print("Inicializando graficos")


        self.tabMenu = ttk.Notebook(self)
        self.tabMenu.pack(expand=1, side=LEFT, fill=BOTH)

        self.tab1 = ConfiguracionGraficos(self)
        self.tab2 = ConfiguracionGraficos(self)
        self.tab3 = ttk.Frame()

        self.addTab("GRÁFICO 1", self.tab1)
        self.addTab("GRÁFICO 2", self.tab2)

        self.addTab("VISTA", self.tab3)

        # graph = Canvas(self)
        # graph.pack(side=TOP, padx=2, pady=4, fill=BOTH, expand=1)
        #
        # f, self.axis = plt.subplots()
        #
        # self.sys = signal.TransferFunction([1], [1, 1])
        # self.w, self.mag, self.phase = signal.bode(self.sys)
        # self.stepT, self.stepMag = signal.step(self.sys)
        # self.impT, self.impMag = signal.impulse(self.sys)
        #
        # self.dataPlot = FigureCanvasTkAgg(f, master=graph)
        # self.dataPlot.draw()
        #
        # self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        # nav = NavigationToolbar2Tk(self.dataPlot, self)
        #
        # nav.update()
        # self.dataPlot._tkcanvas.pack(side=TOP, fill=X, expand=True)

    def addTab(self, title, tabObject):
        if config.debug:
            print("Adding tab, title=", title)

        self.tabMenu.add(tabObject, text=title)

    def setPlotData(self, data):
        plt.cla()

        self.axis.semilogx(data["f"], data["mag"])

        self.axis.grid(color='grey', linestyle='-', linewidth=0.1)
        self.axis.set_xlabel("$f (Hz)$")
        self.axis.set_ylabel("$H(s) (dB)$")
        self.dataPlot.draw()

