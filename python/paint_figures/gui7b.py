"""This example how make that don't work. """

from tkinter import *
from gui7 import HelloPackage # or from gui7c

frm = Frame()
frm.pack()
Label(frm, text='hello').pack()
part = HelloPackage(frm)
part.pack(side=RIGHT) # KABOOOM! Don't work
frm.mainloop()
