"""Exception about."""

######1

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

######2 Try except catching multiple exception and with else block

x = input('Eneter numenator : ')
y = input('Enter denomenator : ')

try:
    a = int(x)
    b = int(y)
    c = a/b
except ValueError:
    print('Check if input string is parsable integer')
except ZeroDivisionError:
    print('Denomenator is zero.')
else:
    print('No Errors.')

######3
