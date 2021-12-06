"""Change font of button."""

from tkinter import *
import tkinter.font as font

gui = Tk(className='Change font button about')
gui.geometry("500x200")

# define font
#myFont = font.Font(size=30)
#myFont = font.Font(weight="bold")
myFont = font.Font(family='Chilanka', size=20, weight='bold')

# create button
button = Button(gui, text="Click", bg='#0052cc', fg='#ffffff')
# apply font to the button label
button['font'] = myFont
# add button to gui window
button.pack()

gui.mainloop()
