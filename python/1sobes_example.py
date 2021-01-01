""" Simple practice questions for sobes."""

# 2D list
# Creates a multi-dimensional list. For instance, to create the following
# table of data:
#    0    1    2
#0   23   16   34
#1   45   29   48
number_list = [[23, 16, 35], [45, 29, 48]]

# Addition
# Adds two values together if they are numbers
total = num1 + num2
# or juins them if they contain text(see concatenation).
name = firstname + surname

# And
# Used to specify that both conditions must be met to return a true value.
if num > 10 and num < 20:
    print("In range")
else:
    print("Out of range")

# Append
# Adds a single item to the end of a list, tuple, dictionary, string or an array.
names_list.append("Timothy")

# Append to a file
# Opens an existing text or .csv file and allows data to be added to the end
# of the existing contents.
file = open("Countries.txt", "a")
file.write("France\n")
file.close

# Argument
# A value passed to a subprogram. In this example UserAns is the argument and
# would have been defined outside of the subprogram.
def CheckAnswer(UserAns):
    if UserAns == 20:
        print("Correct")
    else:
        print("Wrong")

#
