
from tkinter.font import Font
import tkinter.ttk as ttk
from tkinter import PhotoImage

#importante !!!
# https://stackoverflow.com/questions/23354303/removing-ttk-notebook-tab-dashed-line


class Fonts:
    myFont = None
    photo = None
    def __init__(self):
        pass

    def load_fonts(self):
        self.myFont = Font(family="Impact", size=20)
        s = ttk.Style()

        mygreen = "#d2ffd2"
        myred = "#006f00"

        s.theme_create("yummy", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
            "TNotebook.Tab": {
                "configure": {"padding": [10, 10], "background": mygreen, "font": self.myFont,
                              "focuscolor": myred},
                "map": {"background": [("selected", myred)]}}})

        s.theme_use("yummy")
        self.photo = PhotoImage(file="data/button/img0.png")

fonts = Fonts()