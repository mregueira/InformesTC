import tkinter.ttk as ttk
from scipy import signal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.patches as mpatches
from tkinter import *
from data import *
import matplotlib.pyplot as plt
import config
from math import pi
from numpy import logspace

class Vista(ttk.Frame):
    def __init__(self, container, session_data):
        super(Vista, self).__init__(container)

        self.session_data = session_data
        self.titleLabel = Label(self, text="Grafico 1", font=data.myFont)
        self.titleLabel.pack(side=TOP, fill=X)
        self.graph = Canvas(self)

        self.fig, self.axis = plt.subplots()

        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graph)
        self.dataPlot.draw()

        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        nav = NavigationToolbar2Tk(self.dataPlot, self)
        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=True)

        self.graph.pack(side=LEFT, expand=1, fill=BOTH)

    def plotMagnitud(self, mode, add_plantilla, f_range= -1):
        if f_range == -1:
            f_range = self.session_data.plantilla.getDefaultFreqRange()

        plt.cla()
        self.axis.clear()

        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

        patches = []

        min_f = 1e18
        max_f = -1e18
        min_amp = 1e18
        max_amp = -1e18

        for item_key in self.session_data.aproximations.keys():
            item = self.session_data.aproximations[item_key]
            if config.debug:
                print("Graficando ganancia, item= ", item["info"])
            for n in range(item["info"]["minN"], item["info"]["maxN"] + 1):
                tf = item["data"][str(n)]
                w_range = [i * 2 * pi for i in f_range]
                w, mag, pha = signal.bode(tf, w_range)
                f = [i / 2 / pi for i in w]

                if mode == "atenuacion":
                    mag = [-i for i in mag]
                    self.axis.semilogx(f, mag, item["info"]["color"])

                for fi in f:
                    max_f = max(max_f, fi)
                    min_f = min(min_f, fi)

                for ai in mag:
                    min_amp = min(min_amp, ai)
                    max_amp = max(max_amp, ai)

            name = item["info"]["aprox"] + " " + str(item["info"]["minN"]) + "-" + str(item["info"]["maxN"])

            patches.append(mpatches.Patch(color=item["info"]["color"], label=name))

        if min_f != -1e18:
            plot_plantilla = self.session_data.plantilla.getPlantillaPoints(
                min_freq=min_f,
                max_freq=max_f,
                min_amp=min_amp,
                max_amp=max_amp
            )
            for ki in plot_plantilla.keys():
                self.axis.semilogx(plot_plantilla[ki][0], plot_plantilla[ki][1], "black")

        self.axis.legend(handles=patches)

        self.axis.set_xlabel("$f (Hz)$")
        self.axis.set_ylabel("$H(s) (dB)$")

        self.dataPlot.draw()
