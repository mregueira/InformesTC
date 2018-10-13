import tkinter.ttk as ttk
from tkinter import *
from data import *


class AproximacionTabla(ttk.Frame):
    def __init__(self, container):
        super(AproximacionTabla, self).__init__(container)

        title = ttk.Label(self, text="Aproximaciones mostradas", font=data.myFont)

        title.pack(side=TOP, fill=Y)

        self.table = ttk.Treeview(self, style="Custom.Treeview", columns=('Item', 'Aproximacion', 'N range', 'Q max', 'color'))
        self.table.heading('#0', text='Item')
        self.table.heading('#1', text='Aproximación')
        self.table.heading('#2', text='N intervalo')
        self.table.heading('#3', text='Q max')
        self.table.heading('#4', text='color')

        self.table.insert(0, END, text="hi!")

        self.table.pack(side=TOP, fill=Y, pady=20)


    #     self.addContent({"Item": 0,
    #                      "Aproximacion": "Butter",
    #                      "N range": "20-30",
    #                      "Q max": "50",
    #                      "color": "#00ff00"})
    #
    # def addContent(self, data):
    #     for j in self.cols:
    #         self.table.insert()
