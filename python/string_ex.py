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
print(name[:5]
print()

######
