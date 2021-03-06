""" Real big cases.

A shift code is where message can be easily encoded and is one of the simplest
codes to use. Each letter is moved forwards through the alphabet a set number
of letters to be represented by a new letter. For instance, "abc" becomes
"bcd" when the code is shifted by one(i.e. each letter in the alphabet is
moved forward one character).

You need to create a program which will display the following menu:

    1) Make a code
    2) Decode a message
    3) Quit

    Enter your selection:

If the user select 1, they should be able to type in a message(including 
spaces) and then enter a number. Python should then display the encoded
message once the shift code has been applied.

If the user select 2, they should enter an encoded message and the correct
number and it should display the decoded message(i.e. move the correct number
of letters backwards through the alphabet).

If they select 3 it should stop the program from running.

After they have encoded or decoded a message the menu should be displayed to
them again until they selct quit.

Problems You Will Have to Overcome.

Decode if you want to allow both upper and lower case letters or if you want
to convert all the data into one case.

Decode if you are allowing punctuation.

If the shift makes the letter go past the end of the alphabet it should start
again; i.e. if the eser enters "xyz" and 5 is entered as the chit number, it
should display "bcd". This should work the opposite way for decoding a
message, so if the value gets to "a" it will go back to "w".

Make sure that suitable messages are displayed if the user selects an 
inappropriate option on the menu or seldts an inappropriate number to make
the shift code.

Test out you decode option by decoding the message "weovugjohsslunl", which
was created with the number 7 when the code only uses "abcdefghijklmnopqrstuvwxyz "(note the space at the end).
"""
'''
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z", " "]

def get_data():
    word = input("Enter your message: ")
    word = word.lower()
    num = int(input("Enter a number (1-26): "))
    if num > 26 or num == 0:
        while num > 26 or num == 0:
            num = int(input("Out of range, please enter a number (1-26): "))
    data = (word, num)
    return(data)

def make_code(word, num):
    new_word = ""
    for x in word:
        y = alphabet.index(x)
        y = y + num
        if y > 26:
            y = y - 27
        char = alphabet[y]
        new_word = new_word + char
    print(new_word)
    print()

def decode(word, num):
    new_word = ""
    for x in word:
        y = alphabet.index(x)
        y = y - num
        if y < 0:
            y = y + 27
        char = alphabet[y]
        new_word = new_word+char
    print(new_word)
    print()

def main():
    again = True
    while again == True:
        print("1) Make a code")
        print("2) Decode a message")
        print("3) Quit")
        print()
        selection = int(input("Enter your selection: "))
        if selection == 1:
            (word, num) = get_data()
            make_code(word, num)
        elif selection == 2:
            (word, num) = get_data()
            decode(word, num)
        elif selection == 3:
            again = False
        else:
            print("Incorrect selection")

main()

# 147
""" You are going to make an on-screen version of the board game "Mastermind".
The computer will automatically generate four colours from a list of possible
colours (it should be possible for the commputer to randomly select the same
colour more than once). For instance, the computer may choose "red", "blue",
"red", "green". This sequence should not be displayed to the user.

After this is done the user should enter their choice of four colours from
the same list the computer used. For instance, they may choose "pink", "blue",
"yellow", and "red".

After the user has made their selection, the program should display how many
colours they got right in the correct position and how many colours they got
right but in the wrong position. In the example above, it should display the
message "Correct colour in the correct place: 1" and "Correct colour but in
the wrong place: 1".

The user continues guessing until they correctly enter the four colours in the
order they should be in. At the end of the game it should display a suitable
message and tell them how many guesses they took.

Problems you will have to overcome:

The hardest part of this game is working out the logic for checking how many
the user has correct and how many are in the wrong place. Using the example
above, if the user enters "blue", "blue", "blue", "blue" they should see the
messages, "Correct colour in the correct place: 1" and "Correct colour but in
the wrong place: 0".

Decide if there is an easier way of allowing the user to enter their selection
(e.g. using a code of a single letter to represent the colour). If using the
first, make sure you only use colours that have a unique first letter(i.e.
avoid using blue, black and brown as options and select just one of these as
a possibility). Make your instructions clear to the user.

Decide if you want to allow upper and lower case or if it is easier to convert
everything to the same case.

Make sure you build in validation checks to make sure the user is only
entering valid data and display a suitable message if they make an incorrect
selection. If they do make an incorrect selection you may want to allow them
to enter the data again, rather than class it as an incorrect guess.
"""
import random

def select_col():
    colours = ["r", "b", "o", "y", "p", "g", "w"]
    c1 = random.choice(colours)
    c2 = random.choice(colours)
    c3 = random.choice(colours)
    c4 = random.choice(colours)
    data = (c1, c2, c3, c4)
    return data

def tryit(c1, c2, c3, c4):
    print("The colours are: (r)ed, (b)lue, (o)range, (y)ellow, (p)ink, (g)reen and (w)hite.")
    try_again = True
    while try_again == True:
        u1 = input("Enter your choice for place 1: ")
        u1 = u1.lower()
        if u1 != "r" and u1 != "b" and u1 != "o" and u1 != "y" and u1 != "p" and u1 != "g" and u1 != "w":
            print("Incorrect selection")
        else:
            try_again = False
    try_again = True
    while try_again == True:
        u2 = input("Enter your choice for place 2: ")
        u2 = u2.lower()
        if u2 != "r" and u2 != "b" and u2 != "o" and u2 != "y" and u2 != "p" and u2 != "g" and u2 != "w":
            print("Incorrect selection")
        else:
            try_again = False
    try_again = True
    while try_again == True:
        u3 = input("Enter your choice for place 3: ")
        u3 = u3.lower()
        if u3 != "r" and u3 != "b" and u3 != "o" and u3 != "y" and u3 != "p" and u2 != "g" and u3 != "w":
            print("Incorrect selection")
        else:
            try_again = False
    try_again = True
    while try_again == True:
        u4 = input("Enter your choice for place 4: ")
        u4 = u4.lower()
        if u4 != "r" and u4 != "b" and u4 != "o" and u4 != "y" and u4 != "p" and u2 != "g" and u3 != "w":
            print("Incorrect selection")
        else:
            try_again = False
    correct = 0
    wrong_place = 0
    if c1 == u1:
        correct = correct + 1
    elif c1 == u2 or c1 == u3 or c1 == u4:
        wrong_place = wrong_place + 1
    if c2 == u2:
        correct = correct + 1
    elif c2 == u1 or c2 == u3 or c2 == u4:
        wrong_place = wrong_place + 1
    if u3 == c3:
        correct = correct + 1
    elif c3 == u1 or c3 == u2 or c3 == u4:
        wrong_place = wrong_place + 1
    if u4 == c4:
        correct = correct + 1
    elif c4 == u1 or c4 == u2 or c4 == u3:
        wrong_place = wrong_place + 1
    print("Correct colour in the correct place: ", correct)
    print("Correct colour but in the wrong place: ", wrong_place)
    print()
    data2 = [correct, wrong_place]
    return data2

def main():
    (c1, c2, c3, c4) = select_col()
    score = 0
    play = True
    while play == True:
        (correct, wrong_place) = tryit(c1, c2, c3, c4)
        score = score + 1
        if correct == 4:
            play = False
    print("You win!")
    print("You took", score, "guesses")

main()
'''
# 148
""" Passwords.
You need to create a program that will store the user ID and passwords for 
the users of a system. It should display the following menu:
    1) Create a new User ID
    2) Change a password
    3) Display all User IDs
    4) Quit
    Enter Selection:

If the user selcts 1, it should ask them to enter a user ID. It should check
if the user ID is already in the list. If it is, the program should display a
suitable message and ask them to selct another user ID. Once a suitable user
ID has been entered it should ask for a password. Passwords should be scored
with 1 point for each of the following:
    - it should have at least 8 characters;
    - it should include uppercase letters;
    - it should include lower case letters;
    - it should include numbers; and
    - it should include at least one special character such as!, $, % , &,
    <, * or @.

If the password scores only 1 or 2 it should be rejected with a message saying
it is a weak password; if it scores 3 or 4 tell them that "This password could
be improved." Ask them if they want to try again. If it scores 5 tell them
they have selected a strong password. Only acceptable user IDs and passwords
should be added to the end of the .csv file.

if they select 2 from the menu they will need to enter a user ID, check to see
if the user ID exists in the list, and if it does, allow the user to change
the password and save the changes to the .csv file. Make sure the program only
alters the existing password and does not create a new record.

If the user selects 3 from the menu, display all the user IDs but not the
passwords.

If the user selects 4 from the menu it should stop the program.

=== Problems You Will Have to Overcome. ===

As existing data in .csv files cannot be edited and can only be read or added
to, you will need to import the data as a temporary list into Python so you
can make the change before the data is written to the .csv file afresh.

Make sure only passwords belonging to an existing user ID can be altered.

Use suitable messages to guide the user easily throught the system.

Repeat the menu until they quit the program.
"""
# First set up a .csv file, called "passwords.csv"
import csv

def get_data():
    file = list (csv.reader(open("passwords.csv")))
    tmp = []
    for x in file:
        tmp.append(x)
    return tmp

def create_userID(tmp):
    name_again = True
    while name_again == True:
        userID = input("Enter a new user ID: ")
        userID.lower()
        inlist = False
        row = 0
        for y in tmp:
            if userID in tmp[row][0]:
                print(userID, "has already been allocated")
                inlist = True
            row = row + 1
        if inlist == False:
            name_again = False
    return userID

def create_password():
    sclist = ["!", "$", "%", "^", "&", "*", "(", ")", "?", "@", "#"]
    nclist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    tryagain = True
    while tryagain == True:
        score = 0
        uc = False
        lc = False
        sc = False
        nc = False
        password = input("Enter Password: ")
        length = len(password)
        if length >= 8:
            score = score + 1
        for x in password:
            if x.islower():
                lc = True
            if x.isupper():
                uc = True
            if x in sclist:
                sc = True
            if x in nclist:
                nc = True
        if sc == True:
            score = score + 1
        if lc == True:
            score = score + 1
        if uc == True:
            score = score + 1
        if nc == True:
            score = score + 1
        if score == 1 or score == 2:
            print("This is a weeek password, try again")
        if score == 3 or score == 4:
            print("This password could be importved")
            again = input("Do you want to try for a stronger password? (y/n) ")
            again.lower()
            if again == "n":
                tryagain = False
       # if password != password2:    # what is the password2?
        #    print("Passwords do not match. File not saved")
         #   main()
        else:
            return password

def find_userID(tmp):
    ask_name_again = True
    userID = ""
    while ask_name_again == True:
        searchID = input("Enter the user ID you are looking for ")
        searchID.lower()
        inlist = False
        row = 0
        for y in tmp:
            if searchID in tmp[row][0]:
                inlist = True
            row = row + 1
        if inlist == True:
            userID = searchID
            ask_name_again = False
        else:
            print(searchID, "is NOT in the list")
    return userID

def change_password(userID, tmp):
    if userID != "":
        password = create_password()
        ID = userID.index(userID)
        tmp[ID][1] = password
        file = open("passwords.csv", "w")
        x = 0
        for row in tmp:
            newrecord = tmp[x][0] + ", " + tmp[x][1] + "\n"
            file.write(newrecord)
            x = x + 1
        file.close()

def display_all_userID():
    tmp = get_data()
    x = 0
    for row in tmp:
        print(tmp[x][0])
        x = x + 1

def main():
    tmp = get_data()
    go_again = True
    while go_again == True:
        print()
        print("1) Create a new User ID")
        print("2) Change a password")
        print("3) Display all User IDs")
        print("4) Quit")
        print()
        selection = int(input("Enter Selection: "))
        if selection == 1:
            userID = create_userID(tmp)
            password = create_password()
            file = open("passwords.csv", "a")
            newrecord = userID + ", " + password + "\n"
            file.write(str(newrecord))
            file.close()
        elif selection == 2:
            userID = find_userID(tmp)
            change_password(userID, tmp)
        elif selection == 3:
            display_all_userID()
        elif selection == 4:
            go_again = False
        else:
            print("Incorrect selection")

main()


