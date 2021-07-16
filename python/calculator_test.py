from tkinter import *
from calculator import CalcGui

def calcContainer(parent=None):
    frm = Frame(parent)
    frm.pack(expand=YES, fill=BOTH)
    Label(frm, text='Calc Conteiner').pack(side=TOP)
    CalcGui(frm)
    Label(frm, text='Calc Container').pack(side=BOTTOM)
    return frm

class calcSubclass(CalcGui):
    def makeWidgets(self, fg, bg, font):
        Label(self, text='Calc Subclass').pack(side=TOP)
        CalcGui(frm)
        Label(frm, text='Calc Container').pack(side=BOTTOM)
        return frm

class calcSubclass(CalcGui):
    def makeWidgets(self, fg, bg, font):
        Label(self, text='Calc Subclass').pack(side=TOP)
        Label(self, text='Calc Subclass').pack(side=BOTTOM)
        CalcGui.makeWidgets(self, fg, bg, font)
        #Label(self, text='Calc Subclass').pack(side=BOTTOM)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        root = Tk()
        CalcGui(Toplevel())
        calcContainer(Toplevel())
        calcSubclass(Toplefel())
        Button(root, text='quit', command=root.quit).pack()
        root.mainloop()

    if len(sys.argv) == 2:
        CalcGui().mainloop()
    elif len(sys.argv) == 3:
        calcContainer().mainloop()
    elif len(sys.argv) == 4:
        calcSubclass().mainloop()
