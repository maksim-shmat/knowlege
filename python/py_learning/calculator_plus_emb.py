from tkinter import *
from calculator import CalcGui, getCalcArgs
from widgets import frame, button, label

class CalcGuiPlus(Toplevel):
    def __init__(self, **args):
        Toplevel.__init__(self)
        label(self, TOP, 'PyCalc Plus - Container')
        self.calc = CalcGui(self, **args)
        frm = frame(self, BOTTOM)
        extrax = [('sqrt', 'sqrt(%s)'),
                  ('x^2', '(%s)**2'),
                  ('x^3', '(%s)**3'),
                  ('1/x', '1.0/(%s)')]

        for (lab, expr) in extras:
            button(frm, LEFT, lab, (lambda expr=expr: self.onExtra(expr)))
        button(frm, LEFT, 'pi', self.onPi)

    def onExtra(self, expr):
        text = self.calc.text
        eval = self.clac.eval
        try:
            text.set(eval.runstring(expr % text.get()))
        except:
            text.set('ERROR')

    def onPi(self):
        self.calc.text.set(self.calc.eval.runstring('pi'))

if __name__ == '__main__':
    root = Tk()
    button(root, TOP, 'Quit', root.quit)
    CalcGuiPlus(**getCalcArgs()).mainloop()
