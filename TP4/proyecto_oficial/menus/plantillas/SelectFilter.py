import config
from data import *
import tkinter
from tkinter import *
from aprox.plantillas import Plantilla
import re


class SelectFilterMenu(ttk.Frame):

    # Menu para seleccionar cual tipo de filtro se calculará
    # Este codigo no esta muy ordenado debido a que fue programado mientras se aprendia por primera vez
    # A utilizar muchos menos distintos de tkinter
    def __init__(self, tabControl, session_data):
        self.session_data = session_data
        super(SelectFilterMenu, self).__init__(tabControl)
        self.tabControl = tabControl
        if config.debug:
            print("Inicializando menu de tipo de filtro")

        self.inputs = dict()

        self.rightFrame = ttk.Frame(self)
        self.leftFrame = ttk.Frame(self)

        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_columnconfigure(1, weight=1, uniform="group1")

        self.background_label = ttk.Label(self.rightFrame, image=data.imagePb)

        self.background_label.pack(fill=BOTH, expand=1)

        self.texts = dict()

        self.var = tkinter.IntVar()
        self.var.set(1)

        languages = [
            ("Pasa bajos", 1),
            ("Pasa altos", 2),
            ("Pasa bandas", 3),
            ("Rechaza bandas", 4),
            ("Retardo de grupo", 5)
        ]

        for lang in languages:
            language, val = lang
            tkinter.Radiobutton(self.leftFrame,
                            text=language,
                            indicatoron=0,
                            width=20,
                            font=data.myFont3,
                            variable=self.var,
                            command=self.ShowChoice,
                            background="cyan2",
                            selectcolor="cyan4",
                            value=val).pack(fill=BOTH, expand=1)

        buttonCommit = Button(self, height=1, width=10, text="Aplicar",
                              command=lambda: self.retrieve_input(), font=data.myFont,
                              background="dark sea green")
        # command=lambda: retrieve_input() >>> just means do this when i press the button
        buttonCommit.pack(side=BOTTOM, fill=BOTH)

        self.leftFrame.pack(side=LEFT, fill=X)
        self.rightFrame.pack(side=LEFT, fill=BOTH)

        self.bind("<Visibility>", self.onVisibility)

    def ShowChoice(self):
        # Actualizar menu a mostrar según el boton presionado
        if config.debug:
            print("Cambiando Plantila a ", str(self.var.get()))

        if self.var.get() == 1:
            self.addTextPaPb(data.imagePb, self.var.get())
        elif self.var.get() == 2:
            self.addTextPaPb(data.imagePa, self.var.get())
        elif self.var.get() == 3:
            self.addTextBpBr(data.imageBp, self.var.get())
        elif self.var.get() == 4:
            self.addTextBpBr(data.imageBr, self.var.get())
        elif self.var.get() == 5:
            self.addTextGd(data.imageGd, self.var.get())

    def onVisibility(self, event):
        # Actualización cuando el tab es abierto
        if self.session_data.plantilla:
            type = self.session_data.plantilla.data["type"]
            if type == "pb":
                self.var.set(1)
            elif type == "pa":
                self.var.set(2)
            elif type == "bp":
                self.var.set(3)
            elif type == "br":
                self.var.set(4)
            elif type == "gd":
                self.var.set(5)

            self.ShowChoice()

            # Actualizamos el texto de la plantilla para
            if type == "pb" or type == "pa":
                for w in ["aa", "ap", "fp", "fa"]:
                    self.updateText(w, str(self.session_data.plantilla.data[w]))

            elif type == "bp" or type == "br":
                for w in ["aa", "ap", "fp-", "fp+", "fa-", "fa+"]:
                    self.updateText(w, str(self.session_data.plantilla.data[w]))

            elif type == "gd":
                for w in ["fp","t0","tmin"]:
                    self.updateText(w, str(self.session_data.plantilla.data[w]))

    def updateText(self, name, content):
        # Agregar texto ya escrito a un text input
        self.texts[name].insert(END, content)

    def addTextPaPb(self, img, mode):
        # Agergar textos en las coodenadas de pasabajo y pasa alto
        self.background_label.destroy()

        self.texts.clear()

        self.background_label = ttk.Label(self.rightFrame, image=img)
        self.background_label.pack(fill=BOTH, expand=1)

        self.texts["ap"] = Text(self.rightFrame, width=6, height=1, font=data.myFont2, background="peach puff")
        self.texts["ap"].place(relx=0.16, rely=0.64, anchor=SE)

        self.texts["aa"] = Text(self.rightFrame, width=6, height=1, font=data.myFont2, background="peach puff")
        self.texts["aa"].place(relx=0.16, rely=0.435, anchor=SE)

        self.texts["fa"] = Text(self.rightFrame, width=8, height=1, font=data.myFont2, background="peach puff")
        self.texts["fa"].place(relx=0.64, rely=0.78, anchor=SE)

        self.texts["fp"] = Text(self.rightFrame, width=8, height=1, font=data.myFont2, background="peach puff")
        self.texts["fp"].place(relx=0.44, rely=0.78, anchor=SE)

        if mode == 2: # pasa altos hay que invertir
            self.texts["fa"], self.texts["fp"] = self.texts["fp"], self.texts["fa"]

    def addTextBpBr(self, img, mode):
        # Agregar texto en las coordenadas de pasabanda y rechaza banda
        self.background_label.destroy()

        self.texts.clear()

        self.background_label = ttk.Label(self.rightFrame, image=img)
        self.background_label.pack(fill=BOTH, expand=1)

        self.texts["ap"] = Text(self.rightFrame, width=6, height=1, font=data.myFont2, background="peach puff")
        self.texts["ap"].place(relx=0.16, rely=0.64, anchor=SE)

        self.texts["aa"] = Text(self.rightFrame, width=6, height=1, font=data.myFont2, background="peach puff")
        self.texts["aa"].place(relx=0.16, rely=0.435, anchor=SE)

        self.texts["fp-"] = Text(self.rightFrame, width=8, height=1, font=data.myFont2, background="peach puff")
        self.texts["fp-"].place(relx=0.38, rely=0.83, anchor=SE)

        self.texts["fa-"] = Text(self.rightFrame, width=8, height=1, font=data.myFont2, background="peach puff")
        self.texts["fa-"].place(relx=0.38, rely=0.78, anchor=SE)

        self.texts["fp+"] = Text(self.rightFrame, width=8, height=1, font=data.myFont2, background="peach puff")
        self.texts["fp+"].place(relx=0.75, rely=0.83, anchor=SE)

        self.texts["fa+"] = Text(self.rightFrame, width=8, height=1, font=data.myFont2, background="peach puff")
        self.texts["fa+"].place(relx=0.75, rely=0.78, anchor=SE)

        if mode == 4:
            # rechaza banda hay que invertir
            self.texts["fa+"], self.texts["fp+"] = self.texts["fp+"], self.texts["fa+"]
            self.texts["fa-"], self.texts["fp-"] = self.texts["fp-"], self.texts["fa-"]

    def addTextGd(self, img, mode):
        self.background_label.destroy()

        self.texts.clear()

        self.background_label = ttk.Label(self.rightFrame,image=img)
        self.background_label.pack(fill=BOTH, expand=1)

        self.texts["t0"] = Text(self.rightFrame, width=6, height=1, font=data.myFont2, background="peach puff")
        self.texts["t0"].place(relx=0.16, rely=0.42, anchor=SE)

        self.texts["tmin"] = Text(self.rightFrame, width=6, height=1, font=data.myFont2, background="peach puff")
        self.texts["tmin"].place(relx=0.16, rely=0.49, anchor=SE)

        self.texts["fp"] = Text(self.rightFrame, width=8, height=1, font=data.myFont2, background="peach puff")
        self.texts["fp"].place(relx=0.6, rely=0.78, anchor=SE)

    def addLabelFrame(self, title):
        # Ya no se usa, y tampoco me acuerdo para que se usaba
        labelframe = LabelFrame(self.rightFrame, text=title)
        labelframe.pack(side=TOP, padx=30, expand="yes", fill="both")

        left = Text(labelframe, height=1, width=10, font=data.myFont)
        left.pack()
        self.inputs[title] = left

    def retrieve_input(self):
        # Conseguimos el input seleccionado y lo procesamos
        if config.debug:
            print("Cambiando Plantila a ", str(self.var.get()))

        data = dict()
        if self.var.get() == 1: # segun que boton fue seleccionado
            data["type"] = "pb"
            name = "Pasa bajos"
        elif self.var.get() == 2:
            data["type"] = "pa"
            name = "Pasa altos"
        elif self.var.get() == 3:
            data["type"] = "bp"
            name = "Pasa banda"
        elif self.var.get() == 4:
            data["type"] = "br"
            name = "Rechaza banda"
        elif self.var.get() == 5:
            data["type"] = "gd"
            name = "Retardo de grupo"

        if len(self.texts.keys()) == 0:
            self.session_data.topBar.setErrorText("No fue seleccionado ningún tipo de filtro")
            return 0

        # Expresion regular para validar si es un decimal
        regnumber = re.compile(r'^\d+(?:.\d*)?$')

        for i in self.texts.keys():
            if not regnumber.match(self.texts[i].get("1.0", 'end-1c')):
                self.session_data.topBar.setErrorText("Entradas numericas incorrectas")
                return 0
            data[i] = float(self.texts[i].get("1.0", 'end-1c'))

        data["denorm"] = 0
        # cargamos la plantilla con los datos adecuados seleccionados
        my_plantilla = Plantilla(data)

        if my_plantilla.corrupta:
            self.session_data.topBar.setErrorText("Entradas numericas incorrectas (mal ordenadas)")
            return 0
        # seteamos la plantilla como informacion de session
        self.session_data.setPlantilla(my_plantilla)
        # actualzamos mensaje superior mostrado
        self.session_data.topBar.setSucessText("Seleccionado: " + name)

    def onChange(self, v):
        print("change")

