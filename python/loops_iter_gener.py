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

######
