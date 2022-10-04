"""Different math examples for python."""

###### rm_int

x = [1, 3, 5, 0, -1, 3, -2]
new_x = [i for i in x if i >= 0]
print(new_x)

###### make generator that show nechet integer. How check nechet? Is %2

odd_100 = (x for x in range(100) if x % 2)
for i in odd_100:
    print(i)

###### cubes from 11 to 15

cubes = {x: x**3 for x in range(11,16)}
print(cubes)

######
"""Find min."""

def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first

def min3(* args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print(min1(3, 4, 1, 2))
print(min2("bob", "aa"))
print(min3([2,2], [1,1], [3,3]))

#1 constants

import math

print('  п: {:.30f}'.format(math.pi))
print('  e: {:.30f}'.format(math.e))
print('NaN: {:.30f}'.format(math.nan))
print('Inf: {:.30f}'.format(math.inf))

'''RESULTS:
  п: 3.141592653589793115997963468544
  e: 2.718281828459045090795598298428
NaN: nan
Inf: inf
'''

#2 math integers
