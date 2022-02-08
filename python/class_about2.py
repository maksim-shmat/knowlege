"""More examples for the God of Examples python class about."""

#1

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_older(self, years):
        self.age += years


class Programmer(Person):

    def __init__(self, name, age, language):
        super(Programmer, self).__init__(name, age)
        self.language = language

    def print_language(self):
        print("Favorite Programming Language: {}".format(self.language))

p1 = Programmer("Mike", 30, "Python")

print(p1.age)
print(p1.name)
print(p1.language)
p1.get_older(5)
print(p1.age)

#2

class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "X:%d, Y:%d" % (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

v1 = Vector(3, 5)
v2 = Vector(6, 2)
v3 = v1 + v2
v4 = v1 - v2

print(v1)
print(v2)
print(v4)

#3 Simple example

__metaclass__ = type  # Include this if you're using Python2

class Person:

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))

foo = Person()
bar = Person()

foo.set_name('Luke')
bar.set_name('Anka')

print(foo.greet())  # Hello, world! I'm Luke
print(bar.greet())  # Hello, world! I'm Anka

print(foo.name)
bar.name = 'Yaga'
print(bar.greet())

#4 
