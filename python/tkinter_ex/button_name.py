"""Change test of button."""

from tkinter import *

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Change button`s name')

def toggleText():
    if(button['text']=='Submit'):
        button['text']='Submitted'
    else:
        button['text']='Submit'

button = Button(tkWindow,
                text = 'Submit',
                command = toggleText)

button.pack()

tkWindow.mainloop()
