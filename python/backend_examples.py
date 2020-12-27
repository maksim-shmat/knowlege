""" Tuples, lists and dictionaries."""

"""
# 069
# Create a tuple containing the names of five countries and display the whole
# tuple. Ask the user to enter one of the countries that have been shown to 
# them and then display the index number(i.e. position in the list) of that
# item in the tuple.

country_tuple = ("France", "England", "Spain", "Germany", "Australia")
print(country_tuple)
print()
country = input("Please enter one of the countries from above: ")
print(country, "has index number", country_tuple.index(country))

# 070
# Add to program 069 to ask the user to enter a number and display the 
# country in that position.

country_tuple = ("France", "England", "Spain", "Germany", "Australia")
print(country_tuple)
print()
country = input("Please enter one of the countries from above: ")
print(country, "has index number", country_tuple.index(country))
print()
num = int(input("Enter a number between 0 and 4: "))
print(country_tuple[num])

# 071
# Create a list of two sports. Ask the user what their favourite sport is
# and add this to the end of the list. Sort the list and display it.

sports_list = ["tennis", "football"]
sports_list.append(input("What is your favourite sport? "))
sports_list.sort()
print(sports_list)

# 072
# Create a list of six shcool subjects. Ask the user which of these
# subjects they don't like. Delete the subject they have chosen from the
# list before you display the list again.

subject_list = ["maths", "english", "computing", "history", "science", "spanish"]
print(subject_list)
dislike = input("Which of these subjects do you dislike? ")
getrid = subject_list.index(dislike)
del subject_list[getrid]
print(subject_list)

# 073
# Ask the user to enter four of their favorite foods and store them in
# a dictionary so that they are indexed with numbers starting from 1.
# Display the dictionary in full, showing the index number and the item.
# Ask them which they want to get rid of and remove it from the list.
# Sort the remaining data and display the dictionary.

food_dictionary = {}
food1 = input("Enter a food you like: ")
food_dictionary[1] = food1
food2 = input("Enter another food you like: ")
food_dictionary[2] = food2
food3 = input("Enter a third food you like: ")
food_dictionary[3] = food3
food4 = input("Enter one last food you like: ")
food_dictionary[4] = food4
print(food_dictionary)
dislike = int(input("Which of these do you want to get rid of? "))
del food_dictionary[dislike]
print(sorted(food_dictionary.values()))

# 074
# Enter a list of ten colours. Ask the user for a srarting number between 0 
# and 4 and an end number between the start and end numbers the user input.

colours = ["red", "blue", "green", "black", "white", "pink", "grey",
        "purple", "yellow", "brown"]
start = int(input("Enter a starting number(0-4): "))
end = int(input("Enter an end number (5-9): "))
print(colours[start: end])

# 075
# Create a list of four three-digit numbers. Display the list to the user,
# showing each item from the list on a separate line. Ask the user to enter a
# three-digit number. If the number they have typed in matches one in the
# list, display the position of that number in the list, otherwise display
# the message "That is not in the list".

nums = [123, 345, 234, 765]
for i in nums:
    print(i)
selection = int(input("Enter a number from the list: "))
if selection in nums:
    print(selection, "is in position", nums.index(selection))
else:
    print("That is not in the list")

# 076
# Ask the user to enter the names of three people they want to invite
# to a party and store them in a list. After they have entered all three
# names, ask them if they want to add another. If they do, allow them to
# add more names until they answer "no". When they answer "no", display how
# many people they have invited to the party.

name1 = input("Enter a name of somebody you want to invite to your party: ")
name2 = input("Enter another name: ")
name3 = input("Enter a third name: ")
party = [name1, name2, name3]
another = input("Do you want to invite another (y/n): ")
while another == "y":
    newname = party.append(input("Enter another name: "))
    another = input("Do you want to invite another (y/n): ")
print("You have", len(party), "people coming to your party")

# 077
# Change program 076 so that once the user has completed their list of names,
# display the full list and ask them to type in one of the names on the list.
# Display the position of that name in the list. Ask the user if they still
# want that person to come to the party. If they answer "no", delete that
# entry from the list and display the list again.

name1 = input("Enter a name of somebody you want to invite to your party: ")
name2 = input("Enter another name: ")
name3 = input("Enter a third name: ")
party = [name1, name2, name3]
another = input("Do you want to invite another (y/n): ")
while another == "y":
    newname = party.append(input("Enter another name: "))
    another = input("Do you want to invite another (y/n): ")
print("You have", len(party), "people coming to your party")
print(party)
selection = input("Enter one of the names: ")
print(selection, "is in position", party.index(selection), "on the list")
stillcome = input("Do you still want them to come (y/n): ")
if stillcome == "n":
    party.remove(selection)
print(party)

# 078
# Create a list containing the titles of four TV programmes and display
# them on separate lines. Ask the user to enter another show and a position
# they want it itserted into the list. Display the list again, showing all
# five TV programmes in their now positions.

tv = ["Task Master", "Top Gear", "The Big Bang Theory", "How I Met Your Mother"]
for i in tv:
    print(i)
print()
newtv = input("Enter another TV show: ")
position = int(input("Enter a number between 0 and 3: "))
tv.insert(position, newtv)
for i in tv:
    print(i)

# 079
# Create an empty list called "nums". Ask the user to enter numbers. After
# each number is entered, add it to the end of the nums list and display the
# list. Once they have entered three numbers, ask them if they still want the
# last number they entered saved. If they say "no", remove the last item from
# the list. Display the list of numbers.

nums = []
count = 0
while count <3:
    num = int(input("Enter a number: "))
    nums.append(num)
    print(nums)
    count = count + 1
lastnum = input("Do you want the last number saved (y/n): ")
if lastnum == "n":
    nums.remove(num)
print(nums)

# 080
# Ask the user to enter their first name and then display the length of then
# first name. Then ask for their surname and
# display the length of their surname. Join their first name and surname
# together with a space between and display the result. Finally, display the
# length of their full name(including the space).

fname = input("Enter your first name: ")
print("That has", len(fname), "characters in it")
sname = input("Enter your surname: ")
print("That has", len(sname), "characters in it")
name = fname + " " + sname
print("Your full name is", name)
print("That has", len(name), "characters in it")

# 081
# Ask the user to type in their favorite school subject. Display it with '-"
# after each letter, e.g. S-p-a-n-i-s-h-.

subject = input("Enter your favorite school subject: ")
for letter in subject:
    print(letter, end = "-")

# 082
# Show the user a line of text from your favorite poem and ask for a 
# starting and ending point. Display the characters between those two points.

poem = "Oh, I wish I'd looked after me teeth,"
print(poem)
start = int(input("Enter a starting number: "))
end = int(input("Enter an end number: "))
print(poem[start:end])

# 083
# Ask the user to type in a word in upper case. If they type it in lower
# case, ask them to try again. Keep repeating this until they type in a 
# message all in uppercase.

msg = input("Enter a message in uppercase: ")
tryagain = False
while tryagain == False:
    if msg.isupper():
        print("Thank you")
        tryagain = True
    else:
        print("Try again")
        msg = input("Enter a message in uppercase: ")

# 084
# Ask the user to type in their postcode. Display the first two letters in 
# uppercase.

postcode = input("Enter your postcode: ")
start = postcode[0:2]
print(start.upper())

# 085
# Ask the user to type in their name and then tell them how many vowels are
# in their name.

name = input("Enter your name: ")
count = 0
name = name.lower()
for x in name:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        count = count + 1
print("Vowels =", count)

# 086
# Ask the user to enter a new password. Ask them to enter it again. If the
# two passwords match, display "Thank you". If the letters are correct but
# in the wrong case, display the message "They must be in the same case",
# otherwise display the message "incorrect".

pswd1 = input("Enter a password: ")
pswd2 = input("Enter it again: ")
if pswd1 == pswd2:
    print("Thank you")
elif pswd1.lower() == pswd2.lower():
    print("They must be the same case")
else:
    print("Incorrect")

# 087
# Ask the user to type in a word and then display it backwards on separate
# lines. For instance, if they type in "Hello" it should display as shown
# below in reverse column.

word = input("Enter a word: ")
length = len(word)
num = 1
for x in word:
    position = length - num
    letter = word[position]
    print(letter)
    num = num + 1

# -------- Arrays --------
# 088
# Ask the user for a list of five integers. Store them in an array. Sort the
# list and display it in reverse order.

from array import *

nums = array('i', [])
for i in range(0, 5):
    num = int(input("Enter a number: "))
    nums.append(num)
nums = sorted(nums)
nums.reverse()
print(nums)

# 089
# Create an array which will store a list of integers. Generate five random
# numbers and store them in the array. Display the array(showing each item
# on a separate line).

from array import *
import random

nums = array('i', [])
for i in range(0, 5):
    num = random.randint(1, 100)
    nums.append(num)

for i in nums:
    print(i)

# 090
# Ask the user to enter numbers. If they enter a number between 10 and 20,
# save it in the array, otherwise display the message "Outside the range".
# Once five numbers have been successfully added, display the message "Thank
# you" and display the array with each item shown on a separate line.

from array import *

nums = array('i', [])
while len(nums) < 5:
    num = int(input("Enter a number between 10 and 20: "))
    if num >= 10 and num <= 20:
        nums.append(num)
    else:
        print("Outside the range")
for i in nums:
    print(i)

# 091
# Create an array which contains five numbers(two of which should be
# repeated). Display the whole array to the user. Ask the user to enter
# one of the numbers from the array and then display a message saying how
# many times that number appears in the list.

from array import *

nums = array('i', [5, 7, 9, 2, 9])
for i in nums:
    print(i)
num = int(input("Enter a number: "))
if nums.count(num) == 1:
    print(num, "is in the list once")
else:
    print(num, "is in the list", nums.count(num), "times")

# 092
# Create two arrays(one containing three numbers that the user enters and
# one containing a set of five random numbers). Join these two arrays
# together into one large array. Sort this large array and display it so
# that each number appears on a separate line.

from array import *
import random

num1 = array('i', [])
num2 = array('i', [])

for i in range(0, 3):
    num = int(input("Enter a number: "))
    num1.append(num)

for i in range(0, 5):
    num = random.randint(1, 100)
    num2.append(num)

num1.extend(num2)
num1 = sorted(num1)

for i in num1:
    print(i)

# 093
# Ask the user to enter five numbers. Sort them into order and present them
# to the user. Ask them to select one of the numbers. Remove it from the
# original array and save it in a new array.

from array import *

nums = array('i', [])

for i in range(0, 5):
    num = int(input("Enter a number: "))
    nums.append(num)

nums = sorted(nums)

for i in nums:
    print(i)

num = int(input("Select a number from the array: "))
if num in nums:
    nums.remove(num)
    num2 = array('i', [])
    num2.append(num)
    print(nums)
    print(num2)
else:
    print("That is not a value in the array")

# 094
# Display an array of five numbers. Ask the user to select one of the 
# numbers. Once they have selected a number, display the position of that
# item in the array. If they enter something that is not in the array, ask
# them to try again until they select a relevant item.

from array import *

nums = array('i', [4, 6, 8, 2, 5])

for i in nums:
    print(i)

num = int(input("Select one of the numbers: "))

tryagain = True
while tryagain == True:
    if num in nums:
        print("This is in position", nums.index(num))
        tryagain = False
    else:
        print("Not in array")
        num = int(input("Select one of the numbers: "))

# 095
# Create an array of five numbers between 10 and 100 which each have two 
# decimal places. Ask the user to enter a whole number between 2 and 5.
# If they enter something outside of that range, display a suitable error
# message and ask them to try again until they enter a valid amount. Divide
# each of the numbers in the array by the number the user entered and display
# the answers shown to two decimal places.

from array import *
import math

nums = array('f', [34.75, 27.23, 99.58, 45.26, 28.65])
tryagain = True
while tryagain == True:
    num = int(input("Enter a number between 2 and 5: "))
    if num < 2 or num > 5:
        print("Incorrect value, try again.")
    else:
        tryagain = False
for i in range(0, 5):
    ans = nums[i]/num
    print(round(ans, 2))

# 096
# Create the following using a simple 2D list using the standard Python
# indexig

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

# 097
# Using the 2D list from program 096, ask the user to select a row and a 
# column and display that value.

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Select a row: "))
col = int(input("Select a column: "))
print(list[row][col])

# 098
# Using the 2D list from program 096, ask the user which row they would like
# displayed and display just that row. Ask them to enter a new value and add
# it to the end of the row and display the row again.

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Select a row: "))
print(list[row])
newvalue = int(input("Enter a new number: "))
list[row].append(newvalue)
print(list[row])

# 099
# Change your previous program to ask the user which row they want 
# displayed. Display that row. Ask which column in that row they want
# displayed and display the value that is held there. Ask the user if they
# want to change the value. If they do, ask for a new value and change the
# data. Finally, display the whole row again.

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Select a row: "))
print(list[row])
col = int(input("Select a column: "))
print(list[row][col])
change = input("Do you want to change the value? (y/n) ")
if change == "y":
    newvalue = int(input("Enter new value: "))
    list[row][col] = newvalue
print(list[row])

# 100
# Create the folloeing using a 2D dictionary showing th sales each person
# has made in the different geographical regions:

sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
        "Tom": {"N": 4832, "S": 6786, "E": 4737, "W":3612},
        "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
        "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}

# 101
# Using programm 100, ask the user for a name and a region. Display the 
# relevant data. Ask the user for the name and region of data they want to
# change and allow them to make the alteration to the sales figure. Display
# the sales for all regions for the name they choose.

sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
        "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
        "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
        "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
person = input("Enter sales person's name: ")
region = input("Select region: ")
print(sales[person][region])
newdata = int(input("Enter new data: "))
sales[person][region] = newdata
print(sales[person])

# 102
# Ask the user to enter the name, age and shoe size for four people. Ask for
# the name of one of the people in the list and display their age and shoe
# size.

list = {}
for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age": age, "Shoe size": shoe}

ask = input("Enter a name how you interested info: ")
print(list[ask])

# 103
# Adapt program 102 to display the names and ages of all the list but do not
# show their shoe size.

list = {}
for in in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age": age, "Shoe size": shoe}

for name in list:
    print((name), list[name]["Age"])

# 104
# After gathering the four names, ages and shoe sizes, ask the user to enter
# the name of the person they want to remove from the list. Delete this row
# from the data and display the other rows on separate lines.

list = {}
for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age": age, "Shoe size": shoe}

getrid = input("Who do you want to remove from the list? ")
del list[getrid]

for name in list:
    print((name), list[name]["Age"], list[name]["Shoe size"])


# 105
# Write a new file called "Numbers.txt". Add five numbers to the document
# which are stored on th same line and only separated by a comma. Once you
# have run the program, look in the location where your program is stored
# and you should see that the file has been created.

file = open("Numbers.txt", "w")
file.write("4, ")
file.write("6, ")
file.write("10, ")
file.write("8, ")
file.write("5, ")
file.close()

# 106
# Create a new file called "Names.txt". Add five names to the document,which
# are stored on separate lines. Once you have run the program, look in the 
# location where your program is stored and check that the file has been
# created properly.

file = open("Names.txt", "w")
file.write("Bob\n")
file.write("Tom\n")
file.write("Gemma\n")
file.write("Sarah\n")
file.write("Timothy\n")
file.close()


# 107
# Open the Names.txt file and display the data in Python

file = open("Names.txt", "r")
print(file.read())
file.close()


# 108
# Open the Names.txt file. Ask the user to input a new name. Add this to the
# end of the file and display the entire file.

file = open("Names.txt", "a")
newname = input("Enter a new name: ")
file.write(newname + "\n")
file.close

file = open("Names.txt", "r")
print(file.read())
file.close



# 109
# Display the following menu to the user:
# 1) Create a new file
# 2) Display the file
# 3) Add a new item to the file
# Make a selection 1, 2 or 3:
# Ask the user to enter 1, 2 and 3. If they select anything other than 1, 2
# or 3 it should display a suitable error message.
# If they select 1, ask the user to enter a school subject and save it to a
# new file called "Subject.txt". It should overwrite any existing file with
# a new file.
# If they select 2, display the contents of the "Subject.txt" file.
# If they selct 3, ask the user to enter a new subject and save it to the 
# file and then display the entire contents of the file.
# Run the program several times to test the options.

print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
selection = int(input("Make a selection 1, 2 or 3: "))
if selection == 1:
    subject = input("Enter a school subject: ")
    file = open("Subject.txt", "w")
    file.write(subject + "\n")
    file.close()
elif selection == 2:
    file = open("Subject.txt", "r")
    print(file.read())
elif selection == 3:
    file = open("Subject.txt", "a")
    subject = input("Enter a school subject: ")
    file.write(subject + "\n")
    file.close()
    file = open("Subject.txt", "r")
else:
    print("Invalid option")


# 110
# Using the Names.txt file you created earlier, display the list of names in
# Python. Ask the user to type in one of the names and then save all the
# names except the one they entered into a new file called Names2.txt

file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt", "r")
selectedname = input("Enter a name from the list: ")
selectedname = selectedname + "\n"
for row in file:
    if row in file:
        if row != slectedname:
            file = open("Names2.txt", "a")
            newrecord = row
            file.write(newrecord)
            file.close()
file.close()

# csv examples
import csv

file = open("Stars.csv", "w")
newRecord = "Brian, 73, Taurus\n"
file.write(str(newRecord))
file.close()

file = open("Stars.csv", "a")
name = input("Enter name: ")
age = input("Enter age: ")
star = input("Enter star sign: ")
newRecord = name + "," + age + "," + star + "\n"
file.write(str(newRecord))
file.close()

file = open("Stars.csv", "r")
for row in file:
    print(row)

file = open("Stars.csv", "r")
reader = csv.reader(file)
rows = list(reader)
print(rows[1])

file = open("Stars.csv", "r")
search = input("Enter the data you are searching for: ")
reader = csv.reader(file)
for row in file:
    if search in str(row):
        print(row)


###########
# A .csv file cannot be altered, only added to. If you need to alter the file
# you need to write it to a temporary list. This block of code will read the
# original .csv file and write it to a list called "tmp".
import csv
file = list(csv.reader(open("Stars.csv")))
tmp = []
for row in file:
    tmp.append(row)
# Writes from a list into a new .csv file called "NewStars.csv".
file = open("NewStars.csv", "w")
x = 0
for row in tmp:
    newRec = tmp[x][0] + "," + tmp[x][1] + "," + tmp[x][2] + "\n"
    file.write(newRec)
    x = x + 1
file.close()

# 111
# Create a .csv file that will store the following data. Call it "Books.csv".
import csv
file = open("Books.csv", "w")
newrecord = "To Kill A Mockingbird, Harper Lee, 1960\n"
file.write(str(newrecord))
newrecord = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(newrecord))
newrecord = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(newrecord))
newrecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(newrecord))
newrecord = "Pride and Prejudice, Jane Austin, 1813\n"
file.write(str(newrecord))
file.close()

# 112
# Using the Books.csv file from program 111, ask the user to enter another
# record and add it to the end of the file. Display each row of the .csv file
# on a separate line

import csv

file = open("Books.csv", "a")
title = input("Enter a title: ")
author = input("Enter author: ")
year = input("Enter the year it was released: ")
newrecord = title + "," + author + ", " + year + "\n"
file.write(str(newrecord))
file.close()

file = open("Books.csv", "r")
for row in file:
    print(row)
file.close()


# 113
# Using the Books.csv file, ask the user how many records they want to add to
# the list and then allow them to add that many. After all the data has been
# added, ask for an author and display all the books in the list by that
# author. If there are no books by that author in the list, display a
# suitable message.

import csv
num = int(input("How many books do you want to add to the list? "))
file = open("Books.csv", "a")
for x in range(0, num):
    title = input("Enter a title: ")
    author = input("Enter author: ")
    year = input("Enter the year it was released: ")
    newrecord = title + "," + author + ", " + year + "\n"
    file.write(str(newrecord))
file.close()

searchauthor = input("Enter an authors name to search for: ")
file = open("Books.csv", "r")
count = 0
for row in file:
    if searchauthor in str(row):
        print(row)
        count = count + 1
if count == 0:
    print("There are no books by that author in this list.")
file.close()

# 114
# Using the Books.csv file, ask the user to enter a starting year and an
# end year. Display all books released between those two years.

import csv

start = int(input("Enter a starting year: "))
end = int(input("Enter an end year: "))

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <= end:
        print(tmp[x])
    x = x + 1

# 115
# Using th Books.csv file, display  the data in the file along with the row
# number of each

import csv

start = int(input("Enter a starting year: "))
end = int(input("Enter an end year: "))

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <=end:
        print(tmp[x])
    x = x+1
"""
# 116

