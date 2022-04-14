"""A Functions about."""

#1 Defining the function

def func(name):  # 'name' is parameter
    print("Hi",name)

# Calling the function
func("Chirag")  # 'Chirag' is argument

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

def say(message, times = 1):  # default may be only end of list of default parameters def func(a, b=6), but not def func(a=5, b)

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

#14 VarArgs (Variable number of Arguments)

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

#15 
