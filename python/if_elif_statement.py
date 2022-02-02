"""About if and."""

a = 5
b = 2

# nested if 

if a==5:
    if b>0:
        print('a is 5 and',b,'is greater than zero.')

# or you can combine the conditions as

if a==5 and b>0:
    print('a is 5 and',b,'is greater than zero.')

###### Python if-else statement with and operator

a = 3
b = 2

if a==5 and b>0:
    print('a is 5 and',b,'is greater than zero.')
else:
    print('a is not 5 or',b,'is not greater than zero.')

###### Python elif statement with and operator

a = 8

if a<0:
    print('a is less than zero.')
elif a>0 and a<8:
    print('a is in(0,8)')
elif a>7 and a<15:
    print('a is in (7,15)')

######

a = 2
a = 4
a = 5

if a<b:
    print(a, 'is less than', b)
    if c<b:
        print(c, 'is less than', b)
    else:
        print(c, 'is not less than', b)
else:
    print(a, 'is not less than', b)

###### elif statement

a = 2
b = 4

if a<b:
    print(a, 'is less than', b)
elif a >b:
    print(a, 'is greater than', b)
else:
    print(a, 'equals', b)

###### elif with multiple elif blocks

a = 2
if a<0:
    print(a, 'is negative')
elif a==0:
    print('its a 0')
elif a>0 and a<5:
    print(a, 'is in (0,5)')
else:
    print(a, 'equals or greater than 5')

###### if with or operator

today = 'Saturday'

if today == 'Sunday' or today == 'Saturday':
    print('Today is off. Reset at home.')

###### if-else with or

today = 'Wednesday'

if today == 'Sunday' or today == 'Saturday':
    print('Today is off. Reset at home.')
else:
    print('Go to work.')

###### 

today = 'Sunday'

if today == 'Monday':
    print('Your weekend is over. Go to work.')
elif today == 'Sunday' or today == 'Saturday':
    print('Today is off.')
else:
    print('Go to work.')

###### if not - Boolean

a = False
if not a:
    print('a is false.')

###### if not - String

string_1 = ''
if not string_1:
    print('String is empty.')
else:
    print(string_1)

###### if not - List

a = []
if not a:
    print('List is empty.')
else:
    print(a)

###### if not - Dictionary

a = dict({})
if not a:
    print('Dictionary is empty.')
else:
    print(a)

###### if not - Set

a = set({})
if not a:
    print('Set is empty.')
else:
    print(a)

###### if not - Tuple

a = tuple()
if not a:
    print('Tuple is empty.')
else:
    print(a)

###### ternary operator

a, b = 2, 5

# get maximum of a, b
max = a if a > b else b

print(max)

##### print statements in python ternary operator

a, b = 2, 5

# ternary operator
print('Python') if a > b else print('Examples')

###### nested ternary operator

a, b, c = 15, 93, 22

# nested ternary operator
max = a if a > b and a > c else b if b > c else c

print(max)

#1 if/else in one string

name = input('What is your name?')

status = 'friend' if name.endswith("Gumby") else "stranger"
print(status)

#2 elif clauses

num = int(input('Enter a number:'))
if num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')
else:
    print('The numbe is zero')

#3 
