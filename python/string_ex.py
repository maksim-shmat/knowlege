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

######
