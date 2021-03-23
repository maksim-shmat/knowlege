""" Little bit examples python/django about."""

###### Iterables

class Fibonacci(object):
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        a, b = 0, 1
        for x in range(self.count):
            if x < 2:
                yield x
            else:
                c = a + b
                yield c
                a, b = b, c

for x in Fibonacci(5):
    print(x)

for x in Fibonacci(10):
    print(x)

###### next(self)
class FibonacciIterator(object):
    def __init__(self, count):
        self.a = 0
        self.b = 1
        self.count = count
        self.current = 0

    def __next__(self):
        self.current += 1
        if self.current > self.count:
            raise StopIteration
        if self.current < 3:
            return self.current -1
        c = self.a + self.b
        self.a = self.b
        self.b = c
        return c
    next = __next__

    def __iter__(self):
        # Since it's already an iterator, this can return itself.
        return self

class Fibonacci(object):
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return FibonacciIterator(self.count)

###### Positional Arguments

def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

multiply(2, 3)

multiply(2, 3, 4, 5, 6)

###### Keyword Arguments

def accept(**kwargs):
    for keyword, value in kwargs.items():
        print("%s -> %r" % (keyword, value))

accept(foo='bar', span='eggs')

###### Decorators

def decorate(func):
    print('Decorating %s...' % func.__nam__)
    def wrapped(*args, **kwargs):
        print("Called wrapped function with args:", args)
        return func(*args, **kwargs)
    print('done!')
    return wrapped

def test(a, b):
    return a + b

test = decorate(test)

test(13, 72)

### 
def test(a, b):
    return a + b

def decorate(func, prefix='Decorated'):
    def wrapped(*args, **kwargs):
        return '%s: %s' % (prefix, func(*args, **kwargs))
    return wrapped

###
from django.utils.functional import curry
@curry(decorate, prefix='Curried')
def test(a, b):
    return a + b

###
def decorate(prefix='Decorated'):
    # The prefix passed in here will be
    # available to all the inner functions
    def decorator(func):
        # This is called with func being the
        # actual function being decorated
        def wrapper(*args, **kwargs):
            # This will be called each time
            # the real function is executed
            return '%s: %s' % (prefix, func(*args, **kwargs))
        # Send the wrapped function
        return wrapper
    # Provide the decorator for Python to use
    return decorator

@decorate('Easy')
def test(a, b):
    return a + b

test(13, 17)

test(89, 121)

### decorator with or without arguments

def decorate(func=None, prefix='Decorated'):
    def decorated(func):
        # This returns the final, decorated
        # function, regardless of how it was called
        def wrapper(*args, **kwargs):
            return '%s: %s' % (prefix, func(*args, **kwargs))
        return wrapper
    if func is None:
        # The decorator was called with arguments
        def decorator(func):
            return decorated(func)
        return decorator
    # The decorator was called without arguments
    return decorated(func)

@ decorate
def test(a, b):
    return a + b

test(13, 17)

@decorate(prefix='Arguments')
def test(a, b):
    return a + b

test(13, 17)

######
def optional_arguments_decorator(real_decorator):
    def decorator(func=None, **kwargs):
        # This is the decorator that will be
        # exposed to the rest of your program
        def decorated(func):
            # This returns the final, decorated
            # function, regardless of how it was called
            def wrapper(*a, **kw):
                return real_decorator(func, a, kw **kwargs)
            return wrapper
        if func is None:
            # The decorator was called with arguments
            def decorator(func):
                return decorated(func)
            return decorator
        # The decorator was called without arguments
        return decorated(func)
    return decorator

@optional_arguments_decorator
def decorate(func, args, kwargs, prefix='Decorated'):
    return '%s: %s' % (prefix, func(*args, **kwargs))

@decorate
def test(a, b):
    return a + b

test(13, 17)

test = decorate(test, prefix='Decorated again')

test(13, 17)

###### Descriptors
import datetime

class CurrentDate(object):
    def __get__(self, instance, owner):
        return datetime.date.today()
    def __set__(self, instance, value):
        raise NotImplementedError("Can't change the current date.")

class Example(object):
    date = CurrentDate()

e = Example()

e.date

### keep track of instance data

class Descriptor(object):
    
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class TestObject(object):
    attr = Descriptor('attr')

test = TestObject()
test.attr = 6
test.attr

###### Checking for Specific Types

class CustomDict(dict):
    pass    # Pretend there's something more useful here

issubclass(CustomDict, dict)

issubclass(CustomDict, CustomDict)

my_dict = CustomDict()

isinstance(my_dict, dict)

isinstance(my_dict, CustomDict)

######
