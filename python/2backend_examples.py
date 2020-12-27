""" About backend cases part two."""

"""
# 120
# Display the following menu to the user:
# 1) Addition
# 2) Subtraction
# Enter 1 or 2:
# If they ener a 1, it should run a subprogram that will generate two random
# numbers between 5 and 20, and ask the user to add them together. Work out
# the correct answer and return both the user's answer and the correct answer.
# If they intered 2 as their selection on the menu, it should run a 
# subprogram that wil generate one number between 25 and 50 and another
# number between 1 and 25 and ask them to work out num 1 minus num 2. This
# way they will not have to worry about negative answers. Return both the
# user's answer and the correct answer.
# Create another subprogram that will check if the user's answer matches the
# actual answer. If it does, display "Correct", otherwise display a message
# that will say "Incorrect, the answer is" and display the real answer.
# If they do not select a relevant option on the first menu you should display
# a suitable message.

import random

def addition():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    print(num1, "+", num2, "= ")
    user_answer = int(input("Your answer: "))
    actual_answer = num1 + num2
    answers = (user_answer, actual_answer)
    return answers

def subtraction():
    num3 = random.randint(25, 50)
    num4 = random.randint(1, 25)
    print(num3, "-", num4, "= ")
    user_answer = int(input("Your answer: "))
    actual_answer = num3 - num4
    answers = (user_answer, actual_answer)
    return answers

def check_answer(user_answer, actual_answer):
    if user_answer == actual_answer:
        print("Correct")
    else:
        print("Incorrect, the answer is", actual_answer)

def main():
    print("1) Addition")
    print("2) Subtraction")
    selection = int(input("Enter 1 or 2: "))
    if selection == 1:
        user_answer, actual_answer = addition()
        check_answer(user_answer, actual_answer)
    elif selection == 2:
        user_answer, actual_answer = subtraction()
        check_answer(user_answer, actual_answer)
    else:
        print("Incorrect selection")

main()

# 121
# Create a program that will allow the user to easily manage a list of names.
# You should display a menu that will allow them to add a name to the list,
# change a name in the list, delete a name from the list or view all the 
# names in the list. There should also be a menu option to allow the user to
# end the program. If they selct an option that is not relevant, then it 
# should display a suitable message. After they have made a selection to 
# either add a name, change a name, delete a name or view all the names, they
# should see the menu again without having to restart the program. The program
# should be made as easy to use as possible.

def add_name():
    name = input("Enter a new name: ")
    names.append(name)
    return names

def change_name():
    num = 0
    for x in names:
        print(num, x)
        num = num + 1
    select_num = int(input("Enter the number of the name you want to change: "))
    name = input("Enter new name: ")
    names[select_num] = name
    return names

def delete_name():
    num = 0
    for x in names:
        print(num, x)
        num = num + 1
    select_num = int(input("Enter the number of the name you want to delete: "))
    del names[select_num]
    return names

def view_names():
    for x in names:
        print(x)
    print()

def main():
    again = "y"
    while again == "y":
        print("1) Add a name")
        print("2) Change a name")
        print("3) Delete a name")
        print("4) View names")
        print("5) Quit")
        selection = int(input("What do you want to do? "))
        if selection == 1:
            names = add_name()
        elif selection == 2:
            names = change_name()
        elif selection == 3:
            names = delete_name()
        elif selection == 4:
            names = view_names()
        elif selection == 5:
            again = "n"
        else:
            print("Incorrect option: ")
        data = (names, again)

names = []
main()
"""
# 122
# Create the following menu:
# 1) Add to file
# 2) View all records
# 3) Quit program
# Enter the number of your selection:
# If the user selects 1, allow them to add to a file called Salaries.csv 
# which will store their name and salary. If they select 2 it should display
# all records in the Salaries.csv file.  If they select 3 it should stop the
# program. if they select an incorrect option they should see an error
# message. They should keep returning to the menu until they select option 3.

import csv

def addtofile():
    file = open("Salaries.csv", "a")
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    newrecord = name + ", " + str(salary) + "\n"
    file.write(str(newrecord))
    file.close()

def viewrecords():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()

tryagain = True
while tryagain == True:
    print("1) Add to file")
    print("2) View all records")
    print("3) Quit program")
    print()
    selection = input("Enter the number of your selction: ")
    if selection == "1":
        addtofile()
    elif selection == "2":
        viewrecords()
    elif selection == "3":
        tryagain = False
    else:
        print("Incorrect option")

# 123
