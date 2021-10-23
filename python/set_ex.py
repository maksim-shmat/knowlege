"""Set examples."""

######1 Intersection of two sets

set_1 = {'a', 'b', 'c', 'd'}
set_2 = {'a', 'b', 'd', 'm'}

set_output = set_1.intersection(set_2)
print(set_output)

### Intersection of more than two sets

set_1 = {'a', 'b', 'c', 'd'}
set_2 = {'a', 'b', 'd', 'm'}
set_3 = {'d', 'p', 's', 'v'}

set_output = set_1.intersection(set_2).intersection(set_3)
print(set_output)
print()

######2 Set difference

set_1 = {'a', 'b', 'c', 'd'}
set_2 = {'c', 'd', 'e', 'f'}

set_3 = set_1.difference(set_2)
print(set_3)

### set difference() method chaining

set_1 = {'a', 'b', 'c', 'd'}
set_2 = {'c', 'd', 'e', 'f'}
set_3 = {'a'}
set_4 = set_1.difference(set_2).difference(set_3)
print(set_4)

######3 Copy set

set_1 = {32, 56, 19}
set_2 = set_1.copy()
print('set 1:', set_1)
print('set 2:', set_2)

set_2.add(47)
print('\nafter modification')
print('set 1:', set_1)
print('set 2:', set_2)

### Copy set to multiple variables

set_1 = {32, 56, 19}
set_2 = set_3 = set_1.copy()

print('set 1:', set_1)
print('set 2:', set_2)
print('set 3:', set_3)
print()

######4 Set difference_update()

set_1 = {'a', 'b', 'c', 'd'}
set_2 = {'c', 'd', 'e', 'f'}

set_1.difference_update(set_2)
print(set_1)
print()

######5 Add an element to set

set_1 = {'a', 'b', 'c'}
set_1.add('g')
print(set_1)
print()

######6 Remove an item from set

set_1 = {'a', 'b', 'c'}
set_1.remove('b')
print(set_1)

### Remove an item not presented in the set

set_1 = {'a', 'b', 'c'}
item = 'f'
if item in set_1:
    set_1.remove('f')
else:
    print('item not in set')
print()

### Remove an item from set with discard()

set_1 = {'a', 'b', 'c', 'd'}
set_1.discard('c')
print(set_1)

### Remove an element not presented in set

set_1 = {'a', 'b', 'c', 'd'}
set_1.discard('k')
print(set_1)

######7 Clear set

set_1 = {'a', 'b', 'c'}
set_1.clear()
print(set_1)

### Clear an empty set

set_1 = {}
set_1.clear()
print(set_1)
print()

######8
