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
"""
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

