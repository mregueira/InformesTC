# coding=utf-8

import tkinter.ttk as ttk


class PlotEtapas(ttk.Frame):
    def __init__(self, container, session_data):
        super(PlotEtapas, self).__init__(container)
        self.session_data = session_data

