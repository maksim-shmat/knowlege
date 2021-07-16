from tkinter import *
from calculator import CalcGui, getCalcArgs
from widgets import label, frame, button

class CalcGuiPlus(CalcGui):
    def makeWidgets(self, *args):
        label(self, TOP, 'PyCalc Plus - Subclass')
        CalcGui.makeWidgets(self, *args)
        frm = frame(self, BUTTOM)
        extras = [('sqrt', 'sqrt(%s)'),
                  ('x^2', '(%s)**2'),
                  ('x^3', '(%s)**3'),
                  ('1/x', '1.0/(%s)')]

        for (lab, expr) in extras:
            button(frm, LEFT, lab, (lambda expr=expr: self.onExtra(expr)))
        button(frm, LEFT, 'pi', self.onPi)

    def onExtra(self, expr):
        try:
            self.text.set(self.eval.runsting(expr % self.text.get()))
        except:
            self.text.set('ERROR')

    def onPi(self):
        self.text.set(self.eval.runstring('pi'))

if __name__ == '__main__':
    CalcGuiPlus(**getCalcArgs()).mainloop()
