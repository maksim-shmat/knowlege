from tkinter import *
from quitter import Quitter

demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']
parts = []

def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)
        part = module.Demo(root)
        part.config(bd=2, relief=GROOVE)
        part.pack(side=LEFT, expand=YES, fill=BOTH)
        parts.append(part)

"""
def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)
        part = module.Demo(root, bd=6, relief=RIDGE)
        part.pack(side=LEFT, expand=YES, fill=BOTH)
"""
def dumpState():
    for part in parts:
        print(part.__madule__ + ':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')

root = Tk()
root.title('Frames')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()
