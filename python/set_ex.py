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

######2
