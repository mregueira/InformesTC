import config
import tkinter.ttk as ttk
import tkinter
import data
from menus import SelectFilter

## https://tkdocs.com/
# Calculador de filtros - archivo principal

# Grupo 1


class MainApp(tkinter.Tk):
    # Clase principal del proyecto

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

        self.resizable(width=False, height=False)
        self.minsize(width=1440, height=900)
        self.maxsize(width=1440, height=900)

        if config.debug:
            print("Comenzando aplicación principal")

        data.fonts.load_fonts()

        self.tabControl = ttk.Notebook()

        #print(ttk.Notebook().winfo_class())
        self.tab1 = SelectFilter.SelectFilterMenu(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)

        self.initTabs()

    def initTabs(self):
        if config.debug:
            print("Inicializando tabs")
        
        self.addTab("TIPO DE FILTRO", self.tab1)
        self.addTab("PARÁMETROS", self.tab2)
        self.addTab("CONFIG", self.tab3)
        self.addTab("GRÁFICOS", self.tab4)

        #self.monty = ttk.LabelFrame(self.tab1, text=' Monty Python ')
        #self.monty.grid(column=0, row=0, padx=8, pady=4)

    def addTab(self, title, tabObject):
        if config.debug:
            print("Adding tab, title=", title)

        self.tabControl.add(tabObject, text=title)
        self.tabControl.pack(expand=1, fill="both")

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    MainApp().run()
