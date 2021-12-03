""" GUI with Tkinter

Create program that have two fields, one for input integers, second for
visualisation inputing. And two buttons: one - "View Times Table", second -
"Clear".

When the user enters a number in the first box and clicks on the "View Times
Table" button it should show the times table in the list area.

For instance, if the user entered 99 they would see the list as shown in the
example on the right.

The "Clear" button should clear both boxes.

=== Problems You Will Have to Overcome ===

You want to display the number sentence in the list rather than just the
answers. The following line of code may help you do this:
    num_list.insert(END,(i, "x", num, "=", answer))

Make sure it is as easy to use as possible by making sure the focus is in the 
correct location.
"""
from tkinter import *

def show_table():
    num = num_box.get()
    num = int(num)
    value = 1
    for i in range(1, 13):
        answer = i * num
        num_list.insert(END,(i, "x", num, "=", answer))
        value = value + 1
    num_box.delete(0, END)
    num_box.focus()

def clear_list():
    num_box.delete(0, END)
    num_list.delete(0, END)
    num_box.focus()

window = Tk()
window.title("Times Table")
window.geometry("400x280")

label1 = Label(text = "Enter a number:")
label1.place(x = 20, y = 20, width = 100, height = 25)

num_box = Entry(text = 0)
num_box.place(x = 120, y = 20, width = 100, height = 25)
num_box.focus()

button1 = Button(text = "View Times Table", command = show_table)
button1.place(x = 250, y = 20, width = 120, height = 25)

num_list = Listbox()
num_list.place(x = 120, y = 50, width = 100, height = 200)

button2 = Button(text = "Clear", command = clear_list)
button2.place(x = 250, y = 50, width = 120, height = 25)

window.mainloop()
