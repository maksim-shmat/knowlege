import sys
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
import multiprocessing

class GuiMixin:
    def infobox(self, title, text, *args):
        return showinfo(title, text)

    def errorbox(self, text):
        showerror('Error, blya!', text)

    def question(self, title, text, *args):
        return askyesno(title, text)

    def notdone(self):
        showerror('Not implemented', 'Option not available')

    def quit(self):
        ans = self.question('Verify quit', 'Are you sure you want to quit?')
        if ans:
            Frame.quit(self)

    def help(self):
        self.infobox('RTFM', 'Cho blya, help? GUI sasi sabaka beshinaja!')

    def selectOpenFile(self, file="", dir="."):
        return askopenfilename(initialfile=file, initialdir=dir)
    def clone(self, args=()):
        new = Toplevel()
        myclass = self.__class__
        myclass(new, *args)

    def spawn(self, pycmdline, wait=False):
        if not wait:
            PortableLauncher(pycmdline, pycmdline)()
        else:
            System(pycmdline, pycmdline)()

    def browser(self, filename):
        new = Toplevel()
        text = ScrolledText(new, height=30, width=85)
        text.config(font=('courier', 10, 'normal'))
        text.pack(expand=YES, fill=BOTH)
        new.title('Text Viever')
        new.iconname('browser')
        text.insert('0.0', open(filename, 'r').read())

if __name__ == '__main__':
    class TestMixin(GuiMixin, Frame):
        def __init__(self, parent=None):
            Frame.__init__(self, parent)
            self.pack()
            Button(self, text='quit', command=self.quit).pack(fill=X)
            Button(self, text='help', command=self.help).pack(fill=X)
            Button(self, text='clone', command=self.clone).pack(fill=X)
            Button(self, text='other', command=self.other).pack(fill=X)

        def other(self):
            self.spawn('guimixin.py')

    TestMixin().mainloop()
