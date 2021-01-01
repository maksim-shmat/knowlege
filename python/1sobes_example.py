""" Simple practice questions for sobes."""

# === 2D list
# Creates a multi-dimensional list. For instance, to create the following
# table of data:
#    0    1    2
#0   23   16   34
#1   45   29   48
number_list = [[23, 16, 35], [45, 29, 48]]

# === Addition
# Adds two values together if they are numbers
total = num1 + num2
# or juins them if they contain text(see concatenation).
name = firstname + surname

# === And
# Used to specify that both conditions must be met to return a true value.
if num > 10 and num < 20:
    print("In range")
else:
    print("Out of range")

# === Append
# Adds a single item to the end of a list, tuple, dictionary, string or an array.
names_list.append("Timothy")

# === Append to a file
# Opens an existing text or .csv file and allows data to be added to the end
# of the existing contents.
file = open("Countries.txt", "a")
file.write("France\n")
file.close

# === Argument
# A value passed to a subprogram. In this example UserAns is the argument and
# would have been defined outside of the subprogram.
def CheckAnswer(UserAns):
    if UserAns == 20:
        print("Correct")
    else:
        print("Wrong")

# === Array
# In Python arrays are similar to lists but they are only used to store
# numbers. The user defines the specific number type, i.e. integer, long,
# double or floating-point.
nums = aray ('i', [45, 324, 654, 45, 264])
print(nums)

# === Blob 
# A data type that is stored exactly as it was input. See SQL and database.

# === Button
# Used in GUI with Tkinter. The code below creates a button that will run the
# subprogram "click".
button1 = Button(text = "Click here", command = click)

# === Capitslize
# Change the case so the first letter is uppercase and all other letters are
# lower case.
print(name.capitalize())

# === Choice
# Select a random choice from a list of options.
selection = random.choice(['a', 'b', 'c'])

# === compiler 
# Translates a program written in high-level language such as Python into a
# low-level language such as machine code

# === Conditional statement
# Statement used to test out a condition. Commonly used in if statements,
# while and for loops.
if guess == num:

# === Count
# Counts the numbers of times a piece of data appears in a list, tuple, 
# dictionary, string or an array.
print(names_list.count("Sue"))

# === def
# Defines a subprogram.
def menu():
    print("1) Open")
    print("2) Close")
    selection = int(input("Selection: "))

# === double 
# Allows decimal places with numbers ranging from minus 10,308 to 10,308

# === elif 
# Used in an if statement to check a new condition if previous conditions
# have not been met.
if num < 10:
    print("Too low")
elif num > 20:
    print("Too high")
elif:
    print("In range")

# === else
# Used in an if statement to define what happens if the previous
# conditions have not been met.
if num < 10:
    print("Too low")
elif num > 20:
    print("Too high")
else:
    print("In range")

# === extend
# Adds multiple items to the end of a list, tuple, dictionary string or an
# array
names_list.extand(more_names)

# === for loop
# A type of loop which will repeat the block of code a set number of times.
for i in range(1,5):
    print(i)

# === If statement
# Checks to see if a condition is met; if it is it will perform the subsequent
# lines of code.
if num < 100:
    print("too low")

# === images 
# Images can be diwplayed using GUI. There are two ways images can be seen.
# In this first block of code the loop will be shown and this will not
# change as the program is running.
logo = PhotoImage(file = "logo.gif")
logoimage = Label(image = logo)
logoimage.place(x = 30, y = 20, width = 200, height = 120)
# In this second block of code the image will change depending on the value
# selected in an option menu.
photo = PhotoImage(file = "logo.gif")
photobox = Label(window, image = photo)
photobox.image = photo
photobox.place(x = 200, y = 200, width = 200, hight = 120)

# === Immutable
# Unchangeable. The value of immutable data cannot be altered after it has
# been created, e.g. the data in a tuple is immutable and therefore once a
# program starts running it cannot be changed.

# in Can be used to check a character is in a string. This is userul in both
# for and if statements. This is an example of a for statement which will
# print each character on a separate line:
for i in msg:
    print(i)
# Here is an example to see if a letter is within a string:
msg = input("Enter text: ")
letter = input("Enter letter: ")
if letter in msg:
    print("Think you")
else:
    print("Not in string")

# === Indent
# Used in Python to denote lines that belong to another statement. For
# instance, in a for loop the lines beneath it are indented as they are
# within the loop, the lines that are not indented are outside the loop.
for n in range(0,10):
    count = n + 1
    print(count)
print("The end")
# To indent a line, you can hit either the tab key or use the space bar.

# === Input
# Allow the user to input a value. This is usually assigned to a variable name
name = input("Enter name: ")

# === Insert
# Insert an item into a set position in the list and pushes everything else
# along to make space. This will change their index numbers according to their
# new position in the list.
names_list.insert(1, "Gray")

# === int
# Used to define a number as an integer.
num = int(input("Enter number: "))

# === Interpret
# To execute a program by translating it one line ant a time.

# === Nested
# A sequence inside another sequence, for instance a for loop may be inside
# an if statement and therefore the for loop is known as a nested statement
# inside the if statement.
if num < 20:
    for i in range(1, num):
        print(i)
    else:
        print("Too high")

# === Subprogram
# A block of code that can be called to run from another section of the
# program and can return a value.
def get_data():
    user_name = input("Enter your name: ")
    user_age = int(input("Enter age: "))
    data_tuple = (user_name, user_age)
    return data_tuple

def message(user_name, user_age):
    if user_age <= 10:
        print("Hi", user_name)
    else:
        print("Hello", user_name)

def main():
    user_name, user_age = get_data()
    message(user_name, user_age)

main()

# === While loop
# A type of loop that will repeat the block of code inside it(shown with
# indented rows) as long as a particular condition is being met.
total = 0
while total <= 50:
    num = int(input("Enter a number: "))
    total = total + num
    print("The total is ...", total)


