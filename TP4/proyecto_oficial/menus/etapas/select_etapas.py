# coding=utf-8
import tkinter.ttk as ttk
from tkinter import *
from math import pi
from data import *
import config


class SubMenu(ttk.Frame):
    def __init__(self, container):
        super(SubMenu, self).__init__(container)
        self.var = dict()
        self.widgets = []

        self.topFrame = ttk.Frame(self)
        Label(self.topFrame, text="Ajustes", width=25, font=data.myFont).pack(side=TOP, fill=X, expand=1)

        self.bottomFrame = ttk.Frame(self)
        self.bottomFrame.pack(side=BOTTOM, fill=X, expand=1)

        self.topFrame.pack(side=TOP, fill=X, expand=1)

        self.downFrame = ttk.Frame(self)
        self.downFrame.pack(side=TOP)

        self.total = 1

    def addTextInput(self, title, default_text):
        # Agregar un text input en el menu
        label = Label(self.downFrame, text=title, font=data.myFont2, width=20, height=2)
        label.grid(column=0, row=self.total)

        text = Text(self.downFrame, width=20, height=1, font=data.myFont2, background="peach puff")
        text.delete(1.0, 'end-1c')
        text.insert('end-1c', default_text)

        text.grid(column=1, row=self.total)

        self.var[title] = text

        self.widgets.append(label)
        self.widgets.append(text)

        self.total += 1

    def addButton(self, title):
        button = Button(self.bottomFrame, height=1, text=title,
                        command=lambda: self.retrieve_input(title), font=data.myFont,
                        background="dark sea green")
        button.pack(side=BOTTOM, fill=X, expand=1)

    def retrieve_input(self, title):
        # if config.debug:
        #     print(title)
        pass

    def eraseWidgets(self):
        for w in self.widgets:
            w.destroy()
        self.widgets = []


class ButtonArray(ttk.Frame):
    def __init__(self, container):
        super(ButtonArray, self).__init__(container)

    def addGreenButton(self, title):
        button = Button(self, height=1,text=title,
                              command=lambda: self.retrieve_input(title), font=data.myFont,
                              background="dark sea green")
        button.pack(side=LEFT, expand=1, fill=BOTH)

    def addRedutton(self, title):
        button = Button(self, height=1,text=title,
                              command=lambda: self.retrieve_input(title), font=data.myFont,
                              background="light coral")
        button.pack(side=LEFT, expand=1, fill=BOTH)

    def addBlueButton(self, title):
        button = Button(self, height=1,text=title,
                              command=lambda: self.retrieve_input(title), font=data.myFont,
                              background="dodger blue")
        button.pack(side=LEFT, expand=1, fill=BOTH)

    def retrieve_input(self, name):
        pass


class SelectEtapas(ttk.Frame):
    def __init__(self, container, session_data):
        super(SelectEtapas, self).__init__(container)
        self.session_data = session_data

        title = ttk.Label(self, text="Etapas", font=data.myFont)
        title.pack(side=TOP, fill=Y)

        self.leftFrame = ttk.Frame(self)
        self.rightFrame = ttk.Frame(self)

        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_columnconfigure(1, weight=1, uniform="group1")

        lb_header = ['Tipo', 'G - Fc - Q']

        self.table = ttk.Treeview(self.leftFrame, columns=lb_header, show="headings", selectmode='extended')
        for col in lb_header:
            self.table.column(col, anchor="center")
            self.table.heading(col, text=col.title())

        self.table.pack(side=LEFT, fill=BOTH, expand=1)

        self.menu = SubMenu(self.rightFrame)

        self.menu.addTextInput("G", "")
        self.menu.addTextInput("Fc", "")
        self.menu.addTextInput("Q", "")
        self.menu.addButton("Actualizar")

        self.menu.pack(side=TOP, fill=X, expand=1)
        self.bind("<Visibility>", self.onVisibility)

        self.buttonArray = ButtonArray(self)
        self.buttonArray.addBlueButton("Agregar")
        self.buttonArray.addRedutton("Borrar")
        self.buttonArray.addGreenButton("Graficar")

        self.buttonArray.pack(side=BOTTOM, fill=BOTH)

        self.leftFrame.pack(side=LEFT, fill=X, expand=1)
        self.rightFrame.pack(side=LEFT, fill=BOTH, expand=1)



    def onVisibility(self, event):
        if not self.session_data.aproximationEtapas:
            return 0

        for selected_item in self.table.get_children():
            self.table.delete(selected_item)

        for item in self.session_data.aproximationEtapas.etapas:
            self.addItem(item.order, item.k, item.f0, item.q)

    def addItem(self, order, g, f0, q):
        if order == 1:
            q = ""
        else:
            q = "-" + str(q)

        self.table.insert('','end', values=[
            order, str(g) + "-" + str(f0) + q
        ])
