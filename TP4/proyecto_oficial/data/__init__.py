from tkinter.font import Font
import tkinter.ttk as ttk


class Fonts:
    myFont = None

    def __init__(self):
        pass

    def load_fonts(self):
        self.myFont = Font(family="Times New Roman", size=40)




fonts = Fonts()