import config
import tkinter.ttk as ttk
import tkinter

# Calculador de filtros - archivo principal

# Grupo 1


class MainApp:
    # Clase principal del proyecto
    root = tkinter.Tk()
    tabControl = ttk.Notebook()
    tab1 = ttk.Frame(tabControl)

    def __init__(self):
        if config.debug:
            print("Comenzando aplicación principal")

        self.init_tabs()

    def init_tabs(self):
        if config.debug:
            print("Inicializando tabs")
        self.tabControl.add(self.tab1, text='Tab 1')
        self.tabControl.pack(expand=1, fill="both")

        self.monty = ttk.LabelFrame(self.tab1, text=' Monty Python ')
        self.monty.grid(column=0, row=0, padx=8, pady=4)


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    MainApp().run()
