"""A Functions about."""

# Defining the function

def func(name):
    print("Hi",name)

# Calling the function

func("Chirag")

######

# Defining the function for sum of two variables

def sum(num1,num2):
    return num1 + num2

# Taking values from the user as an input

num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))

# Calculating and Printing the sum of num1 and num2

print("Sum = ",sum(num1,num2))

###### maximum from the given three numbers

def max_of_two(x, y):
    if x > y:
        return x
    return y

def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))

print(max_of_three(3, 6, -5))

###### calculate the sum of all the numbers present in a list

def sum(numbers):
    total = 0
    for element in numbers:
        total += element
    return total
print(sum((8, 2, 8, 0, 7)))

###### calculate the multiplication of all the numbers present in a list

def multiply(numbers):
    total = 1
    for element in numbers:
        total *= element
    return total

print(multiply((3, 8, 2, -1, 7)))

###### takes a string as an input and calculates the number of upper case
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

###### program that takes a number(non-negative integer) as an argument
#      and calculates its factorial.

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

number = int(input("Input a number to compute the factorial : "))
print(factorial(number))

###### 
