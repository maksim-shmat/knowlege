"""Strings about."""

#1 concatenate strings without addition

a = ["Python", "-", 'beautiful', 'language.']
print(" ".join(a))
print()

######2 convert list of numbers to string with .join

numbers = [1, 2, 3, 4, 5]
print(', '.join(map(str, numbers)))
print()

######3  escape sharacters

escape_str = "She said: \"Python is great!\""
print(escape_str)
print()

######4 concatenate strings

one = "Lux"
two = "Academy"
print(one + " " + two)
print()

######5 interpolation
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

######6 extract substring

name = "Monty Python"
print(name[6:9])
print(name[6:])
print(name[:5])
print()

######7 check if string is empty

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

######8
"""str() about."""

# str() with list object as argument

myList = [25, 'hello world', 36.25]
resultString = str(myList)
print(f'Resulting string is - "{resultString}"')
print()

######9 str() with no object as argument

resultString = str()
print(f'Resulting string is - "{resultString}"')
print()

######10 str() with encoding

bytes = b'\x65\x66\x67\x68\x69'
resultString = str(bytes, encoding='utf-8')
print(f'Resulting string is - "{resultString}"')
print()

######11 find string length

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

######12 slicing, find substring

mystring = 'pythonexamples.org'
substring = mystring[6:12]
print(substring)
print()

######13 find substring with end position greater than string length

mystring = 'pythonexamples.org'
substring = mystring[6:35]
print(substring)
print()

######14 substring - negative position

mystring = 'pythonexample.org'
substring = mystring[-15:-5]
print(substring)
print()

######15 substring - no start or end provided

mystring = 'pythonexamples.org'
substring = mystring[:]
print(substring)
print()

######16 reverse string using slicing

str = "Welcome to Python Examples."
reversed = str[::-1]
print(reversed)
print()

#####17 reverse string using for loop

str = "Welcome to Python Examples."
reversed = ''
for c in str:
    reversed = c + reversed
print(reversed)
print()

######18 reverse string using while loop

str = "What in the heaven's name are you talking about?"
reversed = ''
length = len(str) - 1
while length >= 0:
    reversed = reversed + str[length]
    length = length - 1
print(reversed)
print()

######19 reverse string using List.reverse()

str = "What is going know?"
str_list = list(str)
str_list.reverse()
reversed = ''.join(str_list)
print(reversed)
print()

######20 slice string with specific end position

string1 = 'hello-world'
stop = 5
slice_object = slice(stop)
result = string1[slice_object]
print(result)
print()

######21 slice string with specific start and end position

string1 = 'hello-world'
start = 2
stop = 5
slice_object = slice(start, stop)
result = string1[slice_object]
print(result)
print()

######22 slice string with specific start and end position, step

string1 = 'hello-world'
start = 2
stop = 9
step = 2
slice_object = slice(start, stop, step)
result = string1[slice_object]
print(result)
print()

######23 iterate over words of string

str = 'Hello! I am Robot. This is a Python example.'
# split string
splits = str.split()

# for loop to iterate over words array
for split in splits:
    print(split)
print()

######24 clean string & iterate over words of string

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

######25 find index of first occurence of substring

string = 'Python programming. Network programming.'
substring = 'prog'
index = string.find(substring)
print(index)
print()

######26 find index of first occurence of substring after a specific position

string = 'Python programming. Network programming.'
substring = 'prog'
start = 12
index = string.find(substring, start)
print(index)
print()

######27 number of overlapping occurrences of substring

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

######28 change strings

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

low = 'ALICE!!! Alice come here'
print(low)
print()

up = 'Hurraaay!'.upper()
print(up)
print()

######29
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

######30 trim white spaces around string

mystring = '    python examples        '
cleanstring = mystring.strip()

# before strip
print(mystring)
print(len(mystring))

# after string
print(cleanstring)
print(len(cleanstring))
print()

######31 trin white spaces like \n \t around string

mystring = ' \n\t  python examples \n\n'
cleanstring = mystring.strip()

# before strip
print(mystring)
print(len(mystring))

# after string
print(cleanstring)
print(len(cleanstring))
print()

######32 traverse strings in list of strings

list_of_strings = ['apple', 'banana', 'mango']
for string in list_of_strings:
    print(string)
print()

### with while

list_of_strings = ['apple', 'banana', 'mango']
i = 0
while i < len(list_of_strings):
    print(list_of_strings[i])
    i += 1
print()

######33 modify strings in list of strings

list_of_strings = ['apple', 'banana', 'mango']
list_of_strings[1] = "orange"
print(list_of_strings)
print()

######34 access strings in list of strings

list_of_strings = ['apple', 'banana', 'mango']
print(list_of_strings[0])
print(list_of_strings[1])
print()

######35 check if string contains only Alphabets

str1 = "hello world, welcome to python example."
bool = str1.isalpha()
print('str1 contains only alphabets:', bool)
print()

### check more

str1 = "HELLOWORLDPYTHONEXAMPLE"
bool = str1.isalpha()
print('str1 contains only alphabets:', bool)
print()

######36 string with only alphanumeric characters

str = 'pythonexamples125'
isalnum = str.isalnum()
print('Is String Alphanumeric :', isalnum)
print()

### alphanumeric and spaces is false
### alphanumeric and special characters is false

######37 check if string contains substring

string = 'Hello World!'
substring = 'Wor'
isSubstringPresent = substring in string
print(isSubstringPresent)
print()

### with if/else

string = 'Hello World!'
substring = 'Wor'
if substring in string:
    print('String contains substring.')
else:
    print('String does not contain substring.')

### with string.find()

string = 'Hello World!'
substring = 'Wor'
if string.find(substring) > -1:
    print('String contains substring.')
else:
    print('String does not contains substring.')
print()

######38 replace a string

mystring = 'Python Examples. Examples for basic and advanced concepts.'
print('Original String : ', mystring)

newstr = mystring.replace('Examples', 'Programs')
print('New String :', newstr)

### replace string only a specific number of times

mystring = 'Python Examples. Examples.Examples. Examples. Examples. Examples.'
print('Original String :', mystring)

newstr = mystring.replace('Examples', 'Programs', 3)
print('New String :', newstr)
print()

######39 replace continuous multiple white spaces with single space

mystring = 'welcome     to  python         examples'
correctedstring = " ".join(mystring.split())
print(correctedstring)
print()

### replace continuous multiple white spaces, containing \n, \t, etc

mystring = 'welcome \t\t    to  pythob   \n\n        examples'
correctedstring = " ".join(mystring.split())
print(correctedstring)
print()

######40 replace character at a given position in a string using string slicing
string = 'pythonhxamples'
position = 6
new_character = 'e'

string = string[:position] + new_character + string[position+1:]
print(string)

### replace character at a given position in a string using list

string = 'pythonhxamples'
position = 6
new_character = 'e'

temp = list(string)
temp[position] = new_character
string = "".join(temp)

print(string)
print()

######41 split string into chunks

str = 'CarBadBoxNumKeyValRayCppSan'
n = 3
chunks = [str[i:i+n] for i in range(0, len(str), n)]
print(chunks)

### split string by length

str = 'Welcome to Python Examples'
n = 4
chunks = [str[i:i+n] for i in range(0, len(str), n)]
print(chunks)

### split string into chunks using while loop

str = 'Welcome to Python Examples'
n = 5
chunks = []
i = 0
while i < len(str):
    if i+n < len(str):
        chunks.append(str[i:i+n])
    else:
        chunks.append(str[i:len(str)])
    i += n
print(chunks)
print()

######42 split string by underscore

str = '52_841_63_24_76_49'
items = str.split('_')
print(items)

### split string by one or more underscore

import re
str = '52_841__63____24_76______49'
items = re.split('_+', str)
print(items)
print()

######43 split string by space

str = '63 41 92 81 69 70'
chuncks = str.split(' ')
print(chunks)

### split string by one or more adjacent spaces
import re

str = '63 41    92  81          69  70'
chunks = re.split(' +', str)
print(chunks)

### split string by any white space character
# ascii hex code: 09 - horizontal tab
#                 0A - new line feed
#                 0B - vertical tab
#                 0D - carrage return/form feed
#                 20 - space
import re

str = '63 41\t92\n81\r69 70'
chunks = str.split()
print(chunks)
print()

######44
