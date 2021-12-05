"""After click on the button we will see the message."""

# Call function on button click

from tkinter import *
from tkinter import messagebox

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Click on the button, and get the message')

def showMsg():
    messagebox.showinfo('Message', 'You clicked the Submitus button!')

button = Button(tkWindow,
                text = 'Submitus',
                command = showMsg)
button.pack()

tkWindow.mainloop()
