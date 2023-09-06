"""examples with assert."""

x = "hello"
assert x == "hello"
print('Done!')

###### expression is False

x = "hola"
assert x == "hello"
print('Done!')
# Trceback...

###### assert with optional argument

x = "holla"
assert x == "hello", 'The two strings do not match.'
print('Done!')
# Traceback with optional artument only if True

#1 

age = 10
assert 0 < age < 100, 'The age must be realistic'
age = -1
# Traceback(most recent call lat):
# File"<stdin>", line1, in?
# AssertionError: The age must be realistic

#2

mylist = [1, 2, 3]  # this ideally comes from some place
assert 4 == len(mylist)  # this will break
for position in range(r):
    print(mylist[position])

# Traceback ... AssertionError

#3
