import matplotlib, sys
matplotlib.use('TkAgg')
from scipy import signal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import *


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

    def getInputTF(self):
        inputValue = self.textBox.get("1.0", "end-1c")
        #print(inputValue)
        10

    def __init__(self):
        self.root = Tk()
        self.root.title("Tc Example")
        #------------------------------------------------------------------------
        toolbar = Frame(self.root)
        buttonPhase = Button(toolbar,text="Bode Phase",command=self.plotPhase)
        buttonPhase.pack(side=LEFT,padx=2,pady=2)
        buttonMag = Button(toolbar,text="Bode Mag",command=self.plotMag)
        buttonMag.pack(side=LEFT,padx=2,pady=2)
        buttonStep = Button(toolbar,text="Step",command=self.plotStep)
        buttonStep.pack(side=LEFT,padx=2,pady=2)
        buttonImp = Button(toolbar,text="Impulse",command=self.plotImp)
        buttonImp.pack(side=LEFT,padx=2,pady=4)
        toolbar.pack(side=TOP,fill=X)
        graph = Canvas(self.root)
        graph.pack(side=TOP,fill=BOTH,expand=True,padx=2,pady=4)
        buttonCommit = Button(self.root, height=1, width=10, text="Commit", command=self.getInputTF())
        buttonCommit.pack()
        #-------------------------------------------------------------------------------

        f = Figure()
        self.axis = f.add_subplot(111)
        self.sys = signal.TransferFunction([1],[1,1])
        self.w,self.mag,self.phase = signal.bode(self.sys)
        self.stepT,self.stepMag = signal.step(self.sys)
        self.impT,self.impMag = signal.impulse(self.sys)

        self.textBox = Text(self.root, height=2, width=10)
        self.textBox.pack()
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
