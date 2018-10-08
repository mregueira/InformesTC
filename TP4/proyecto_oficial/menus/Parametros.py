import tkinter.ttk as ttk
import config
from tkinter import Text, Button
import data


class Parametros(ttk.Frame):
    def __init__(self, tabControl):
        super(Parametros, self).__init__(tabControl)
        if config.debug:
            print("Inicializando menu de tipo de filtro")

        buttonCommit = Button(self, height=1, width=10, text="Aplicar",
                              command=lambda: self.retrieve_input())

        # command=lambda: retrieve_input() >>> just means do this when i press the button
        buttonCommit.pack()

    def retrieve_input(self):
        #inputValue = self.textBox.get("1.0", "end-1c")
        #print(inputValue)
        pass
