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
