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

######3
