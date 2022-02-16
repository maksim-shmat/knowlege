"""About the decorators."""

'''
def  outer_function():
    """Assign task to student"""

    task = 'Read Python book chapter 3.'
    def inner_function():
        print(task)
    return inner_function

homework = outer_function()
homework()

### One func move to another func with how an argument
def friendly_reminder(func):
    """Reminder for husband"""

    func()
    print('Don\'t forget to bring your wallet!')

def action():
    print('I am going to the store buy you something nice.')
# Calling the friendly_reminder function with the action function used as an argument.
friendly_reminder(action)

# Make the func-decorator
# basic sintaxis

def my_decorator_func(func):

    def wrapper_func():
        # Do something before the function.
        func()
        # Do something after the function.
    return wrapper_func
# and more
@my_decorator_func
def my_func():

    pass

### simple example of decorator how generate date and time
from datetime import datetime

def log_datetime(func):
    """Log the date and time of a function"""

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper

@log_datetime
def daily_backup():
    
    print('Daily backup job has finished.')

daily_backup()

###### How add args to the decorators?
def my_decorator_func(func):

    def wrapper_func(*args, **kwargs):
        # Do something before the function.
        func(*args, **kwargs)
        # Do something after the function.
    return wrapper_func

@my_decorator_func
def my_func(my_arg):
    """Example docstring for function"""

    pass

### decorators hide function from ambient, use wraps that it is not good for you
from functools import wraps

def my_decorator_func(func):

    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func

@my_decorator_func
def my_func(my_args):
    """Example docstring for function"""

    pass
"""
###### decorator function how check speed and memory 
from functools import wraps
import tracemalloc
from time import perf_counter

def measure_performance(func):
    """Measure performance of a function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()
    return wrapper

@measure_performance
def make_list1():
    """Range"""
    
    my_list = list(range(100000))

@measure_performance
def make_list2():
    """List comprehension"""

    my_list = [l for l in range(100000)]

@measure_performance
def make_list3():
    """Append"""

    my_list = []
    for item in range(100000):
        my_list.append(item)

@measure_performance
def make_list4():
    """Concatenation"""

    my_list = []
    for item in range(100000):
        my_list = my_list + [item]

make_list1()
make_list2()
make_list3()
make_list4()

###### decorator with __call__
import requests

class LimitQuery:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.limit = args[0]
        if self.count < self.limit:
            self.count += 1
            return self.func(*args, **kwargs)
        else:
            print(f'No queries left. All {self.cont} used.')
            return

@LimitQuery

def get_coin_price():
    """View the Bitcoin Price Index (BPI)"""

    url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    if url.status_code == 200:
        text = url.json()
        return f("${float(text['bpi']['USD']['rate_flot']):.2f}")

get_coin_price(5)
get_coin_price(5)
get_coin_price(5)
get_coin_price(5)
get_coin_price(5)

###### simple example 

def  execute(user, action):
    self.authenticate(user)        # one
    self.authorize(user, action)   # two, not good, just only one
    return action()

### dicision with decorator

def execute(action, *args, **kwargs):
    return action()

def authenticated_only(method):
    def decorated(*args, **kwargs):
        if check_authenticated_only(method):
            return method(*args, **kwargs)
        else:
            raise UnauthenticatedError
    return decorated

def authorized_only(method):
    def decorated(*args, **kwargs):
        if check_authorized(kwargs['user'], kwargs['action']):
            return method(*args, **kwargs)
        else:
            raise UnauthorizedError
    return decorated

execute = authenticated_only(execute)
execute = authorized_only(execute)

### same name but with parent inserted decorator

def authenticated_only(method):
    def decorated(*args, **kwargs):
        if check_authenticated(kwargs['user']):
            return method(*args, **kwargs)
        else:
            raise UnauthenticatedError
    return decorated

def authorized_only(method):
    def decorated(*args, **kwargs):
        if check_authorized(kwargs['user'], kwargs['action']):
            return method(*args, **kwargs)
        else:
            raise UnauthorizedError
    return decorated

@authorized_only
@authenticated_only
def execute(action, *args, **kwargs):
    return action()
'''
#1
# old Python 2.4
class MyClass:
    def smeth():
        print('This is a static method')
    smeth = staticmethod(smeth)
    def cmeth(cls):
        print('This is a class method of', cls)
    cmeth = classmethod(cmeth)

# style with decorator from the new aegis

class MyClass1:
    @staticmethod
    def smeth1():
        print('This is a static method 1')

    @staticmethod
    def cmeth2(cls):
        print('This is a class method of 2', cls)

print(MyClass.smeth())
print(MyClass.cmeth())
print(MyClass1.smeth1())
print(MyClass1.cmeth2())  # ?


