import config
import tkinter.ttk as ttk
import tkinter
import data
from ttkthemes import ThemedTk


# Calculador de filtros - archivo principal

# Grupo 1


class MainApp(ThemedTk):
    # Clase principal del proyecto

    def __init__(self):
        ThemedTk.__init__(self)
        self.set_theme("equilux")

        self.resizable(width=False, height=False)
        self.minsize(width=1440, height=900)
        self.maxsize(width=1440, height=900)

        tabControl = ttk.Notebook()


        if config.debug:
            print("Comenzando aplicación principal")

        data.fonts.load_fonts()

        s = tkinter.ttk.Style()
        s.configure("BW.TLabel", font=data.fonts.myFont)

        self.tabControl = ttk.Notebook(style="BW.TLabel")
        self.tab1 = ttk.Frame(self.tabControl, style="BW.TLabel")
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)

        self.init_tabs()

    def init_tabs(self):
        if config.debug:
            print("Inicializando tabs")
        
        self.add_tab("Tipo de filtro", self.tab1)
        self.add_tab("Parámetros", self.tab2)
        self.add_tab("Configuracion", self.tab3)
        self.add_tab("Gráficos", self.tab4)

        self.monty = ttk.LabelFrame(self.tab1, text=' Monty Python ')
        self.monty.grid(column=0, row=0, padx=8, pady=4)

    def add_tab(self, title, tab_object):
        if config.debug:
            print("Adding tab, title=", title)

        self.tabControl.add(tab_object, text=title)
        self.tabControl.pack(expand=1, fill="both")

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    MainApp().run()
