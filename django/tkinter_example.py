""" Tkinter GUI."""

"""
# A button in right-up corner of screen.
from tkinter import *
def Call():
    msg = Label(window, text = "You pressed the button")
    msg.place(x = 30, y = 50)
    button["bg"] = "blue"
    button["fg"] = "white"

window = Tk()
window.geometry("200x110")
button = Button(text = "Press me", command = Call)
button.place(x = 30, y = 20, width=120, height=25)
window.mainloop()

# Creates a window that will act as the display, referred to as "window",
# adds a title and defines the size of the window.
window = Tk()
window.title("Window Title")
window.geometry("450x100")

# Adds text to the screen displaying the message shown.
label = Label(text = "Enter number: ")

# Creates a blank entry box. Entry boxes can be used by the user to input data
# or used to display output.
entry_box = Entry(text=0)

# Creates a message box which is used to display an output
output_box = Message(text=0)

# Specifies the background colour of the object.
output_box ["bg"] = "red"

# Specifies the style of the box. This can be flat, raised, sunken, grooved
# and ridged.
output_box ["relief"] = "sunken"

# Specifies the font colour of the object
output_box ["fg"] = "white"

# Creates a drop_down list box which can only contain strings
list_box = Listbox()

# Specifies the justification of the text in an entry box, but this does not
# work for message boxes.
entry_box ["justify"] = "center"

# Creates a button that will run the subprogram "click".
button1 = Button(text = "Click here", command = click)

# Specifies the position in which the object will appear in the window. If the
# position is not specified the item will not appear in the window.
label.place(x = 50, y = 20, width = 100, height = 25)

# Deletes the contents of an entry or list box.
entry_box.delete(0, END)

# Saves the contents of an entry box and stores it in a variable called num.
# This does not work with message boxes.
num = entry_box.get()

# Obtains the contents of a message box and stores it in a variable called
# ansver. This does not work with an entry box.
answer = output_txt["text"]

# Changes the content of a message box to display the value ot the variable 
# total.
output_txt["text"] = total

# This must be at the end of the program to make sure it keeps working.
window.mainloop()

# 124
# Create a window that will ask the user to enter their name. When they click
# on a button it should display the message "Hello" and their name and change
# the background colour and font colour of the message box.

from tkinter import *

def click():
    name = textbox1.get()
    message = str("Hello " + name)
    textbox2["bg"] = "yellow"
    textbox2["fg"] = "blue"
    textbox2["text"] = message

window = Tk()
window.geometry("500x200")

label1 = Label(text = "Enter your name:")
label1.place(x = 30, y = 20)

textbox1 = Entry(text = "")
textbox1.place(x = 150, y = 20, width = 200, height = 25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text = "Press me", command = click)
button1.place(x = 30, y = 50, width = 120, height = 25)

textbox2 = Message(text = "")
textbox2.place(x = 150, y = 50, width = 200, height = 25)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

window.mainloop()
"""
# 125
# Write a program that can be used instead of rolling a six-sided die in a
# board game. When the user clicks a button it should display a random whole
# number between 1 to 6 (inclusive).
from tkinter import *
import random

def click():
    num = random.randint(1, 6)
    answer["text"] = num

window = Tk()
window.title("Roll a dice")
window.geometry("100x120")

button1 = Button(text = "Roll", command = click)
button1.place(x = 30, y = 30, width = 50, height = 25)

answer = Message(text = "")
answer.place(x = 40, y = 70, width = 30, height = 25)

window.mainloop()

# 126


