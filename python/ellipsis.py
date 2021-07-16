"""Ellipsis is a tripledots."""

### for not writen code yet
def some_function():
    ...

def another_function():
    pass

### NONE alternative
# calculate nth odd number
def nth_odd(n):
    if isinstance(n, int):
        return 2 * n - 1
    else:
        return None

# calculate the original n of nth odd number
def original_num(m=...):
    if m is ...:
        print('This function needs some input')
    elif m is None:
        print('Non integer input provided to nth_odd() function')
    elif isinstance(m, int):
        if m % 2:
            print(f'{m} is {int((m+1)/2)}th odd number')
        else:
            print(f'{m} is not an odd number')

original_num()

a = nth_odd(n='some string')
original_num(a)

b = nth_odd(5)
original_num(b)

original_num(16)
