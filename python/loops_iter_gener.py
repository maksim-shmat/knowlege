"""Loops, Iterators, and Generators."""

###### Python implicit iterator behavior

astring = 'coffee'
coffee_types = ['Cappuccino','Latte','Macchiato']
address = {'city':'San Diego','state':'CA','country':'US'}

# Standard for loop, with implicit iterator
for letter in astring:
    print(letter)

# Loop with enumerator (counter)
for counter,letter in enumerate(astring):
    print(counter,letter)

# Standard for loop, with implicit iterator
for coffee in coffee_types:
    print(coffee)

# Loop with enumerator (counter), starting at 1
for counter,coffee in enumerate(coffee_types,start=1):
    print(counter,coffee)

# Standard for loop, with implicit iterator
for key,value in address.items():
    print(key,value)

# Standard for loop, with implicit iterator
for address_key in address.keys():
    print(address_key)

# Standard for loop, with implicit iterator
for address_value in address.values():
    print(address_value)

###### Python explicit iterator behavior

astring = 'coffee'
coffee_types = ['Cappuccino','Latte','Macchiato']

# Create explicit iterators
astring_iter = iter(astring)
coffee_types_iter = iter(coffee_types)

# Print iterator types
print(type(astring_iter))
print(type(coffee_types_iter))

# Call next() to advance over the iterator
# In Python 2 next() works the same (e.g. astring_iter.next())
# In Python 3 __next__() works the same (e.g. astring_iter.__next__())

# >>> next(astring_iter)
# 'c'

# Call next() to advice over the iterator
# In Python 3 __next__() works the same (e.g. coffee_types.__next__())
# >>> next(coffee_types_iter)
# 'Cappuccino'

order_numbers = iter([1,2,3,4,5,6,7,8,9,10])
# Get order number
# next(order_numbers)

###### Python generator behavior

def funky_order_numbers():
    yield 100
    yield 350
    yield 575
    yield 700
    yield 950

order_numbers = funky_order_numbers()
print(type(order_numbers))
# Call next() to advance over the generator
# >>> next(order_numbers)
# 100

def generate_order_numbers(n):
    for i in range(1,n):
        yield i

regular_order_numbers = generate_order_numbers(100)
# Call next() to advance over the generator
# >>> next(regulat_order_numbers)
# 1

def generate_infinite_order_numbers(n):
    while True:
        n += 1
        yield n

infinite_order_numbers = generate_infinite_order_numbers(1000)
# Call next() to advance over the generator
# >>> next(infinite_order_numbers)
# >>> 1001
# next() never reaches end due to infinite 'while True:' statement

######
