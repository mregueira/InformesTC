
from tkinter.font import Font
import tkinter.ttk as ttk
from tkinter import PhotoImage

#importante !!!
# https://stackoverflow.com/questions/23354303/removing-ttk-notebook-tab-dashed-line


class Data:
    def __init__(self):
        pass

    def load(self):
        self.myFont = Font(family="Impact", size=20)
        self.myFont2 = Font(family="Impact", size=15)
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
        self.pb = PhotoImage(file="data/button/img0.png")
        self.pa = PhotoImage(file="data/button/img1.png")


data = Data()


def begin():
    data.load()
