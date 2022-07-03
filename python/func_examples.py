"""A Functions about."""

#1 Defining the function

def func_hello(username):  # 'username' is parameter
    """Return simple hello."""
    print(f"Hello, {username.title()}!")

# Calling the function
func_hello('jessie')  # 'jessie' is argument

results:
    Hello, Jessie!

#2 Parameters and args

def printMax(a, b):  # a, b is parameters
    if a > b:
        print(a, 'max')
    elif a == b:
        print(a, 'equals', b)
    else:
        print(b, 'max')

printMax(3, 4)  # bring values

x = 5
y = 7

printMax(x, y)  # variables as arguments

results:
    4 max
    7 max

--------------
def describe_pet(animal_type, pet_name):
    """Return info about animal."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

or with named arguments

describe_pet(animal_type='hamster', pet_name='harry')

results:
    I have a hamster.
    My hamster`s name is Harry.


#3 Defining the function for sum of two variables

def sum(num1,num2):
    return num1 + num2

#4 Taking values from the user as an input

num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))

#5 Calculating and Printing the sum of num1 and num2

print("Sum = ",sum(num1,num2))

#6 maximum from the given three numbers

def max_of_two(x, y):
    if x > y:
        return x
    return y

def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))

print(max_of_three(3, 6, -5))

#7 calculate the sum of all the numbers present in a list

def sum(numbers):
    total = 0
    for element in numbers:
        total += element
    return total
print(sum((8, 2, 8, 0, 7)))

#8 calculate the multiplication of all the numbers present in a list

def multiply(numbers):
    total = 1
    for element in numbers:
        total *= element
    return total

print(multiply((3, 8, 2, -1, 7)))

#9 takes a string as an input and calculates the number of upper case
#      and lower case letters present in the string

def string_test(string):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for character in string:
        if character.isupper():
            d["UPPER_CASE"]+=1
        elif character.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("Original String: ", string)
    print("No. of Upper case characters: ", d["UPPER_CASE"])
    print("No. of Lower case characters: ", d["LOWER_CASE"])

string_test('The quick Brown Fox')

#10 program that takes a number(non-negative integer) as an argument
#      and calculates its factorial.

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

number = int(input("Input a number to compute the factorial : "))
print(factorial(number))

#11 
"""Athributes of function in python."""

def func(x):
    intermediate_var = x**2 + x + 1

    if intermediate_var % 2:
        y = intermediate_var ** 3
    else:
        y = intermediate_var ** 3 + 1

    # settings attributes here
    func.optonal_return = intermediate_var
    func.is_awesome = 'Yes, my function is awesome.'

    return y

y = func(3)
print('Final answer is', y)

# Accessing function attributes
print('Show calculations -->', func.optional_return)
print('Is my function awesome? -->', func.is_awesome)

#12 func with default values

def say(message, times = 1):  # default can be only end of list of default parameters def func(a, b=6), but not def func(a=5, b)

    print(message * times)
    say('Hello')
    say('World', 5)
result:
    Hello
    WorldWorldWorldWorldWorld

# 

def is_laundry_day(today, laundry_day = "Monday", on_vacation = False):
    if today is laundry_day and today != "Sunday" and on_vacation is False:
        return True
    else:
        return False

print(is_laundry_day("Tuesday"))
print(is_laundry_day("Tuesday", "Tuesday"))
print(is_laundry_day("Friday", "Friday", True))

#13 kwargs

def func(a, b=5, c=10):
    print('a eqwl', a, ', b eqwl', b, ', and c eqwl', c)

func(3,7)
func(25, c=24)
func(c=50, a=100)
results:
    a eqwl 3, b eqwl 7, and c eqwl 10
    a eqwl 25, b eqwl 5, and c eqwl 24
    a eqwl 100, b eqwl 5, and c eqwl 50

#13-a **kwargs

def bild_profile(first, last, **user_info):  # **kwargs make an empty dict
    """Make a dict wiht info about user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einsteing',
                             location='princeton',
                             field='phisics')
print(user_profile)

Results:
    {'location': 'princeton', 'field': 'phisics',
            'first_name': 'albert', 'last_name': 'einstein'}

#14 VarArgs (Variable number of Arguments) or *args

def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print(total(10, 1, 2, 3, vegetables=50, fruits=100))

results:
    166

# more e.g.

def make_pizza(*toppings):
    """Return list of toppings."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

Results:
    Making a pizza with the following toppings:
        - pepperoni
    
    Making a pizza with the following toppings:
        - mushrooms
        - green peppers
        - extra cheese

#15 Not all cases included argument

def get_formated_name(first_name, last_name, middle_name=''):  # middle is not included
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formated_name('jimi', 'hendrix')  # if names included two names
print(musician)  # print two names

musician = get_formated_name('john', 'hooker', 'lee')  # if names included three names
print(musician)  # print three names

Results:
    Jimi Hendrix
    John Lee Hooker

or variant with return dict

def build_person(first_name, last_name, middle_name='', age=''):
    "Return dict with info about person."""
    person = {'first': first_name, 'last': last_name, 'middle': middle_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 'esquire', age=27)
print(musician)

Results:
    {'first': 'jimi', 'last': 'hendrix', 'middle': 'esquire', 'age': 27}

#16 function in while cicle

def get formatted_name(first_name, last_name):
    """Return formatted full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# !!! INFINITE CICLE..................

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if f_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

Results:
    Please tell me your name:
        (enter 'q' at any time to quit)
        First name: eric
        Last name: muffons

        Hello, Erric Muffons!

        Please tell me your name:
            (enter 'q' at any time to quit)
        First name: q

#17 func get list of names

def greet_users(names):
    """Return greetings for every user in list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'toffic', 'margot']
greet_users(usernames)

Results:
    Hello, Hannah!
    Hello, Toffic!
    Hello, Margot!

#18 change list into function, 

# e.g whithout function
# list models for printing
unpinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print models in while cicle
# go models to list of completed models
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Return all completed models
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

Results:
    Printing model: dodecahedron
    Printing model: robot pendant
    Printing model: phone case

    The following models have been printed:
        dodecahedron
        robot pendant
        phone case

# e.g with functions

def print_models(unprinted_designs, completed_models):
    """Imitated printing models, and after work move to 
    completed_models.
    """
    while unprinted_disigns:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Return info about printed models."""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)  # for change original list(faster)
or
print_models(unprinted_designs[:], completed_models)  # for copy original list(slower)
show_completed_models(completed_models)

Results:
    Printing model: dodecahedron
    Printing model: robot pendant
    Printing model: phone case

    The following models have been printed:
        dodecahedron
        robot pendant
        phone case

#19 example how use function for check internet
import httplib

def check_web_server(host, port, path):  # or use kwargs (port=80, path='/', host='www.python.org')
    h = httplib.HTTPConnection(host, port)
    h.request('GET', path)
    resp = h.getresponse()
    print('HTTP Response:')
    print('    status =', resp.status)
    print('    reason =', resp.reason)
    print('HTTP Headers: ')
    for hdr in resp.getheaders():
        print('    %s: %s' % hdr)

Results:
>>> check_web_server('www.python.org', 80, '/')
HTTP Response:
    status = 200
    reason = OK
HTTP Headers:
    content-length: 16793
    accept-ranges: bytes
    server: Apache/2.2.3 (Debian) DAV/2 SVN/1.4.2 mod_ssl/2.2.3 OpenSSL/0.9.8c
    last-modified: Sun, 27 Apr
    etag: "6008a-4199-df35c889"
    date: Sun, 27 Apr
    content-type: text/html

#20 Get object of function but not function

import datetime

class DiaryEntry(model.Model):
    entry = models.TextField()
    date = models.DateField(default=datetime.date.today)  # but not datetime()

#21
