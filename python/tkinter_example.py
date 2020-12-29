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
# Create a program that will ask the user to enter a number in a box. When
# they click on a button it will add that number to a total and display it 
# in another box. This can be repeated as many times as they want and keep
# adding to the total. There should be another button that resets the total
# back to 0 and empties the original text box, ready for them to start again.

from tkinter import *

def add_on():
    num = enter_txt.get()
    num = int(num)
    answer = output_txt["text"]
    answer = int(answer)
    total = num + answer
    output_txt["text"] = total

def reset():
    total = 0
    output_txt["text"] = 0
    enter_txt.delete(0, END)
    enter_txt.focus()

total = 0
num = 0

window = Tk()
window.title("Adding Together")
window.geometry("450x100")

enter_lbl = Label(text = "Enter a number:")
enter_lbl.place(x = 50, y = 20, width = 100, height = 25)

enter_txt = Entry(text = 0)
enter_txt.place(x = 150, y = 20, width = 100, height = 25)
enter_txt["justify"] = "center"
enter_txt.focus()

add_btn = Button(text = "Add", command = add_on)
add_btn.place(x = 300, y = 20, width = 50, height = 25)

output_lbl = Label(text = "Answer = ")
output_lbl.place(x = 50, y = 50, width = 100, height = 25)

output_txt = Message(text = 0)
output_txt.place(x = 150, y = 50, width = 100, height = 25)
output_txt["bg"] = "white"
output_txt["relief"] = "sunken"

clear_btn = Button(text = "Clear", command = reset)
clear_btn.place(x = 300, y = 50, width = 50, height = 25)

window.mainloop()

# 127
# Create a window that will ask the user to enter a name in a text box.
# When they click on a button it will add it to the end of the list that
# is displayed on the screen. Create another button which will clear the
# list.

from tkinter import *

def add_name():
    name = name_box.get()
    name_list.insert(END, name)
    name_box.delete(0, END)
    name_box.focus()

def clear_list():
    name_list.delete(0, END)
    name_box.focus()

window = Tk()
window.title("Names list")
window.geometry("400x200")

label1 = Label(text = "Enter a name:")
label1.place(x = 20, y = 20, width = 100, height = 25)

name_box = Entry(text = 0)
name_box.place(x = 250, y = 20, width = 100, height = 25)
name_box.focus()

button1 = Button(text = "Add to list", command = add_name)
button1.place(x = 250, y = 20, width = 100, height = 25)

name_list = Listbox()
name_list.place(x = 120, y = 50 , width = 100, height = 100)

button2 = Button(text = "Clear list", command = clear_list)
button2.place(x = 250, y = 50, width = 100, height = 25)

window.mainloop()

# 128
# 1 kilometer = 0.6214 miles and 1 mile = 1.6093 kilometers. Using these 
# figures, make a program that will allow the user to convert between miles
# and kilometres.

from tkinter import *

def convert1():
    mile = textbox1.get()
    mile = int(mile)
    message = mile * 1.6093
    textbox2.delete(0, END)
    textbox2.insert(END, message)
    textbox2.insert(END, " kilometers")

def convert2():
    km = textbox1.get()
    km = int(km)
    message = km * 0.6214
    textbox2.delete(0, END)
    textbox2.insert(END, message)
    textbox2.insert(END, "miles")

window = Tk()
window.title("Distance")
window.geometry("260x200")

label1 = Label(text = "Enter the value you want to convert:")
label1.place(x = 30, y = 20)

textbox1 = Entry(text = "")
textbox1.place(x = 30, y = 50, width = 200, height = 25)
textbox1["justify"] = "center"
textbox1.focus()

convert1 = Button(text = "Convert miles to km", command = convert1)
convert1.place(x = 30, y = 80, width = 200, height = 25)

convert2 = Button(text = "Convert km to mile", command = convert2)
convert2.place(x = 30, y = 110, width = 200, height = 25)

textbox2 = Entry(text = "")
textbox2.place(x = 30, y = 140, width = 200, height = 25)
textbox2["justify"] = "center"

window.mainloop()

# 129
# Create a window that will ask the user to enter a number in a text box.
# When they click on a button it will use the code variable.isdigit() to 
# check to see if it is a whole number. If it is a whole number, add it to a
# list box, otherwise clear the entry box. Add another button that will clear
# the list.

from tkinter import *

def add_number():
    num = num_box.get()
    if num.isdigit():
        num_list.insert(END, num)
        num_box.delete(0, END)
        num_box.focus()
    else:
        num_box.delete(0, END)
        num_box.focus()

def clear_list():
    num_list.delete(0, END)
    num_box.focus()

window = Tk()
window.title("Number list")
window.geometry("400x200")

label1 = Label(text = "Enter a number:")
label1.place(x = 20, y = 20, width = 100, height = 25)

num_box = Entry(text = 0)
num_box.place(x = 120, y = 20, width = 100, height = 25)
num_box.focus()

button1 = Button(text = "Add to list", command = add_number)
button1.place(x = 250, y = 20, width = 100, height = 25)

num_list = Listbox()
num_list.place(x = 120, y = 50, width=100, height=100)

button2 = Button(text = "Clear list", command = clear_list)
button2.place(x = 250, y = 50, width = 100, height = 25)

window.mainloop()

# 130
# Alter program 129 to add a third button that will save the list to a .csv
# file. Tht code tmp_list = num_list.get(0, END) can be used to save the
# contents of a list box as a tuple called tmp_list.

from tkinter import *
import csv

def add_number():
    num = num_box.get()
    if num.isdigit():
        num_list.insert(END, num)
        num_box.delete(0, END)
        num_box.focus()
    else:
        num_box.delete(0, END)
        num_box.focus()

def clear_list():
    num_list.delete(0, END)
    num_box.focus()

def save_list():
    file = open("numbers.csv", "w")
    tmp_list=num_list.get(0, END)
    item = 0
    for x in tmp_list:
        newrecord = tmp_list[item] + "\n"
        file.write(str(newrecord))
        item = item + 1
    file.close()

window = Tk()
window.title("Number list")
window.geometry("400x200")

label1 = Label(text = "Enter a number:")
label1.place(x = 20, y = 20, width = 100, height = 25)

num_box = Entry(text = 0)
num_box.place(x = 120, y = 20, width = 100, height = 25)
num_box.focus()

button1 = Button(text = "Add to list", command = add_number)
button1.place(x = 250, y = 20, width = 100, height = 25)

num_list = Listbox()
num_list.place(x = 120, y = 50, width = 100, height = 100)

button2 = Button(text = "Clear list", command = clear_list)
button2.place(x = 250, y = 50, width = 100, height = 25)

button3 = Button(text = "Save list", command = save_list)
button3.place(x = 250, y = 80, width = 100, height = 25)

window.mainloop()

# 131
# Create a program that will allow the user to create a new .csv file.
# It should ask them to enter the name and age of a person and then
# allow them to add this to the end of the file they have just created.

from tkinter import *
import csv

def create_new():
    file = open("ages.csv", "w")
    file.close()

def save_list():
    file = open("ages.csv", "a")
    name = name_box.get()
    age = age_box.get()
    newrecord = name + "," + age + "\n"
    file.write(str(newrecord))
    file.close()
    name_box.delete(0, END)
    age_box.delete(0, END)
    name_box.focus()

window = Tk()
window.title("People List")
window.geometry("400x100")

label1 = Label(text = "Enter a name:")
label1.place(x = 20, y = 20, width = 100, height = 25)

name_box = Entry(text = "")
name_box.place(x = 120, y = 20, width = 100, height = 25)
name_box ["justify"] = "left"
name_box.focus()

label2 = Label(text = "Enter their age:")
label2.place(x = 20, y = 50, width = 100, height = 25)

age_box = Entry(text = "")
age_box.place(x = 120, y = 50, width = 100, height = 25)
age_box["justify"] = "left"

button1 = Button(text = "Create new file", command = create_new)
button1.place(x = 250, y = 50, width = 100, height = 25)

button2 = Button(text = "Add to file", command = save_list)
button2.place(x = 250, y = 50, width = 100, height = 25)

window.mainloop()

# 132
# Using the .csv file you created for the last challenge, create a program
# that will allow people to add names and ages to the list and create a
# button that will display the contents of the .csv file by importing it to a
# list box.

from tkinter import *
import csv

def save_list():
    file = open("ages.csv", "a")
    name = name_box.get()
    age = age_box.get()
    newrecord = name + "," + age + "\n"
    file.write(str(newrecord))
    file.close()
    name_box.delete(0, END)
    age_box.delete(0, END)
    name_box.focus()

def read_list():
    name_list.delete(0, END)
    file = list(csv.reader(open("ages.csv")))
    tmp = []
    for row in file:
        tmp.append(row)
    x = 0
    for i in tmp:
        data = tmp[x]
        name_list.insert(END, data)
        x = x + 1

window = Tk()
window.title("People List")
window.geometry("400x200")

label1 = Label(text = "Enter a name:")
label1.place(x = 20, y = 20, width = 100, height = 25)

name_box = Entry(text = "")
name_box.place(x = 120, y = 20, width = 100, height = 25)
name_box["justify"] = "left"
name_box.focus()

label2 = Label(text = "Enter their age:")
label2.place(x = 20, y = 50, width = 100, height = 25)

age_box = Entry(text = "")
age_box.place(x = 120, y = 50, width = 100, height = 25)
age_box["justify"] = "left"

button1 = Button(text = "Add to file", command = save_list)
button1.place(x = 250, y = 20, width = 100, height = 25)

button2 = Button(text = "Read list", command = read_list)
button2.place(x = 250, y = 50, width = 100, height = 25)

label3 = Label(text = "Saved Names:")
label3.place(x = 20, y = 80, width = 100, height = 25)

name_list = Listbox()
name_list.place(x = 120, y = 80, width = 230, height = 100)

window.mainloop()

# Tkinter support only .git
# Change the icon displayed in the title of the window.
window.wm_iconbitmap("MyIcon.ico")  # for Windows?

# Change the background colour of the window, in this case to light green.
window.configure(background = "light green")

# Displays an image in a label widget. This image will not change while the
# program is running.
logo = PhotoImage(file = "logo.gif")
logoimage = Label(image = logo)
logoimage.place(x = 30, y = 20, width = 200, height = 120)

# This is similar to the block above but as we want the image to change as
# we update the data we need to add the code photobox.image = photo, which
# makes it updatable.
photo = PhotoImage(file = "logo.gif")
photobox = Label(window, image = photo)
photobox.image = photo
photobox.place(x = 30, y = 20, width = 200, height = 120)

# Creates a variable called selectName which will store a string where the 
# original value of the variable is "SelectName". It will then create a
# drop-down option menu which stores the value the user selects in the 
# selectNames variable and displays the values in the list: Bob, Sue and Tom.
selectName = StringVar(window)
selectName.set("Select Name")
namesList = OptionMenu(window, selectName, "Bob", "Sue", "Tom")
namesList.place(x = 30, y = 250)

# In this example, when a button is clicked it will run the "clicked" 
# subprogram. This will obtain the value from the selctName variable and
# create a message that will be displayed in a label. It will then check to
# see which option has been selected and change the picture to the correct
# image, which is displayed in the photo variable. If no name is selected it
# will simply show the logo.

def clicked():
    sel = selectName.get()
    mseg = "Hello " + sel
    mlabel["text"] = mesg
    if sel == "Bob":
        photo = PhotoImage(file = "Bob.git")
        photobox.image = photo
    elif sel == "Sue":
        photo = PhotoImage(file = "Sue.gif")
        photobox.image = photo
    elif sel == "Tim":
        photo = PhotoImag(file = "Tim.gif")
        photobox.image = photo
    else:
        photo = PhotoImage(file = "logo.gif")
        photobox.image = photo
        photobox["image"] = photo
        photobox.update()

# 133
# Create your own icon that consists of several vertical multi-coloured lines.
# Create a logo which measures 200x150, using Paint or another graphics
# package. Create the following window using your own icon and logo.
# When the user enters their name and clicks on the Press Me button it should
# display "Hello" and their name in the second text box.

