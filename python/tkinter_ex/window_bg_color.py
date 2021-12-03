"""Change background color."""

from tkinter import *

gui = Tk(className='Window color example')
gui.geometry("400x200")
#gui.configure(bg='blue')
#gui['bg'] = 'green'
#gui['background'] = 'purple'
gui['background'] = '#856ff8'
gui.mainloop()
