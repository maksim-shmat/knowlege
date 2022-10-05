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

#2 math floor to integers: trunc(), floor(), ceil - ., >, <

import math

HEADINGS = ('i', 'int', 'trunk', 'floor', 'ceil')
print('{:^5} {:^5} {:^5} {:^5} {:^5}'.format(*HEADINGS))
print('{:^5} {:-^5} {:-^5} {:-^5} {:-^5}'.format(
    '', '', '', '', '',
))

fmt = '{:5.1f} {:5.1f} {:5.1f} {:5.1f} {:5.1f}'

TEST_VALUES = [
        -1.5,
        -0.8,
        -0.5,
        -0.2,
        0,
        0.2,
        0.5,
        0.8,
        1,
]

for i in TEST_VALUES:
    print(fmt.format(
        i,
        int(i),
        math.trunc(i),
        math.floor(i),
        math.ceil(i),
))

'''RESULTS:
  i    int  trunk floor ceil
      ----- ----- ----- -----
 -1.5  -1.0  -1.0  -2.0  -1.0
 -0.8   0.0   0.0  -1.0   0.0
 -0.5   0.0   0.0  -1.0   0.0
 -0.2   0.0   0.0  -1.0   0.0
  0.0   0.0   0.0   0.0   0.0
  0.2   0.0   0.0   0.0   1.0
  0.5   0.0   0.0   0.0   1.0
  0.8   0.0   0.0   0.0   1.0
  1.0   1.0   1.0   1.0   1.0
'''

#3 modf()

import math

for i in range(6):
    print('{}/2 = {}'.format(i, math.modf(i / 2.0)))
    
'''RESULTS:
0/2 = (0.0, 0.0)
1/2 = (0.5, 0.0)
2/2 = (0.0, 1.0)
3/2 = (0.5, 1.0)
4/2 = (0.0, 2.0)
5/2 = (0.5, 2.0)
'''

#4  frexp() use x=m*2**e and return mantice and exponent

import math

print('{:^7} {:^7} {:^7}'.format('x', 'm', 'e'))
print('{:-^7} {:-^7} {:-^7}'.format('', '', ''))

for x in [0.1, 0.5, 4.0]:
    m, e = math.frexp(x)
    print('{:7.2f} {:7.2f} {:7d}'.format(x, m, e))

'''RESULTS:
   x       m       e   
------- ------- -------
   0.10    0.80      -3
   0.50    0.50       0
   4.00    0.50       3
'''

#4 ldexp() against frexp()

import math

print('{:^7} {:^7} {:^7}'.format('m', 'e', 'x'))
print('{:-^7} {:-^7} {:-^7}'.format('', '', ''))

INPUTS = [
        (0.8, -3),
        (0.5, 0),
        (0.5, 3),
]

for m, e in INPUTS:
    x = math.ldexp(m, e)
    print('{:7.2f} {:7d} {:7.2f}'.format(m, e, x))

'''RESULTS:
   m       e       x   
------- ------- -------
   0.80      -3    0.10
   0.50       0    0.50
   0.50       3    4.00
'''

#5 fabs() for absolute value of number

import math

print(math.fabs(-1.1))
print(math.fabs(-0.0))
print(math.fabs(0.0))
print(math.fabs(1.1))

'''RESULTS:
1.1
0.0
0.0
1.1
'''

#6 fsum(), 0.1 * 10 = 1, but not on the computer, need fsum()

import math

values = [0.1] * 10
print('Input values:', values)
print('sum()        : {:.20f}'.format(sum(values)))

s = 0.0
for i in values:
    s += i
print('for-loop     : {:.20f}'.format(s))
print('math.fsum()  : {:.20f}'.format(math.fsum(values)))

'''RESULTS:
Input values: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
sum()        : 0.99999999999999988898
for-loop     : 0.99999999999999988898
math.fsum()  : 1.00000000000000000000
'''

#7 factorial()
