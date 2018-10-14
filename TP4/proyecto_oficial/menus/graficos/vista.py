import tkinter.ttk as ttk
from scipy import signal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import *
from data import *
import matplotlib.pyplot as plt
import config


class Vista(ttk.Frame):
    def __init__(self, container, session_data):
        super(Vista, self).__init__(container)

        self.session_data = session_data
        self.titleLabel = Label(self, text="Grafico 1", font=data.myFont)
        self.titleLabel.pack(side=TOP,fill=X)
        self.graph = Canvas(self)

        f, self.axis = plt.subplots()

        self.dataPlot = FigureCanvasTkAgg(f, master=self.graph)
        self.dataPlot.draw()

        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        nav = NavigationToolbar2Tk(self.dataPlot, self)
        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=True)

        self.graph.pack(side=LEFT, expand=1, fill=BOTH)

    def plotGanancia(self):
        plt.cla()

        for item_key in self.session_data.aproximations.keys():
            item = self.session_data.aproximations[item_key]
            if config.debug:
                print("Graficando ganancia, item= ", item["info"])
            for n in range(item["info"]["minN"], item["info"]["maxN"] + 1):
                tf = item["data"][str(n)]
                f, mag, pha = signal.bode(tf)

                self.axis.semilogx(f, mag)

        self.axis.set_xlabel("$f (Hz)$")
        self.axis.set_ylabel("$H(s) (dB)$")

        self.dataPlot.draw()
