"""After click on the button we will see the message."""

# Call function on button click

from tkinter import *
from tkinter import messagebox

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Привет, там внизу есть кое что?')

def showMsg():
    messagebox.showinfo('WARNING!', 'Ты нажал на соску!')

button = Button(tkWindow,
                text = 'Привет, я Соска!',
                command = showMsg)
button.pack()

tkWindow.mainloop()
