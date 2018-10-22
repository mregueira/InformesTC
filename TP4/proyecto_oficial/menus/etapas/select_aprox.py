# coding=utf-8
import tkinter.ttk as ttk
from utils import random_color
from tkinter import *
from data import *

class SelectAprox(ttk.Frame):
    def __init__(self, container, session_data):
        super(SelectAprox, self).__init__(container)
        self.session_data = session_data

        lb_header = ['Item', 'Aprox.', 'N', 'Denorm', 'Color']
        self.table = ttk.Treeview(self, columns=lb_header, show="headings", selectmode='browse')
        for col in lb_header:
            self.table.column(col, anchor="center")
            self.table.heading(col, text=col.title())

        self.bind("<Visibility>", self.onVisibility)

        buttonCommit = Button(self, height=1, width=10, text="Seleccionar",
                              command=lambda: self.retrieve_input(), font=data.myFont,
                              background="dark sea green")
        # command=lambda: retrieve_input() >>> just means do this when i press the button
        buttonCommit.pack(side=BOTTOM, fill=BOTH)

        self.table.pack(side=LEFT, fill=BOTH, expand=1)

    def onVisibility(self , event):
        # actualizamos
        for selected_item in self.table.get_children():
            self.table.delete(selected_item)

        for item in self.session_data.aproximations.keys():
            act = self.session_data.aproximations[item]

            self.addItem(act["info"]["number"],
                         act["info"]["aprox"] + " " + str(act["data"]["number"]) + " " + str(act["info"]["norm"]),
                         act["info"]["minN"],
                         act["info"]["norm"],
                         act["info"]["color"])

    def retrieve_input(self):
        selected_item = self.table.selection()[0]
        code = self.table.item(selected_item)["values"][0]
        self.session_data.selectParaEtapas(code)

        self.session_data.topBar.setSucessText("Aproximacion seleccionada: " + str(self.table.item(selected_item)["values"][1]))

    def addItem(self, number, aproxName, n, denorm, color = -1):
        if color == -1:
            color = random_color()

        self.table.insert('','end', values=[
            number, aproxName, str(n) , str(denorm), color
        ])
