# save your radiobutton variables, remember it!

from tkinter import *
root = Tk()

def radio1():      # local var is temporary, make it global
   # global tmp     #decoment in for normalaiz
    tmp = IntVar()
    for i in range(10):
        rad = Radiobutton(root, text=str(i), value=i, variable=tmp)
        rad.pack(side=LEFT)
    tmp.set(5)

radio1()
root.mainloop()
