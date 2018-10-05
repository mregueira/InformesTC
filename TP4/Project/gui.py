import matplotlib, sys
matplotlib.use('TkAgg')
from scipy import signal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from numpy import *
from math import *
from tkinter import *
from random import *


class ButterWorth:
    def __init__(self):
        self.filt0r_type = None
        self.xi = None
        self.nVal1e = None
        self.normalization = None
        self.Ap = None
        self.As = None
        self.poles = None

    def areAllAttrNone(self):
        if self.filter_type and self.Ap and self.xi and self.nValue and self.Ap and self.As and self.poles:
            return 0
        else:
            return 1

class TCExample:
    def plotPhase(self):
        self.axis.clear()
        self.axis.semilogx(self.w,self.phase)
        self.axis.grid(color='grey',linestyle='-',linewidth=0.1)
        self.axis.set_xlabel("$f (Hz)$")
        self.axis.set_ylabel("$Phase (deg)$")
        self.dataPlot.draw()

    def plotMag(self):
        self.axis.clear()
        self.axis.semilogx(self.w,self.mag)
        self.axis.grid(color='grey',linestyle='-',linewidth=0.1)
        self.axis.set_xlabel("$f (Hz)$")
        self.axis.set_ylabel("$V_{out}/V_{in} (dB)$")
        self.dataPlot.draw()

    def plotStep(self):
        self.axis.clear()
        self.axis.plot(self.stepT,self.stepMag)
        self.axis.grid(color='grey',linestyle='-',linewidth=0.1)
        self.axis.set_xlabel("$t (s)$")
        self.axis.set_ylabel("$V_{out} (Volts)$")
        self.dataPlot.draw()

    def plotImp(self):
        self.axis.clear()
        self.axis.plot(self.impT,self.impMag)
        self.axis.grid(color='grey',linestyle='-',linewidth=0.1)
        self.axis.set_xlabel("$t (s)$")
        self.axis.set_ylabel("$V_{out} (Volts)$")
        self.dataPlot.draw()

    def goButterWorth(self):
        if self.ButterWorth:
            self.ButterWorth.Ap = self.textBox[0].get("1.0","end-1c")
            self.ButterWorth.As = self.textBox[1].get("1.0","end-1c")
            self.ButterWorth.wp = self.textBox[2].get("1.0","end-1c")
            self.ButterWorth.ws = self.textBox[3].get("1.0","end-1c")
            normalization = None
            if self.ButterWorth.areAllAttrNone() == 0:
                #acortamos la notacion
                xi = ButterWorth.xi
                nValue = ButterWorth.nValue
                wp = ButterWorth.wp
                ws = ButterWorth.ws
                #FALTA : VALIDAR INPUT
                if self.filterType == "lowpass":
                    normalization = ws/wp
                elif self.filterType == "highpass":
                    normalization = wp/ws
                if normalization != None:
                    xi = ((10**(ButterWorth.Ap/10)) - 1)**(1/2)
                    num = ((10**(ButterWorth.As/10)) - 1)**(1/2)
                    nValue = math.ceil(log10(num/xi)/log10(normalization))
                    self.ButterWorth.poles = []
                    for k in range(0,ButterWorth.nValue):
                        ButterWorth.poles.append((xi**(1/nValue))*(exp(1j*(2*k+1+nValue)*(pi/(2*nValue)))))
                        print(ButterWorth.poles)

    def __init__(self):
        self.root = Tk()
        self.root.title("Tc Example")
        self.ButterWorth = None
        self.textBox = []
        #------------------------------------------------------------------------
        toolbar = Frame(self.root)
        buttonPhase = Button(toolbar, text="Bode Phase", command=self.plotPhase)
        buttonPhase.pack(side=LEFT,padx=2,pady=2)
        buttonMag = Button(toolbar,text="Bode Mag",command=self.plotMag)
        buttonMag.pack(side=LEFT,padx=2,pady=2)
        buttonStep = Button(toolbar,text="Step",command=self.plotStep)
        buttonStep.pack(side=LEFT,padx=2,pady=2)
        buttonImp = Button(toolbar,text="Impulse",command=self.plotImp)
        buttonImp.pack(side=LEFT,padx=2,pady=4)
        toolbar.pack(side=TOP,fill=X)
        graph = Canvas(self.root)
        #graph.pack(side=TOP,fill=BOTH,expand=True,padx=2,pady=4)
        graph.pack(side=RIGHT, padx=2, pady=4)

        buttonTF = Button(self.root, height=1, width=20, text="Go ButterWorth", command=self.goButterWorth)
        buttonTF.pack()


        #-------------------------------------------------------------------------------

        f = Figure()
        self.axis = f.add_subplot(111)
        self.sys = signal.TransferFunction([1],[1,1])
        self.w,self.mag,self.phase = signal.bode(self.sys)
        self.stepT,self.stepMag = signal.step(self.sys)
        self.impT,self.impMag = signal.impulse(self.sys)

        # --------- Radio Button ------------
        MODES = [
            ("Low Pass", "LP"),
            ("High Pass", "HP"),
            ("Band Pass", "BP"),
            ("Band Reject", "BR"),
        ]
        self.filter_type = StringVar()
        self.filter_type.set("LP")  # initialize

        for text, mode in MODES:
            b = Radiobutton(self.root, text=text, variable=self.filter_type, value=mode)
            b.pack(anchor=NW)
        #----Aca van los botones de input de butter---
        InputsStr = ['Ap', 'As', 'wp', 'ws']
        for i in range(len(InputsStr)):
            w = Label(self.root, text=InputsStr[i], bg="red", fg="white")
            w.pack(padx=5, pady=10, side=TOP)
            self.textBox.append(Text(self.root, height=2, width=10))
            self.textBox[i].pack(padx=5, pady=10, side=TOP)
        # ---------------------------------------------

        self.dataPlot = FigureCanvasTkAgg(f, master=graph)
        self.dataPlot.draw()
        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        nav = NavigationToolbar2Tk(self.dataPlot, self.root)
        nav.update()
        self.dataPlot._tkcanvas.pack(side=TOP, fill=X, expand=True)
        self.plotMag()
        #-------------------------------------------------------------------------------
        self.root.mainloop()

if __name__ == "__main__":
    ex = TCExample()
