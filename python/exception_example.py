"""Exception about."""

#1
'''
class MyError(Exception):
    pass

try:
    raise MyError("Some information \
about what went wrong")
except MyError as error:
    print("Situation:", error) 
try:
    raise MyError("Some information", "my_filename", 3)
except MyError as error:
    print("Situation: {0} with file {1}\n error code: {2}".format\
            (error.args[0],error.args[1],error.args[2]))

#2 Try except catching multiple exception and with else block

x = input('Enter numenator : ')
y = input('Enter denomenator : ')

try:
    a = int(x)
    b = int(y)
    c = a/b
except ValueError:
    print('Check if input string is parsable integer')
except ZeroDivisionError:
    print('Denomenator is zero.')
except TypeError:
    print("That wasn't a number, was it?")
except(ZeroDivisionError, TypeError, NameError):  # more exception for the God of Exceptions
    print("Your numbers were bogus...")
else:
    print('No Errors.')

#3 
class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise
calculator = MuffledCalculator()
print(calculator.calc('10/2'))  # 5.0
#print(calculator.calc('10/0'))  # Error, no muffling
calculator.muffled = True
print(calculator.calc('10/0'))  # Division by zero is illegal

#4 
while True:
    try:
        x = int(input('Enter the first number:'))
        y = int(input('Enter the second number:'))
        value = x/y
        print('x/y is', value)
    except Exception as e:
        print('Invalid input:', e)
        print('Please try again')
    else:
        break
'''
#5 Finally
x = None
try:
    x = 1/1  # if x = 1/0 Error
    
except NameError:
    print("Unknown variable")
else:
    print("That went well!")
finally:
    print('Cleaning up ...')
    del x

#5
