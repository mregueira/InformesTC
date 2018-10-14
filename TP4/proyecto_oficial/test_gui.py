from tkinter import *
import tkinter.ttk as ttk
from tkinter.font import Font

def selectItem(v):
    pass



root = Tk()
tree = ttk.Treeview(root, columns=("size", "modified"))
tree["columns"] = ("date", "time", "loc")

tree.column("date", width=65)
tree.column("time", width=40)
tree.column("loc", width=100)

tree.heading("date", text="Date")
tree.heading("time", text="Time")
tree.heading("loc", text="Loc")
tree.bind('<Button-1>', selectItem)
tree.tag_configure('oddrow', background='orange')
tree.tag_configure('evenrow', background='purple')

tree.insert("","end",text = "Name",values = ("Date","Time","Loc"),tags = ('oddrow'))
tree.insert("","end",text = "Name",values = ("Date","Time","Loc"),tags= ('evenrow'))
tree.insert("","end",text = "Name",values = ("Date","Time","Loc"),tags=('oddrow'))

mygreen = "#d2ffd2"
myred = "#006f00"
myFont2 = Font(family="ProLamina", size=25)
myFontSmall = Font(family="ProLamina", size=20)




tree.grid()
root.mainloop()