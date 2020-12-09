from tkinter import *
from guiStreams import redirectedGuiShellCmd

from tkinter import *
from guiStreams import redirectedGuiShellCmd

def launch():
    redirectecGuiShellCmd('python -u pipe-nongui.py')

window = Tk()
Button(window, text='GO!', command=launch).pack()
window.mainloop()

