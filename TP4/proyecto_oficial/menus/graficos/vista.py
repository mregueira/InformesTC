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
from numpy import logspace, log10
import numpy as np
from utils.etapas import getSing

class Vista(ttk.Frame):
    # Esta clase es muy importante, aqui se grafican todos los graficos
    def __init__(self, container, session_data):
        super(Vista, self).__init__(container)

        self.session_data = session_data
        self.titleLabel = Label(self, text="Graficos", font=data.myFont)
        self.titleLabel.pack(side=TOP, fill=X)
        self.graph = Canvas(self)

        self.fig, self.axis = self.session_data.fig, self.session_data.axis

        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graph)
        self.dataPlot.draw()

        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.nav = NavigationToolbar2Tk(self.dataPlot, self)
        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=True)

        self.graph.pack(side=LEFT, expand=1, fill=BOTH)

        self.bind("<Visibility>", self.onVisibility)
    def onVisibility(self, event):

        pass

    def setTitulo(self,title):
        self.titleLabel["text"] = title

    def plotMagnitud(self, mode, add_plantilla, min_freq, max_freq, scale = "log"):
        # if f_range == -1:
        #     f_range = self.session_data.plantilla.getDefaultFreqRange()
        if not self.session_data.plantilla:
            return 0

        f_range = logspace(log10(min_freq), log10(max_freq), 10000)

        plt.cla()
        self.axis.clear()
        self.nav.update()

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

            tf = item["data"]["tf"]
            w_range = [i * 2 * pi for i in f_range]
            w, mag, pha = signal.bode(tf, w_range)
            f = [i / 2 / pi for i in w]

            if mode == "fase":
                self.setTitulo("Grafico de Fase (°)")

                y_var = pha
                self.axis.set_xlabel("$f (Hz)$")
                self.axis.set_ylabel("$Fase (°)$")
                if scale == "log":
                    self.axis.semilogx(f, y_var, item["info"]["color"])
                else:
                    self.axis.plot(f, y_var, item["info"]["color"])



            elif mode == "atenuacion" or mode == "ganancia":
                if mode == "atenuacion":
                    self.setTitulo("Grafico de Atenuación en dB")

                    mag = [-i for i in mag]

                y_var = mag
                self.axis.set_xlabel("$f (Hz)$")
                self.axis.set_ylabel("$A(s) (dB)$")
                if scale == "log":
                    self.axis.semilogx(f, y_var, item["info"]["color"])
                else:
                    self.axis.plot(f, y_var, item["info"]["color"])

            elif mode == "ganancia":
                self.setTitulo("Grafico de Ganancia en dB")

                y_var = mag
                self.axis.set_xlabel("$f (Hz)$")
                self.axis.set_ylabel("$H(s) (dB)$")
                if scale == "log":
                    self.axis.semilogx(f, y_var, item["info"]["color"])

                else:
                    self.axis.plot(f, y_var, item["info"]["color"])

            elif mode == "retardo de grupo":
                self.setTitulo("Grafico de Retardo de Grupo")
                y_var = []
                for i in range(1, len(f)):
                    delta_y = (pha[i] - pha[i-1])*pi/180.0
                    delta_x = (f[i] - f[i-1])*2*pi
                    #cociente incremental
                    y_var.append(-delta_y/delta_x*1000.0)

                    self.axis.set_xlabel("$f (Hz)$")
                    self.axis.set_ylabel("$t(w) (ms)$")

                f.pop()

                fdeltas = []
                ydeltas = []
                fnormal = []
                ynormal = []

                for n in range (1,len(y_var)-1):
                    if abs(y_var[n]-y_var[n-1])*50 < abs(y_var[n]-y_var[n+1]):
                        fdeltas.append(f[n+1])
                        ydeltas.append(y_var[n])
                    else:
                        fnormal.append(f[n+1])
                        ynormal.append(y_var[n+1])


                arr = sorted(ynormal)
                ymax = arr[len(arr)-1]
                ymin = arr[0]

                fmax = f[len(f)-1]
                fmin = f[0]


                arrow_length = abs(ymax-ymin)/4
                arrow_width = abs(fmax-fmin)/400


                if scale == "log":
                    self.axis.semilogx(fnormal, ynormal, item["info"]["color"])

                    for j in range(len(fdeltas)):
                        plt.arrow(fdeltas[j], ydeltas[j], 0, -arrow_length,  head_width = arrow_width, head_length = arrow_length/4, length_includes_head = "true")

                else:
                    self.axis.plot(f, y_var, item["info"]["color"])

                    for j in range(len(fdeltas)):
                        plt.arrow(fdeltas[j], ydeltas[j], 0, -arrow_length, head_width=arrow_width,
                                  head_length=arrow_length / 4, length_includes_head="true")


            for fi in f:
                max_f = max(max_f, fi)
                min_f = min(min_f, fi)

            for ai in y_var:
                min_amp = min(min_amp, ai)
                max_amp = max(max_amp, ai)

            name = item["info"]["aprox"] + " " + str(item["data"]["number"])

            patches.append(mpatches.Patch(color=item["info"]["color"], label=name))

        if min_f != -1e18 and mode == "atenuacion" and self.session_data.plantilla.type == "magnitud":

            if mode == "ganancia":
                factor = -1
            else:
                factor = 1

            plot_plantilla = self.session_data.plantilla.getPlantillaPoints(
                min_freq=min_freq,
                max_freq=max_freq,
                min_amp=min_amp,
                max_amp=max_amp
            )
            if add_plantilla:
                for ki in plot_plantilla.keys():
                    mag_new = [factor*i for i in plot_plantilla[ki][1]]

                    if scale == "log":
                        self.axis.semilogx(plot_plantilla[ki][0],  mag_new, "black")
                    else:
                        self.axis.plot(plot_plantilla[ki][0], mag_new, "black")

        if min_f != -1e18 and mode == "retardo de grupo" and self.session_data.plantilla.type == "fase":

            if mode == "ganancia":
                factor = -1
            else:
                factor = 1

            plot_plantilla = self.session_data.plantilla.getPlantillaPoints(
                min_freq=min_freq,
                max_freq=max_freq,
                min_amp=min_amp,
                max_amp=max_amp
            )
            if add_plantilla:
                for ki in plot_plantilla.keys():
                    mag_new = [factor*i for i in plot_plantilla[ki][1]]

                    if scale == "log":
                        self.axis.semilogx(plot_plantilla[ki][0],  mag_new, "black")
                    else:
                        self.axis.plot(plot_plantilla[ki][0], mag_new, "black")


        self.axis.legend(handles=patches)

        self.dataPlot.draw()

    def plotPolesAndZeros(self):
        plt.cla()
        self.axis.clear()

        maxDistance = 0

        patches = []
        self.setTitulo("Grafico de Polos y Ceros")

        for item_key in self.session_data.aproximations.keys():
            item = self.session_data.aproximations[item_key]

            tf = item["data"]["tf"]

            #print("poles = ", p)
            for pi in tf.poles:
                maxDistance = max(maxDistance, abs(pi))
            for pi in tf.zeros:
                maxDistance = max(maxDistance, abs(pi))

            t2 = plt.plot( tf.poles.real,  tf.poles.imag, 'rx', ms=10)
            plt.setp(t2, markersize=12.0, markeredgewidth=3.0,
                     markeredgecolor=item["info"]["color"], markerfacecolor=item["info"]["color"])
            t2 = plt.plot( tf.zeros.real, tf.zeros.imag, 'ro', ms=10)
            plt.setp(t2, markersize=12.0, markeredgewidth=3.0,
                     markeredgecolor=item["info"]["color"], markerfacecolor=item["info"]["color"])
            if "norm" in item["info"]:
                add_text = ""
            else:
                add_text = " " + item["info"]

            name = item["info"]["aprox"] + " " + str(item["data"]["number"]) + add_text
            patches.append(mpatches.Patch(color=item["info"]["color"], label=name))

        uc = mpatches.Circle((0, 0), radius=maxDistance, fill=False,
                             color='black', ls='dashed')
        self.axis.add_patch(uc)
        self.axis.legend(handles=patches)

        self.axis.set_xlim(left = -maxDistance*1.5, right=maxDistance*1.5)
        self.axis.set_ylim(bottom = -maxDistance*1.5, top=maxDistance*1.5)

        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
        plt.gca().set_aspect('equal', adjustable='box')
        #plt.axis('scaled')
        #plt.axis([-r, r, -r, r])
        #ticks = [-1, -.5, .5, 1]

        #plt.xticks(ticks)
        #plt.yticks(ticks)

        self.dataPlot.draw()

    def plotRtaImpulso(self,min_t, max_t,scale = "log"):
        if not self.session_data.plantilla:
            return 0
        plt.cla()
        self.axis.clear()
        self.nav.update()
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
        patches = []
        self.setTitulo("Grafico de Respuesta al impulso")

        for item_key in self.session_data.aproximations.keys():
            item = self.session_data.aproximations[item_key]
            if config.debug:
                print("Graficando Rta Impulso, item= ", item["info"])

            tf = item["data"]["tf"]
            t_range = np.linspace(min_t,max_t, num=100000)
            t,s = signal.impulse(tf,T=t_range)
            if scale == "log":
                self.axis.semilogx(t,s, color =item["info"]["color"])
            else:
                self.axis.plot(t,s, color=item["info"]["color"])

            name = item["info"]["aprox"] + " " + str(item["data"]["number"])
            patches.append(mpatches.Patch(color=item["info"]["color"], label=name))

        self.axis.set_xlabel("$t(s)$")
        self.axis.set_ylabel("$h(t)$")
        self.axis.legend(handles=patches)
        self.dataPlot.draw()

    def plotRtaEscalon(self,min_t, max_t,scale = "log"):
        if not self.session_data.plantilla:
            return 0
        plt.cla()
        self.axis.clear()
        self.nav.update()
        plt.minorticks_on()
        self.setTitulo("Grafico de Respuesta al escalon")
        plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
        patches = []

        for item_key in self.session_data.aproximations.keys():
            item = self.session_data.aproximations[item_key]
            if config.debug:
                print("Graficando Rta Escalon, item= ", item["info"])

            tf = item["data"]["tf"]
            t_range = np.linspace(min_t,max_t, num=100000)
            t,s = signal.step(tf,T=t_range)
            if scale == "log":
                self.axis.semilogx(t,s, color =item["info"]["color"])
            else:
                self.axis.plot(t,s, color=item["info"]["color"])

            name = item["info"]["aprox"] + " " + str(item["data"]["number"])
            patches.append(mpatches.Patch(color=item["info"]["color"], label=name))

        self.axis.set_xlabel("$t(s)$")
        self.axis.set_ylabel("$step(t)$")
        self.axis.legend(handles=patches)
        self.dataPlot.draw()



    def plotQ(self):
        plt.cla()
        self.axis.clear()

        plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

        qs = []
        patches = []
        plots = [ ]

        for item_key in self.session_data.aproximations.keys():
            item = self.session_data.aproximations[item_key]

            tf = item["data"]["tf"]

            etapas = getSing(tf.poles)
            for n in range (len(etapas)):
                if etapas[n].getType() =="conjugados":
                    qs.append(etapas[n].q)


            etapas = getSing(tf.zeros)
            for n in range(len(etapas)):
                if etapas[n].getType() == "conjugados":
                    qs.append(etapas[n].q)

            if len(qs) != 0:

                self.axis.stem(qs)

        self.axis.set_xlabel("$Q number$")
        self.axis.set_ylabel("$Q value$")
        self.dataPlot.draw()








