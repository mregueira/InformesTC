# coding=utf-8

import tkinter.ttk as ttk
from tkinter import *
from utils.gui.button_array import ButtonArray
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from utils import random_color
from utils.algebra import conseguir_tf
from scipy import signal
from numpy import pi
import matplotlib.patches as mpatches


class PlotEtapas(ttk.Frame):
    def __init__(self, container, session_data):
        super(PlotEtapas, self).__init__(container)
        self.session_data = session_data

        self.leftFrame = ttk.Frame(self)
        self.rightFrame = ttk.Frame(self)

        self.buttonArray = ButtonArray(self)
        self.buttonArray.addBlueButton("Graficar fase")
        self.buttonArray.addGreenButton("Graficar magnitud")

        self.buttonArray.pack(side=BOTTOM, fill=X)

        #self.table = ttk.Treeview()
        lb_header = ["Etapa"]

        self.graph = Canvas(self.rightFrame)
        self.table = ttk.Treeview(self.leftFrame, columns=lb_header, show="headings", selectmode='extended')

        for col in lb_header:
            self.table.column(col, anchor="center", width=40)
            self.table.heading(col, text=col.title())

        self.table.pack(side=TOP, fill=BOTH, expand=1)

        self.fig, self.axis = plt.subplots()

        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graph)
        self.dataPlot.draw()

        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.nav = NavigationToolbar2Tk(self.dataPlot, self.rightFrame)
        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=True)

        self.graph.pack(side=TOP, fill=X, expand=1)
        #self.nav.pack(side=BOTTOM, fill=X, expand=1)

        self.leftFrame.pack(side=LEFT, fill=BOTH, expand=1)
        self.rightFrame.pack(side=LEFT, fill=BOTH, expand=1)

        self.bind("<Visibility>", self.onVisibility)

    def addTableItem(self, title):
        self.table.insert('','end', values=[
            title
        ])

    def onVisibility(self, event):
        self.table.delete(*self.table.get_children())
        #self.tableB.delete(*self.tableB.get_children())

        for etapa_key in self.session_data.etapas.keys():
            etapa = self.session_data.etapas[etapa_key]
            self.addTableItem(str(etapa_key+1) )

    def buttonPressed(self, button):
        if button == "Graficar magnitud" or button == "Graficar fase":

            ## Armamos la transferencia de las etapas seleccionadas y graficamos

            plt.cla()
            self.axis.clear()
            self.nav.update()

            plt.minorticks_on()
            plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
            plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

            self.nav.update()

            if len(self.table.get_children()) == 0:
                return 0

            patches = []

            codes = []
            cds = []
            exp = 1

            for itemCode in self.table.selection():
                code = int(self.table.item(itemCode)["values"][0])
                codes.append(self.session_data.etapas[code-1])
                cds.append(code)
                variable = self.session_data.etapas[code-1].var
                exp *= 10**( self.session_data.etapas[code-1].gain / 20.0)

                exp *= self.session_data.etapas[code-1].transfer_expression

            tf = conseguir_tf(exp, variable)

            w, mag, pha = signal.bode(tf, self.session_data.plantilla.getDefaultFreqRange())
            f = [wi / 2 / pi for wi in w]

            col = random_color(self.session_data.parent)
            if button == "Graficar magnitud":
                self.axis.semilogx(f, mag, col)
            else:
                self.axis.semilogx(f, pha, col)
            name = "Etapas"
            for i in range(len(cds)):
                name += " " + str(cds[i])

            patches.append(mpatches.Patch(color=col, label=name))


            self.axis.legend(handles=patches)

            self.dataPlot.draw()
