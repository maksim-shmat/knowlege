""" Tkinter GUI."""

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

###########

