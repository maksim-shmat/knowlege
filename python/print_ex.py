"""print() about."""

import sys
def print3(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs: raise TypeError('extra keywords: %s' %kargs)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

###### alternative ver

import sys
def print3(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

"""Print string n-ones withot for or while."""

n=5
string="Hello World "
print(string * n) 

### print both variables
x = 'pi is'
y = 3.14
print(x,y)

### print() with a specific serparator
x = 'pi is'
y = 3.14
print(x, y, sep=' : ')

### print() with a specific end
print('Hello', end='-')
print('World', end='.\n')

"""print reverse parameters in column."""

def my_funct(*params):
    for i in reversed(params):
        print(i)

my_funct(1, 2 , 3, 4)
# Wow print in column!

"""For two print() print in one string."""

import sys
sys.stdout.write("Call of duty ")
sys.stdout.write("and Black Ops ")

print("Python ", end="")
print("Programming")
