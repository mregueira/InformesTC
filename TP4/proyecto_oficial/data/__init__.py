
from tkinter.font import Font
import tkinter.ttk as ttk
from tkinter import PhotoImage

# En este archivo configuramos el estilo de el programa
# Actualmente esta un poco desordenado porque fue programado aprendiendo a usarse
# Sobre la marcha


# importante !!!
# Codigo para configurar el estilo de los tab:
# https://stackoverflow.com/questions/23354303/removing-ttk-notebook-tab-dashed-line


class Data:
    myFont = None
    myFont2 = None
    myFont3 = None
    imagePb = None
    imagePa = None
    imageBp = None
    imageBr = None
    imageGd = None

    def __init__(self):
        pass

    def load(self):
        # Fonts utilizados
        self.myFont = Font(family="ProLamina", size=40)
        self.myFont2 = Font(family="ProLamina", size=25)
        self.myFont3 = Font(family="ProLamina", size=40)
        self.myFont4 = Font(family="ProLamina", size=30)
        self.myFontSmall = Font(family="ProLamina", size=20)

        # Imagenes de filtros de la ventana para configurar la plantilla
        self.imagePb = PhotoImage(file="data/filters/pb.png")
        self.imagePa = PhotoImage(file="data/filters/pa.png")
        self.imageBp = PhotoImage(file="data/filters/bp.png")
        self.imageBr = PhotoImage(file="data/filters/br.png")
        self.imageGd = PhotoImage(file="data/filters/gd.png")

        s = ttk.Style()
        mygreen = "#d2ffd2"
        myred = "#006f00"

        # Configuración del theme para el notebook, el treeview, y la progressbar
        s.theme_create("yummy", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [0, 1, 0, 0]}},
            "TNotebook.Tab": {
                "configure": {"padding": [30, 5], "background": mygreen, "font": self.myFont4,
                              "focuscolor": myred},
                "map": {"background": [("selected", myred)]}},
            "Treeview.Heading": {
                "configure": {"font": self.myFont, "background": "SkyBlue2", "padding": [10, 10]},
                "map": {"background": [("selected", myred)]}
            },
            "Treeview": {
                "configure": {"font": self.myFontSmall, "padding": [10, 10]},
                "map": {"background": [("selected", "cyan4")]}
            },
            "red.Horizontal.TProgressbar": {
                "configure": {"foreground": "bisque2", "background": "forestGreen", "thickness": 50}
            }
        })

        s.theme_use("yummy")

        self.pb = PhotoImage(file="data/button/img0.png")
        self.pa = PhotoImage(file="data/button/img1.png")


data = Data()


def begin():
    data.load()
