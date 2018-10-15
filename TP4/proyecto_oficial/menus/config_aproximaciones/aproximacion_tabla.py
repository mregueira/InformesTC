import tkinter.ttk as ttk
from tkinter import *
from data import *
from utils import random_color
import config


class AproximacionTabla(ttk.Frame):
    def __init__(self, container, session_data):
        super(AproximacionTabla, self).__init__(container)

        self.session_data = session_data
        title = ttk.Label(self, text="Aproximaciones mostradas", font=data.myFont)

        title.pack(side=TOP, fill=Y)
        buttonCommit = Button(self, height=1, width=10, text="Borrar",
                              command=lambda: self.retrieve_input(), font=data.myFont,
                              background="light coral")
        # command=lambda: retrieve_input() >>> just means do this when i press the button
        buttonCommit.pack(side=BOTTOM, fill=BOTH)

        lb_header = ['Item', 'Aprox.', 'N rango', 'Q max', 'Color']
        self.table = ttk.Treeview(self, columns=lb_header, show="headings", selectmode='extended')

        for col in lb_header:
            self.table.column(col, anchor="center")
            self.table.heading(col, text=col.title())

        self.table.bind('<ButtonRelease-1>', self.selectItem)
        self.table.tag_configure('oddrow', background='orange')
        self.table.tag_configure('evenrow', background='purple')

        self.table.pack(side=LEFT, fill=BOTH, expand=1)

    def addItem(self, number, aproxName, min_n, max_n, qmax, color= -1):
        if color == -1:
            color = random_color()

        self.table.insert('', 'end', values=[
            number, aproxName, str(min_n)+"-"+str(max_n), qmax, color
        ])

    def retrieve_input(self):
        if config.debug:
            print("Delete button pressed")
        selected_item = self.table.selection()[0]
        self.session_data.eraseAproximation(self.table.item(selected_item)["values"][0])
        self.table.delete(selected_item)

    def selectItem(self, item):
        curItem = self.table.focus()
        if config.debug:
            print("Selected: ", self.table.item(curItem))

