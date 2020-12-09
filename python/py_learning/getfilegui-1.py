import sys, os
from tkinter import *
from tkinter.messagebox import showinfo

def onReturnKey():
    cmdline = ('python getfile.py -mode client -file %s -port %s -host %s' %
            (connect['File'].get(),
             connect['Port'].get(),
             connect['Server'].get()))

    os.system(cmdline)
    showinfo('getfilegui-1', 'Download complete')
    box = Tk()
    labels = ['Server', 'Port', 'File']
    content = {}
    for label in labels:
        row = Frame(box)
        row.pack(fill=X)
        Label(row, text=label, width=6).pack(side=LEFT)
        entry = Entry(row)
        content[label] = entry
    box.title('getfilegui-1')
    box.bind('<Return>', (lambda event: onReturnKey()))
    mainloop()
