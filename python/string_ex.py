"""Strings about."""

# concatenate strings without addition

a = ["Python", "-", 'beautiful', 'language.']
print(" ".join(a))
print()

###### convert list of numbers to string with .join

numbers = [1, 2, 3, 4, 5]
print(', '.join(map(str, numbers)))
print()

######  escape sharacters

escape_str = "She said: \"Python is great!\""
print(escape_str)
print()

###### concatenate strings

one = "Lux"
two = "Academy"
print(one + " " + two)
print()

###### interpolation
# method 1

first_name = "Lux"
last_name = "Academy"
greet = f"Welcome at {first_name} {last_name}!"
print(greet)
print()

# method 2

first_name = "Lux"
last_name = "Academy"
greet = 'Welcome at {} {}!'.format(first_name, last_name)
print(greet)
print()

# method 3

first_name = "Lux"
last_name = "Academy"
greet = 'Welcome at{first} {last} !'.format(first=first_name, last=last_name)
print(greet)
print()

###### extract substring

name = "Monty Python"
print(name[6:9])
print(name[6:])
print(name[:5])
print()

###### check if string is empty

mystring = ""
if not mystring:
    print("The string is empty.")
else:
    print("The string is not empty.")

### check if string is empty with ==

mystring == ""
if mystring == "":
    print("The string is empty.")
else:
    print("The string is not empty.")
print()

######
"""str() about."""

# str() with list object as argument

myList = [25, 'hello world', 36.25]
resultString = str(myList)
print(f'Resulting string is - "{resultString}"')
print()

###### str() with no object as argument

resultString = str()
print(f'Resulting string is - "{resultString}"')
print()

###### str() with encoding

bytes = b'\x65\x66\x67\x68\x69'
resultString = str(bytes, encoding='utf-8')
print(f'Resulting string is - "{resultString}"')
print()

###### find string length

mystring = 'python examples'
# length of string
length = len(mystring)

print('Length of the string is:', length)
print()

### find empty string length

mystring = ''
length = len(mystring)
print('length of the is: ', length)
print()

###### slicing, find substring

mystring = 'pythonexamples.org'
substring = mystring[6:12]
print(substring)
print()

###### find substring with end position greater than string length

mystring = 'pythonexamples.org'
substring = mystring[6:35]
print(substring)
print()

###### substring - negative position

mystring = 'pythonexample.org'
substring = mystring[-15:-5]
print(substring)
print()

###### substring - no start or end provided

mystring = 'pythonexamples.org'
substring = mystring[:]
print(substring)
print()

###### reverse string using slicing

str = "Welcome to Python Examples."
reversed = str[::-1]
print(reversed)
print()

##### reverse string using for loop

str = "Welcome to Python Examples."
reversed = ''
for c in str:
    reversed = c + reversed
print(reversed)
print()

###### reverse string using while loop

str = "What in the heaven's name are you talking about?"
reversed = ''
length = len(str) - 1
while length >= 0:
    reversed = reversed + str[length]
    length = length - 1
print(reversed)
print()

###### reverse string using List.reverse()

str = "What is going know?"
str_list = list(str)
str_list.reverse()
reversed = ''.join(str_list)
print(reversed)
print()

###### slice string with specific end position

string1 = 'hello-world'
stop = 5
slice_object = slice(stop)
result = string1[slice_object]
print(result)
print()

###### slice string with specific start and end position

string1 = 'hello-world'
start = 2
stop = 5
slice_object = slice(start, stop)
result = string1[slice_object]
print(result)
print()

###### slice string with specific start and end position, step

string1 = 'hello-world'
start = 2
stop = 9
step = 2
slice_object = slice(start, stop, step)
result = string1[slice_object]
print(result)
print()

###### iterate over words of string

str = 'Hello! I am Robot. This is a Python example.'
# split string
splits = str.split()

# for loop to iterate over words array
for split in splits:
    print(split)
print()

###### clean string & iterate over words of string

import re
str = "What in the heavens's name are you talking about?"

# clean string
pat = re.compile(r'[^a-zA-Z ]+')  # not check apostrofie
str = re.sub(pat, '', str).lower()

# split strng
splits = str.split()

# for loop to iterate over words array
for split in splits:
    print(split)
print()

###### find index of first occurence of substring

string = 'Python programming. Network programming.'
substring = 'prog'
index = string.find(substring)
print(index)
print()

###### find index of first occurence of substring after a specific position

string = 'Python programming. Network programming.'
substring = 'prog'
start = 12
index = string.find(substring, start)
print(index)
print()

###### number of overlapping occurrences of substring

string = 'abcdefghghghghghg.'
substring = 'ghg'

count = 0
start = 0
if (len(string)>0 and len(string) < 201):
    for i in range(len(string)):
        i = string.find(substring, start)
        if (i>0):
            start = i+1
            count += 1
        else:
            break
print(count)
print()

###### change strings

cap = 'need capital later in head'.capitalize()
print(cap)
print()

spac = '    spaces!!!    '.strip()
print(spac)
print()

cent = 'centerus for tg bot exmpl'.center(70)
print(cent)
print()

one_to_two = 'PyThOn'.swapcase()
print(one_to_two)
print()

low = 'ALICE!!! Alice come here'.lower()
print(low)
print()

up = 'Hurraaay!'.upper()
print(up)
print()

######
"""Find understring."""

programmers = ["I'm an expert Python Programmer",
               "I'm an expert Javascript Programmer",
               "I'm a professional Python Programmer",
               "I'm a beginner C++ Programmer"
]

# method 1
for p in programmers:
    if p.find("expert"):
        print("wrong example")


# method 2
for p in programmers:
    if "Python" in p:
        print(p)

###### trim white spaces around string

mystring = '    python examples        '
cleanstring = mystring.strip()

# before strip
print(mystring)
print(len(mystring))

# after string
print(cleanstring)
print(len(cleanstring))
print()

###### trin white spaces like \n \t around string

mystring = ' \n\t  python examples \n\n'
cleanstring = mystring.strip()

# before strip
print(mystring)
print(len(mystring))

# after string
print(cleanstring)
print(len(cleanstring))
print()

######
