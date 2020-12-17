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
"""
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
