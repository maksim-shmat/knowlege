""" What in heaven's name django tests are you talking about?"""

###### wraps(func)

def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def test():
    print('Testing!')
decorated = decorator(test)
decorated.__nam__
# 'wrapper'

### wraps() from Python
from django.utils.functional import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def test():
    print('Testing!')

decorated = decorator(test)
decorated.__name__
# 'test'

######
