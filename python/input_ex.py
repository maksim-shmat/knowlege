""" There is a victorina, man."""
"""
# 001
firstname = input("Please inter your first name: ")
print("Hello",firstname)

# 002
firstname = input("Please enter your first name: ")
surname = input("Please enter your surname: ")
print("Hello",firstname, surname)

# 003
print("What do you call a bear with no teeth?\nA gummy bear!")

### x = input('What do you call a bear with no teeth?\n')
print('\nNo', x, '\nA gummy bear!')

# 004
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
answer = num1 + num2
print("The answer is", answer)

# 005
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
num3 = int(input("Please enter your third number: "))
answer = (num1 + num2) * num3
print("The answer is", answer)

# 006
startNum = int(input("Enter the number of slices of pizza you started with: "))
endNum = int(input("How many slices have you eaten? "))
slicesLeft = startNum - endNum
print("You have", slicesLeft, "slices remaining")

# 007
name = input("What is your name? ")
age = int(input("How old are you? "))
newAge = age + 1
print(name, "next birthday you will be", newAge)

# 008

bill = int(input("What is the total cost of the bill? "))
people = int(input("How many people are there? "))
each = bill/people
print("Each person should pay $", each)

# 009

days = int(input("Enter the number of days: "))
hours = days*24
minutes = hours*60
seconds = minutes*60
print("In", days,"days there are...")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")

# 010

kilo = int(input("Enter the number of kilo: "))
pound = kilo * 2.204
print("That is", pound, "pounds")

# 011

larger = int(input("Enter a number over 100: "))
smaller = int(input("Ente a number under 10: "))
answer = larger//smaller
print(smaller, "goes into", larger, answer, "times")

# 012

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)

# 013

num = int(input("Enter a value less than 20: "))
if num >= 20:
    print("Too high")
else:
    print("Thank you")

# 014

num = int(input("Enter a value between 10 and 20: "))
if num >= 10 and num <= 20:
    print("Thank you")
else:
    print("Incorrect answer")

# 015

colour = input("Type in your favorite colour: ")
if colour == "red" or colour == "RED" or colour == "RED":
    print("I like red too.")
else:
    print("I don`t like that colour, Prefer red")

# 016

raining = input("Is it raining? ")
raining = str.lower(raining)
if raining == "yes":
    windy = input("Is it windy? ")
    windy = str.lower(windy)
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")

# 017

age = int(input("What is your age? "))
if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print("You can buy a lottery ticket")
else:
    print("You can go Trick-or-Treating")

# 018

num = int(input("Enter a number: "))
if num < 10:
    print("Too low")
elif num >= 10 and num <= 20:
    print("Correct")
else:
    print("Too high")

# 019

num = input("Enter 1, 2 or 3: ")
if num == "1":
    print("Thank you")
elif num == "2":
    print("Well done")
elif num == "3":
    print("Correct")
else:
    print("Error message")

# 020

name = input("Enter your first name: ")
length = len(name)
print(length)

# 021

firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")
name = firstname + " " + surname
length = len(name)
print(name)
print(length)

# 022

firstname = input("Enter your first name in lowercase: " )
surname = input("Enter your surname in lowercase: " )
firstname = firstname.title()
surname = surname.title()
name = firstname + " " + surname
print(name)

# 023

phrase = input("Enter the first line of a nursery rhyme: ")
length = len(phrase)
print("This has", length, "letters in it")
start = int(input("Enter a starting number: "))
end = int(input("Enter an end number: "))
part = (phrase[start:end])
print(part)

# 024

word = input("Enter a word: ")
word = word.upper()
print(word)

# 025

name = input("Enter your first name: ")
if len(name) < 5:
    surname = input("Enter your surname: ")
    name = name+surname
    print(name.upper())
else:
    print(name.lower())

# 026

word = input("Please enter a word: ")
first = word[0]
length = len(word)
rest = word[1:length]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newword = rest + first + "ay"
else:
    newword = word + "way"
print(newword.lower())

# 027

num = float (input("Enter a number with lots of decimal places: "))
print(num*2)

# 028

num = float(input("Enter a number with lots of decimal places: "))
answer = num*2
print(answer)
print(round(answer, 2))

# 029

import math
num = int(input("Enter a number over 500: "))
answer = math.sqrt(num)
print(round(answer, 2))

# 030

import math
print(round(math.pi, 5))

# 031

import math
radius = int(input("Enter the radius of the circle: "))
area = math.pi*(radius**2)
print(area)

# 032

import  math
radius = int(input("Enter the radius of the circle: "))
depth = int(input("Enter depth: "))
area = math.pi*(radius**2)
volume = area*depth
print(round(volume,3))

# 033

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
ans1 = num1//num2
ans2 = num1%num2
print(num1, "divided by", num2, "is", ans1, "with", ans2, "remaining.")

# 034

print("1) Square")
print("2) Triangle")
print()
menuselection = int(input("Enter a number: "))
if menuselection == 1:
    side = int(input("Enter the length of one side: "))
    area = side*side
    print("The area of your chosen shape is", area)
elif menuselection == 2:
    base = int(input("Enter the length of the base: "))
    height = int(input("Enter the height of the triangle: "))
    area = (base*height)/2
    print("The area of your chosen shape is", area)
else:
    print("Incorrect option selected")

# 035

name = input("Type in your name: ")
for i in range(0,3):
    print(name)

# 036

name = input("Type in your name: ")
number = int(input("Enter a number: "))
for i in range (0, number):
    print(name)

# 037

name = input("Enter your name: ")
for i in name:
    print(i)

# 038

num  = int(input("Enter a number: "))
name = input("Enter your name: ")
for x in range(0, num):
    for i in name:
        print(i)

# 039

num = int(input("Enter a number between 1 and 12: "))
for i in range(1, 13):
    answer = i * num
    print(i, "x", num, "=", answer)

# 040

num = int(input("Enter a number below 50: "))
for i in range(50, num-1, -1):
    print(i)

# 041
# Ask the user to enter their name and a number. If the number is less than
# 10, then display their name that number of times; otherwise display the
# message "Too high" three times.

name = input("Enter your name: ")
num = int(input("Enter a number: "))
if num < 10:
    for i in range(0, num):
        print(name)
else:
    for i in range(0,3):
        print("Too high")

# 042
# Set a variable called total to 0. Ask the user to enter five numbers and
# after each input ask them if they want that number included. If they do,
# then add the number to the total. If they do not want it included, don't
# add it to the total. After they have entered all five numbers, display the
# total.

total = 0
for i in range(0, 5):
    num = int(input("Enter a number: "))
    ans = input("Do you want this number included? (y/n)")
    if ans == "y":
        total = total + num
print(total)

# 043
# Ask which direction the user wants to count (up or down). If they select up,
# then ask them for top number and then count from 1 to that number. If they
# select down, ask them to enter a number below 20 and then count down from
# 20 to that number. If they entered something other than up or down, display
# the message "I dont`t understand".

direction = input("Do you want to count up or down? (u/d) ")
if direction == "u":
    num = int(input("What is the top number? "))
    for i in range(1, num+1):
        print(i)
elif direction == "d":
    num = int(input("Enter a number below 20: "))
    for i in range(20, num-1, -1):
        print(i)
else:
    print("I don`t understand")

# 044
# Ask how many people the user wants to invite to a party. If they enter a 
# number below 10, ask for the names and after each name display "[name] has
# been invited". If they enter a number which is 10 or higher, display the
# message "Too many people".

num = int(input("How many friends do you want to invite to the party?"))
if num < 10:
    for i in range(0, num):
        name = input("Enter a name: ")
        print(name, "has been invited")
else:
    print("Too many people")

# just example loop while

again = "yes"
while again == "yes":
    print('Hello')
    again = input("Do you want to loop again? ")

# and more
total = 0
while total < 100:
    num = int(input("Enter a number: "))
    total = total + num
print("The total is ", total)

# 045
# Set the total to 0 to start with. While th total is 50 ot less, ask the
# user to input a number. Add that number to the total and print the message
# "The total is...[total]". Stop loop when the total is over 50.

total = 0
while total <= 50:
     num = int(input("Enter a number: "))
     total = total + num
     print("The total is...", total)

# 046
# Ask the user to inter a number. Keep asking until they enter a vlue over
# 5 and then display the number you entered was a [number]" and sntop the
# progtram.

num = 0
while num <= 5:
    num = int(input("Enter a number: "))
print("The last number you entered was a", num)

# 047
# Ask the user to enter a number and then enter another number. Add these two
# numbers together and then ask if they want to add another number. If they
# enter "y", ask them to enter another number and keep adding numbers "y". 
# Once the loop has stopped, display the total.

num1 = int(input("Enter a number: "))
total = num1
again = "y"
while again == "y":
    num2 = int(input("Enter another number: "))
    total = total + num2
    again = input("Do you want to add another number? (y/n)")
    print("The total is ", total)

# 048

# Ask for the name of somebody the use wants to invite to a party. After this,
# display the message "[name] has now been invited" and add 1 to the count.
# Then ask if they want to invite somebody else. Keep repeating this until
# they no longer want to invite anyone else to the party and then display how
# many people they have coming to the party.

again = "y"
count = 0
while again =="y":
    name = input("Enter a name of sombody you want to invite to your party: ")
    print(name, "has now been invited")
    count = count + 1
    again = input("Do you want to invite somebody else? (y/n) ")
print("You have", count, "people coming to your party")
"""
# 049

# Create a variable called compnum and set the value to 50. Ask the user to
# enter a number. While their guess is not the same as the compnum value,
# tell them if their guess is too low or too high and ask them to have
# another guess. If they enter the same value as compnum, display the
# message "Well done, you took [count] attempts".

compnum = 50
guess = int(input("Can you guess the number I am thinking of? "))
count = 1
while guess != compnum:
    if guess < compnum:
        print("Too low")
    else:
        print("Too high")
    count = count+1
    guess = int(input("Have another guess: "))
print("Well done, you took", count, "attempts")

# 050

# Ask the user to enter a number between 10 and 20. If they enter a value
# under 10, display the message "Too low " and ask them to try again. If
# they enter a value above 20, display the message "To high" and ask them
# to try again. Keep repeating this until they enter a value that is 
# between 10 and 20 and then display the message "Thank you".

num = int(input("Enter a number between 10 and 20: "))
while num < 10 or num > 20:
    if num < 10:
        print("Too low")
    else:
        print("Too high")
    num = int(input("Try again: "))
print("Thank you")

# 051

# Using the song "10 green bottles", display the lines "Ther are[num] green
# bottles hanging on the wall, [num] green bottles hanging on the wall, and if
# 1 green bottle should accidentally fall". Then ask the question "how many 
# green bottles will be hanging on the wall?" If the user answers correctly,
# display the message "There will be hanging on the wall?" If they answer
# incorrectly, display the message "No, try again" until they get it right.
# When the number of green bottles gets down to 0, display the message
# "There are no more green bottles hanging on the wall"

num = 10
while num > 0:
    print("There are ", num, "green bottles hanging on the wall. ")
    print(num, "green bottles hanging on the wall. ")
    print("And if 1 green bottle should accidently fall,")
    num = num - 1
    answer = int(input("How many green bottles will be hanging on the wall? "))
    if answer == num:
        print("There will be", num, "green bottles hanging on the wall. ")
    else:
        while answer != num:
            answer = int(input("No, try again: "))
print("There are no more green bottles hanging on the wall. ")

=======================

"""Input integer."""

# read integer from user
n1 = int(input('Enter a number: '))
n2 = int(input('Ener another number: '))

print('The sum of two numbers is:', n1+n2)

#read integer from user
n1 = int(input('Enter a number: '))
print(type(n1))

==========================

""" Docs. """

name_age = {}
for i in range(3):
    name = input("Name? ")
    age = int(input("Age? "))
    name_age[name] = age
name_choice = input("Name to find? ")
print(name_age[name_choice])

######1 input with float

x = float(input('Enter a float : '))
print('You entered : ', x)

#2 input with long string

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"  # add more to variable 'prompt'
name = input(prompt)
print(f"\nHello, {name}!")

resutls:
    If you tell us who you are, we can personalize the messages you see.
    What is you first name? Vibldr

    Hello, Vibldr!

#3
