"""Tkinter buttons about."""

from tkinter import *

gui = Tk(className = 'Button example')
gui.geometry("500x200")

button = Button(gui,
                text = 'Sweet button',
                width = 40,
                height = 3,
                bg = '#0052cc',
                fg = '#ffffff',
                activebackground = '#0052cc',
                activeforeground = '#aaffaa'
                #command = ???
                # font = ???
                # image = ???
                )

button.pack()
gui.mainloop()
