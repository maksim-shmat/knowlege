"""max() about, and min()"""

# find maximum of iterable

a = [18, 52, 23, 41, 32]
largest = max(a)
print(f'Largest number in the list is : {largest}.')
print()

###### find maximum of two or more items

largest = max(18, 52, 23, 41, 32)
print(f'Largest number in the list is : {largest}.')
print()

###### max() with key function

a = [18, 52, 23, 41, 32]
keyfunc = lambda x: x % 10
largest = max(a, key=keyfunc)
print(f'Number that leaves largest reminder is : {largest}.')
print()

###### max() with default value

a = []
largest = max(a, default = 99)
print(f'Largest number in the list is : {largest}.')
print()

######
