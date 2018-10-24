# coding=utf-8
import tkinter.ttk as ttk
from tkinter import *
from math import pi
from data import *
import config
from numpy import isinf, log10
from utils import round_sig
from utils.parse_float import getText
from utils.etapas import getSingText
from algoritmos.auto_comb import autoComb


def getEtapaText(etapa):
    gainText = str(int(20 * log10(etapa.gain)*100)/100.0) + "dB"

    # siempre tiene un polo
    sing = etapa.polo
    f0text, qText = getSingText(sing)
    poloText = f0text + " " + qText

    if etapa.cero:
        f0text, qText = getSingText(etapa.cero)
        ceroText = f0text + " " + qText
    else:
        ceroText = "Ninguno"

    return gainText, poloText, ceroText


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


def addTextInput(container, title, default_text, mode = "horizontal", w = 15):
    cont = ttk.Frame(container)
    label = Label(cont, text=title, font=data.myFont2, width=w, height=1)
    label.grid(column=0, row=0)

    text = Text(cont, width=10, height=1, font=data.myFont2, background="peach puff")
    text.delete(1.0, 'end-1c')
    text.insert('end-1c', default_text)

    if mode == "horizontal":
        text.grid(column=1, row=0)
    else:
        text.grid(column=0, row=1)

    return label, text, cont

def addShowText(container, title, default_text, w, size = "big"):
    cont = ttk.Frame(container)

    label = Label(cont, text=title, font=data.myFont2, width=w)
    label.pack(side=TOP, fill=BOTH, expand=1)
    if size == "big":
        text = Label(cont, width=10, text=default_text, font=data.myFont, background="peach puff")
    else:
        text = Label(cont, width=10, text=default_text, font=data.myFont2, background="peach puff")

    text.pack(side=TOP, fill=BOTH, expand=1)

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

    def addGold2Button(self, title):
        button = Button(self, height=1, text=title,
                        command=lambda: self.retrieve_input(title), font=data.myFont,
                            background="thistle")
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

        title = Label(self.topFrame, width=23, text="Singularidades", font=data.myFont)
        title.pack(side=LEFT, fill=X)

        titleB = Label(self.topFrame, width= 33, text="Etapas", font=data.myFont)
        titleB.pack(side=LEFT, fill=X)

        self.topFrame.pack(side=TOP, fill=X)
        lb_header = ['#', 'Tipo', 'Fc - Q']

        self.table = ttk.Treeview(self.leftFrame, columns=lb_header, show="headings", selectmode='extended')

        start = 1
        for col in lb_header:
            if start:
                self.table.column(col, anchor="center", width=40)
                start = 0
            else:
                self.table.column(col, anchor="center", width=150)
            self.table.heading(col, text=col.title())

        #Agregamos text inputs. Lamentablemente no se ve muy lindo, lo ideal seria usar un layout file

        self.freqCont = ttk.Frame(self.rightFrame)

        self.downTextCont = ttk.Frame(self.rightFrame)
        self.downTextCont2 = ttk.Frame(self.downTextCont)
        self.downTextCont3 = ttk.Frame(self.downTextCont)
        self.vContainer = ttk.Frame(self.downTextCont3)

        self.labelGain, self.textGain, cont1 = addTextInput(self.leftFrame, "Ganancia etapa (db)", "0", "horizontal", 20)
        self.labelMinFreq, self.textMinFreq, contMinFreq = addTextInput(self.downTextCont2, "Frec. Min (hz)", "100","horizontal", 18)
        self.labelMaxFreq, self.textMaxFreq, contMaxFreq = addTextInput(self.downTextCont2, "Frec. Max (hz)", "1000000","horizontal", 18)

        self.labelMinSignal, self.textMinSignal, contMaxSignal = addTextInput(self.downTextCont2, "Señal mínima (V)", "0.05", "horizontal", 18)
        self.labelMaxSignal, self.textMaxSignal, contMinSignal = addTextInput(self.downTextCont2, "Señal máxima (V)", "15", "horizontal", 18)
        self.labelTotalGain, self.textTotalGain, cont4 = addTextInput(self.downTextCont2, "Ganancia total (db)", "0", "horizontal", 18)

        self.labelVmin, self.textVMin, contVmin = addShowText(self.vContainer, "Vmin (V)", "Ind.", 13, "small")
        self.labelVmax, self.textVMax, contVmax = addShowText(self.vContainer, "Vmax (V)", "Ind.", 13, "small")

        self.labelRD, self.textRD, cont5 = addShowText(self.downTextCont3, "Rango dinamico (db)", "Ind.", 27)


        contMaxSignal.pack(side=TOP, fill=X)
        contMinSignal.pack(side=TOP, fill=X)

        cont1.pack(side=BOTTOM, fill=X)
        contMinFreq.pack(side=TOP, fill=X)
        contMaxFreq.pack(side=TOP, fill=X)
        cont4.pack(side=TOP, fill=X)

        contVmin.grid(column=0, row=0)
        contVmax.grid(column=1, row=0)

        self.vContainer.pack(side=TOP, fill=BOTH, expand=1)

        cont5.pack(side=TOP, fill=BOTH, expand=1)

        self.downTextCont2.grid(column=0, row=0)
        self.downTextCont3.grid(column=1, row=0)


        self.downTextCont.pack(side=BOTTOM, fill=X)

        self.freqCont.pack(side=BOTTOM,fill=X)
        #self.downTextCont1.pack(side=BOTTOM, fill=X)

        self.table.pack(side=TOP, fill = Y, expand=1)

        lb_header = ['#', 'Gan', 'Polo', 'Cero']

        self.tableB = ttk.Treeview(self.rightFrame, columns=lb_header, show="headings", selectmode='browse')

        start = 1
        for col in lb_header:
            if start:
                self.tableB.column(col, anchor="center", width = 40)
                start = 0
            else:
                self.tableB.column(col, anchor="center", width=200)
            self.tableB.heading(col, text=col.title())

        self.tableB.pack(side=TOP, fill=BOTH, expand=1)

        self.bind("<Visibility>", self.onVisibility)

        self.buttonArray = ButtonArray(self)
        self.buttonArray.addGreenButton("Unir")
        self.buttonArray.addBlueButton("Calcular RD")
        self.buttonArray.addGold2Button("Auto-comb")
        self.buttonArray.addRedutton("Borrar")

        self.buttonArray.pack(side=BOTTOM, fill=BOTH)

        self.leftFrame.pack(side=LEFT, fill=BOTH, expand=1)
        self.rightFrame.pack(side=RIGHT, fill=BOTH, expand=1)

    def onVisibility(self, event):
        if not self.session_data.aproximationEtapas:
            return 0
        if not self.session_data.getUpdateSing():
            return 0

        for selected_item in self.table.get_children():
            self.table.delete(selected_item)

        for selected_item in self.tableB.get_children():
            self.tableB.delete(selected_item)

        #print(self.session_data.aproximationEtapas.polos)

        # for item in self.session_data.aproximationEtapas.polos:
        #     #tipo = "polo("+str(item.order)+")"
        #     self.addItem(i, "polo", item.order, item.q, item.f0)
        #     i += 1
        # for item in self.session_data.aproximationEtapas.ceros:
        #     #tipo = "cero("+str(item.order)+")"
        #     self.addItem(i, "cero", item.order, item.q, item.f0)
        #     i += 1
        for item_key in self.session_data.aproximationEtapas.conjunto.keys():
            item = self.session_data.aproximationEtapas.conjunto[item_key]
            self.addSing(item)

    def getGainText(self):
        return getText(self.textGain)

    def addSing(self, item):
        contenido = item["contenido"]
        self.addItem(item["index"], item["tipo"], contenido.order, contenido.q, contenido.f0)

    def removeSing(self, item):
        for child in self.table.get_children():
            #cuadratico - no importa en el contexto de funcionamiento es rápido
            content = self.table.item(child)
            if str(content["values"][0]) == str(item):
                self.table.delete(child)

    def removeEtapaTable(self, item):
        for child in self.tableB.get_children(): #cuadratico
            content = self.tableB.item(child)
            if str(content["values"][0]) == str(item):
                self.tableB.delete(child)

    def addItem(self, index, tipo, order, q, f0, pos = 'end'):
        f0 = round_sig(f0, 2)

        if q > 100:
            self.table.insert('', pos, values=[
                index, "("+tipo+" en eje Im)",  "f="+str(f0) + "hz"
            ])
        elif f0 < 0:
            self.table.insert('', pos, values=[
                index, "(" + tipo + " en origen)", ""
            ])
        elif q == -0.5:
            self.table.insert('', pos, values=[
                index, "("+tipo+" - orden 1)", "f=" + str(f0) + "hz"
            ])
        else:
            if not isinf(q):
                q = round_sig(q, 2)
            self.table.insert('', pos, values=[
                index, "("+tipo+" - orden 2)", "f="+str(f0) + "hz - q=" + str(q)
            ])

    def addItemEtapa(self, index, gan, polo, cero):
        self.tableB.insert('', 'end', values=
                          [index, gan, polo, cero], )

    def buttonPressed(self, button):
        if button == "Unir":
            codes = []
            items = []
            for sel in self.table.selection():
                codes.append(self.table.item(sel)["values"][0])
                items.append(self.table.item(sel))
            if self.tryJoin(codes):
                for i in codes:
                    self.removeSing(i)
            self.table.selection_set([])

        elif button == "Borrar":

            for sel in self.tableB.selection():
                item = self.tableB.item(sel)
                self.removeEtapaTable(item["values"][0])
                self.eraseEtapa(item["values"][0])

            self.tableB.selection_set([])

        elif button == "Calcular RD":
            min_freq = getText(self.textMinFreq)
            max_freq = getText(self.textMaxFreq)
            v_ruido = getText(self.textMinSignal)
            v_sat = getText(self.textMaxSignal)

            if not min_freq or not max_freq:
                self.session_data.topBar.setErrorText("Frecuencias invalidas")
                return 0
            if not min_freq + 1e-5 < max_freq:
                self.session_data.topBar.setErrorText("Frecuencias invalidas")
                return 0
            if not v_ruido:
                self.session_data.topBar.setErrorText("Tensiones invalidas")
                return 0
            if not v_sat:
                self.session_data.topBar.setErrorText("Tensiones invalidas")
                return 0
            if not v_ruido + 1e-5 < v_sat:
                self.session_data.topBar.setErrorText("Tensiones invalidas")
                return 0

            self.session_data.updateMaxMinEtapas(min_freq, max_freq)

            ans = self.session_data.computeRD(v_ruido, v_sat)
            if not ans:
                self.session_data.topBar.setErrorText("No hay etapas")
                return 0

            v_max, v_min, RD = ans

            self.setRDText(RD)
            self.setVmaxText(v_max)
            self.setVminText(v_min)

        elif button == "Auto-comb":
            autoComb(self.session_data.aproximationEtapas)

    def setRDText(self, RD):

        if not RD:
            self.textRD["text"] = "Ind."
            return 0

        RD = round_sig(20*log10(RD), 2)

        RD = str(RD) + "dB"

        self.textRD["text"] = RD

    def setVminText(self, vmin):
        if not vmin:
            self.textVMin["text"] = "Ind."
            return 0
        vmin = round_sig(vmin, 2)
        vmin = str(vmin) + "v"
        self.textVMin["text"] = vmin

    def setVmaxText(self, vmax): # copie el codigo 3 veces, deberia haber hecho una funcion y usar un dict
        if not vmax:
            self.textVMax["text"] = "Ind."
            return 0
        vmax = round_sig(vmax, 2)
        vmax = str(vmax) + "v"
        self.textVMax["text"] = vmax

    def tryJoin(self, codes):
        gain = 10**(self.getGainText()/20.0)

        if not gain:
            self.session_data.topBar.setErrorText("Ganancia incorrecta")
            return 0

        ans = self.session_data.tryToJoin(codes, gain)
        if not ans:
            self.session_data.topBar.setErrorText("No se puede unir las singularidades")
            return 0

        ganText, poloText, ceroText = getEtapaText(ans)

        self.addItemEtapa(ans.index, ganText, poloText, ceroText)

        # for polo in ans.polos:
        #     self.removeSing(polo.index)
        #
        # for cero in ans.ceros:
        #     self.removeSing(cero.index)

        return 1

    def eraseEtapa(self, index):
        for polo in self.session_data.etapas[index].polos:
            self.addItem(polo.index, "polo", polo.order, polo.q, polo.f0, polo.index)
        for cero in self.session_data.etapas[index].ceros:
            self.addItem(cero.index, "cero", cero.order, cero.q, cero.f0, cero.index)

        self.session_data.ereaseEtapa(index)


