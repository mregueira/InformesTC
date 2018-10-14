import config
import tkinter.ttk as ttk
import tkinter
import data
from menus import TopBar
from menus.graficos import graficos
from menus.plantillas import SelectFilter
from menus.config_aproximaciones import aproximacion
from aprox import butter_old
from menus import session_data

import numpy as np

## https://tkdocs.com/
# Calculador de filtros - archivo principal

# Grupo 1


class MainApp(tkinter.Tk):
    # Clase principal del proyecto

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

        self.resizable(width=False, height=False)
        self.minsize(width=1024, height=768)
        self.maxsize(width=1024, height=768)

        if config.debug:
            print("Comenzando aplicación principal")

        ### inicializamos recursos externos
        data.begin()
        self.session_data = session_data.SessionData()

        self.tabControl = ttk.Notebook()
        self.topFrame = TopBar.TopBar(self)
        self.topFrame.pack()
        self.tabControl.pack(expand=1, fill="both")

        self.tab1 = SelectFilter.SelectFilterMenu(self.tabControl, self.session_data)
        self.tab3 = aproximacion.AproximacionMenu(self.tabControl, self.session_data)
        self.tab4 = graficos.Graficos(self.tabControl, self.session_data)

        self.initTabs()

        self.aproximations = {"butter": butter_old.Butter()}

    def initTabs(self):
        if config.debug:
            print("Inicializando tabs")
        
        self.addTab("PLANTILLA", self.tab1)
        self.addTab("APROXIMACIÓN", self.tab3)
        self.addTab("GRÁFICOS", self.tab4)

    def addTab(self, title, tabObject):
        if config.debug:
            print("Adding tab, title=", title)

        self.tabControl.add(tabObject, text=title)

    def updatePlot(self, data):
        myAprox = self.aproximations[data["aprox"]]
        myAprox.configure(data["ap"], data["aa"], data["fp"], data["fa"], data["filter"])
        fmin = min(data["fp"], data["fa"])
        fmax = max(data["fp"], data["fa"])
        print(fmin, fmax)
        f_range = np.logspace(np.log10(fmin)-1, np.log10(fmax)+1, 10000)

        myAprox.computar(100, "Pasa Bajos", "sin N", f_range)

        self.tab4.setPlotData({"f": myAprox.f, "mag": myAprox.mag})

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    MainApp().run()
