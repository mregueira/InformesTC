# coding=utf-8
import tkinter.ttk as ttk
from tkinter import *
from math import pi
from data import *
import config
from numpy import isinf
from utils import round_sig


class EtapaEE: # etapa compuesta por un polo de orden dos o uno mas uno cero de orden 1 o 2
    def __init__(self, partes):
        self.polos = []
        self.ceros = []

        orderPolos = 0
        orderCeros = 0

        for comp in partes:
            if comp["tipo"] == "polo":
                self.polos.append(comp["contenido"])
                orderPolos += comp["contenido"].order
            else:
                self.ceros.append(comp["contenido"])
                orderCeros += comp["contenido"].order

        self.corrupto = 0
        if orderPolos != 2:
            self.corrupto = 1
        if orderCeros >= 3:
            self.corrupto = 1

    def getTransfer(self):
        pass


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


def addTextInput(container, title, default_text):
    cont = ttk.Frame(container)
    label = Label(cont, text=title, font=data.myFont2, width=20, height=1)
    label.grid(column=0, row=0)

    text = Text(cont, width=20, height=1, font=data.myFont2, background="peach puff")
    text.delete(1.0, 'end-1c')
    text.insert('end-1c', default_text)

    text.grid(column=1, row=0)

    return label, text, cont


class ButtonArray(ttk.Frame):
    def __init__(self, container):
        super(ButtonArray, self).__init__(container)
        self.container = container

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
        self.container.buttonPressed(name)


class SelectEtapas(ttk.Frame):
    def __init__(self, container, session_data):
        super(SelectEtapas, self).__init__(container)
        self.session_data = session_data

        self.topFrame = ttk.Frame(self)

        self.leftFrame = ttk.Frame(self)
        self.rightFrame = ttk.Frame(self)

        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_columnconfigure(1, weight=1, uniform="group1")

        title = Label(self.topFrame, width=23,text="Singularidades", font=data.myFont)
        title.pack(side=LEFT, fill=X)

        titleB = Label(self.topFrame, width= 33,text="Etapas", font=data.myFont)
        titleB.pack(side=LEFT, fill=X)

        self.topFrame.pack(side=TOP, fill=X)
        lb_header = ['Tipo', 'Fc - Q']

        self.table = ttk.Treeview(self.leftFrame, columns=lb_header, show="headings", selectmode='extended')
        for col in lb_header:
            self.table.column(col, anchor="center")
            self.table.heading(col, text=col.title())

        self.labelGain, self.textGain, cont = addTextInput(self.leftFrame, "Ganancia", "1")

        cont.pack(side=BOTTOM, fill=X)

        self.table.pack(side=TOP, fill = BOTH, expand=1)

        # self.menu = SubMenu(self.rightFrame)
        #
        # self.menu.addTextInput("Fc", "")
        # self.menu.addTextInput("Q", "")
        # self.menu.addButton("Actualizar")

        #self.menu.pack(side=TOP, fill=X, expand=1)

        lb_header = ['#', 'Gan - Polo - Cero']

        self.tableB = ttk.Treeview(self.rightFrame, columns=lb_header, show="headings", selectmode='browse')

        for col in lb_header:
            self.tableB.column(col, anchor="center")
            self.tableB.heading(col, text=col.title())

        self.tableB.pack(side=TOP, fill=BOTH, expand=1)

        self.bind("<Visibility>", self.onVisibility)

        self.buttonArray = ButtonArray(self)
        self.buttonArray.addGreenButton("Unir")
        #self.buttonArray.addBlueButton("Swap")
        self.buttonArray.addRedutton("Borrar")

        self.buttonArray.pack(side=BOTTOM, fill=BOTH)

        self.leftFrame.pack(side=LEFT, fill=BOTH, expand=1)
        self.rightFrame.pack(side=RIGHT, fill=BOTH, expand=1)

    def onVisibility(self, event):
        if not self.session_data.aproximationEtapas:
            return 0

        for selected_item in self.table.get_children():
            self.table.delete(selected_item)

        #print(self.session_data.aproximationEtapas.polos)

        for item in self.session_data.aproximationEtapas.polos:
            #tipo = "polo("+str(item.order)+")"
            self.addItem("polo",item.order, item.q, item.f0)
        for item in self.session_data.aproximationEtapas.ceros:
            #tipo = "cero("+str(item.order)+")"
            self.addItem("cero",item.order, item.q, item.f0)

    def addItem(self, tipo,order, q, f0):
        f0 = round_sig(f0, 3)

        if q > 100:
            self.table.insert('', 'end', values=[
                "("+tipo+" en eje Im)",  "f="+str(f0) + "hz"
            ])
        elif f0 < 0:
            self.table.insert('', 'end', values=[
                "(" + tipo + " en origen)", ""
            ])
        elif q == -0.5:
            self.table.insert('', 'end', values=[
                "("+tipo+" - orden 1)", "f=" + str(f0) + "hz"
            ])
        else:
            if not isinf(q):
                q = round_sig(q, 3)
            self.table.insert('', 'end', values=[
                "("+tipo+" - orden 2)", "f="+str(f0) + "hz - q=" + str(q)
            ])

    def buttonPressed(self, button):
        if button == "Unir":
            for item in self.table.selection():
                values = item["values"]



