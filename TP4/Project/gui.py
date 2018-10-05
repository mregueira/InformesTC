import matplotlib, sys
matplotlib.use('TkAgg')
from scipy import signal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from numpy import *
from math import *
from tkinter import *
import cmath
from numpy.polynomial import polynomial as P

class DataFromTF:
    def __init__(self):
        self.f = None
        self.mag = None
        self.phase = None

class ButterWorth:
    def __init__(self):
        self.filterType = None
        self.xi = None
        self.nValue = None
        self.normalization = None
        self.Ap = None
        self.As = None
        self.poles = None
        self.DataFromTF = None

    def areAllInputNone(self):
        if self.filterType and self.Ap and self.As and self.As and self.wp and self.ws:
            return 0
        else:
            return 1

class TCExample:
    def nousefunc(self):
        print("im useless")

    # def plotStep(self):
    def getButterWorthInput(self):
        self.ButterWorth.Ap = float(self.textBox[0].get("1.0", "end-1c"))
        self.ButterWorth.As = float(self.textBox[1].get("1.0", "end-1c"))
        self.ButterWorth.wp = float(self.textBox[2].get("1.0", "end-1c"))
        self.ButterWorth.ws = float(self.textBox[3].get("1.0", "end-1c"))

    def goButterWorth(self):
        self.getButterWorthInput()
        if self.ButterWorth.areAllInputNone():
            normalization = None
            #acortamos la notacion
            xi = self.ButterWorth.xi
            nValue = self.ButterWorth.nValue
            Ap = self.ButterWorth.Ap
            As = self.ButterWorth.As
            wp = self.ButterWorth.wp
            ws = self.ButterWorth.ws
            #FALTA : VALIDAR INPUT
            if self.filterType.get() == "LowPass":
                normalization = ws/wp
            elif self.filterType.get() == "HighPass":
                normalization = wp/ws
            if normalization != None:
                xi = ((10**(Ap/10)) - 1)**(1/2)
                num = ((10**(As/10)) - 1)**(1/2)
                nValue = math.ceil(log10(num/xi)/log10(normalization))
                self.ButterWorth.poles = []
                for k in range(0,nValue):
                    self.ButterWorth.poles.append((xi**(1/nValue))*(cmath.exp(1j*(2*k+1+nValue)*(pi/(2*nValue)))))
                print(self.ButterWorth.poles)
                polescoeff=P.polyfromroots(self.ButterWorth.poles)

            transferFunction = signal.TransferFunction(1,polescoeff)

            #self.w, self.mag, self.phase = signal.bode(self.sys)
            w, mag, phase = signal.bode(transferFunction)
            self.ButterWorth.DataFromTF.f = w/(2*pi)
            self.ButterWorth.DataFromTF.mag = mag
            self.ButterWorth.DataFromTF.phase = phase

            self.axis.clear()
            self.axis.plot(self.ButterWorth.DataFromTF.f, self.ButterWorth.DataFromTF.mag)
            self.axis.grid(color='grey', linestyle='-', linewidth=0.1)
            self.axis.set_xlabel("$t (s)$")
            self.axis.set_ylabel("$V_{out} (Volts)$")
            self.dataPlot.draw()


    def __init__(self):
        self.root = Tk()
        self.root.title("Tc Example")
        self.ButterWorth = ButterWorth()
        self.textBox = []
        self.ButterWorth.DataFromTF = DataFromTF()
        #------------------------------------------------------------------------
        toolbar = Frame(self.root)
        toolbarButtons = []
        toolbarButtonsName = [
            ("ButtonPhase",self.nousefunc),
            ("ButtonMag",self.nousefunc),
            ("ButtonStep",self.nousefunc),
            ("ButtonImp",self.nousefunc)
        ]
        for tbname, callback in toolbarButtonsName:
            toolbarButtons.append(Button(toolbar, text=tbname, command=callback))
            toolbarButtons[-1].pack(side=LEFT,padx=2,pady=2)
        toolbar.pack(side=TOP,fill=X)
        #------------------------------------------------------------------------
        self.w=100
        self.h=100

        graph = Canvas(self.root,width=self.w,height=self.h)
        graph.pack(side=RIGHT,expand=True,padx=2,pady=4)
        buttonTF = Button(self.root, height=1, width=20, text="Go ButterWorth", command=self.goButterWorth)
        buttonTF.pack()
        #------------------------

        # --------- Radio Button ------------
        # # ----Aca van los botones de input de butter---
        MODES = [
            ("LP", "LowPass"),
            ("HP", "HighPass"),
            ("BP", "BandPass"),
            ("BR", "BandReject"),
        ]

        self.filterType = StringVar()
        self.filterType.set("LowPass")  # initialize

        for text, mode in MODES:
            b = Radiobutton(self.root, text=text, variable=self.filterType, value=mode)
            b.pack(anchor=NW)
        InputsStr = ['Ap', 'As', 'wp', 'ws']
        for i in range(len(InputsStr)):
            w = Label(self.root, text=InputsStr[i], bg="red", fg="white")
            w.pack(padx=5, pady=8, side=TOP,anchor=NE)
            self.textBox.append(Text(self.root, height=2, width=10))
            self.textBox[i].pack(padx=5, pady=8, side=TOP,anchor=NE)
        # # ---------------------------------------------

        f = Figure()
        self.axis = f.add_subplot(111)
        self.sys = signal.TransferFunction([1], [1, 1])
        self.w, self.mag, self.phase = signal.bode(self.sys)
        self.stepT, self.stepMag = signal.step(self.sys)
        self.dataPlot = FigureCanvasTkAgg(f, master=graph)

        nav = NavigationToolbar2Tk(self.dataPlot, self.root)
        nav.update()
        self.dataPlot.draw()
        self.dataPlot.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=True, anchor=NE)
        self.dataPlot._tkcanvas.pack(side=RIGHT, expand=True)

        #-------------------------------------------------------------------------------
        self.root.mainloop()

if __name__ == "__main__":
    ex = TCExample()
