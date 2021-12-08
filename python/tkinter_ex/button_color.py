"""Change button background color after click."""

from tkinter import *

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Button color')


button = Button(tkWindow, text = 'Submit',
                          bg = '#ffffff',
                          activebackground = 'red')
button.pack()
tkWindow.mainloop()

# command = toggleColor ???
