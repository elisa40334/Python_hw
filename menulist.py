# -*- coding: utf-8 -*-
"""
menu.py

"""

from tkinter import Tk, Menu, filedialog

def NewFile():
    print("New File!")
def OpenFile():
    name = filedialog.askopenfilename()
    print(name)
def About():
    print("This is a simple example of a menu")
    
root = Tk()
menu = Menu(root)
filemenu = Menu(menu)
menu.add_cascade(label="Menu", menu=filemenu)
# configure File menu items
filemenu.add_command(label="Analyze", command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
#configure Help menu items
helpmenu.add_command(label="About...", command=About)

root.config(menu=menu)
root.mainloop()

