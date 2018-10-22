import tkinter as tk
from tkinter import ttk, Tk


def insert(tree, value):
    tree.insert('', tk.END, value, text=value)

root = Tk()
tree = ttk.Treeview(root)

insert(tree, '1')
insert(tree, '2')
insert(tree, '3')

tree.pack()
children = tree.get_children()
tree.selection_set(children)
tree.selection_toggle(children[1])

# uncomment line by line to see the change
#tree.selection_toggle(children)
#tree.selection_remove(children[1])

print(tree.selection())

root.mainloop()