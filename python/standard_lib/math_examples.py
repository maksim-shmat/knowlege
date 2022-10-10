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

import math

for i in [0, 1, 2, 3, 4, 5, 6]:
    try:
        print('{:2.0f} {:6.0f}'.format(i, math.factorial(i)))
    except ValueError as err:
        print('Error computing factorial({}): {}'.format(i, err))

'''RESULTS:
 0      1
 1      1
 2      2
 3      6
 4     24
 5    120
 6    720
'''

#8 gamma() (n - 1) !

import math

for i in [0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6]:
    try:
        print('{:2.1f} {:6.2f}'.format(i, math.gamma(i)))
    except ValueError as err:
        print('Error computing gamma({}): {}'.format(i, err))

'''RESULTS:
Error computing gamma(0): math domain error
1.1   0.95
2.2   1.10
3.3   2.68
4.4  10.14
5.5  52.34
6.6 344.70
'''

#9 lgamma()

import math

for i in [0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6]:
    try:
        print('{:2.1f} {:.20f} {:.20f}'.format(
            i,
            math.lgamma(i),
            math.log(math.gamma(i)),
        ))
    except ValueError as err:
        print('Error computing lgamma({}): {}'.format(i, err))

'''RESULTS:
Error computing lgamma(0): math domain error
1.1 -0.04987244125984036103 -0.04987244125983997245
2.2 0.09694746679063825923 0.09694746679063866168
3.3 0.98709857789473387513 0.98709857789473409717
4.4 2.31610349142485727469 2.31610349142485727469
5.5 3.95781396761871651080 3.95781396761871606671
6.6 5.84268005527463252236 5.84268005527463252236
'''

#10 fmod() against %

import math

print('{:^4} {:^4} {:^5} {:^5}'.format(
    'x', 'y', '%', 'fmod'))

print('{:-^4} {:-^4} {:-^5} {:-^5}'.format(
    '-', '-', '-', '-'))

INPUTS = [
        (5, 2),
        (5, -2),
        (-5, 2),
]

for x, y in INPUTS:
    print('{:4.1f} {:4.1f} {:5.2f} {:5.2f}'.format(
        x,
        y,
        x % y,
        math.fmod(x, y),
    ))

'''RESULTS:
x    y     %   fmod 
---- ---- ----- -----
 5.0  2.0  1.00  1.00
 5.0 -2.0 -1.00  1.00
-5.0  2.0  1.00 -1.00
'''

#11 gcd() great common divisioned?

import math

print(math.gcd(10, 8))
print(math.gcd(10, 0))
print(math.gcd(50, 225))
print(math.gcd(11, 9))
print(math.gcd(0, 0))

'''RESULTS:
2
10
25
1
0
'''

#12 pow() == **

import math

INPUTS = [
        # Typical uses
        (2, 3),
        (2.1, 3.2),

        # 1 Always
        (1.0, 5),
        (2.0, 0),

        # NaN
        (2, float('nan')),

        # Squareroots
        (9.0, 0.5),
        (27.0, 1.0 / 3),
]

for x, y in INPUTS:
    print('{:5.1f} ** {:5.3f} = {:6.3f}'.format(
        x, y, math.pow(x, y)))

'''RESULTS:
2.0 ** 3.000 =  8.000
  2.1 ** 3.200 = 10.742
  1.0 ** 5.000 =  1.000
  2.0 ** 0.000 =  1.000
  2.0 **   nan =    nan
  9.0 ** 0.500 =  3.000
 27.0 ** 0.333 =  3.000
'''
#13 math.sqrt()

import math

print(math.sqrt(9.0))
print(math.sqrt(3))
try:
    print(math.sqrt(-1))
except ValueError as err:
    print('Cannot compute sqrt(-1):', err)

'''RESULTS:
3.0
1.7320508075688772
Cannot compute sqrt(-1): math domain error
'''

#14 math.log() find y if x = b ** y

import math

print(math.log(8))
print(math.log(8, 2))
print(math.log(0.5, 2))

'''RESULTS:
2.0794415416798357
3.0
-1.0
'''

#15 math.log10

import math

print('{:2} {:^12} {:^10} {:^20} {:8}'.format(
    'i', 'x', 'accurate', 'inaccurate', 'mismatch',
))
print('{:-^2} {:-^12} {:-^10} {:-^20} {:-^8}'.format(
    '', '', '', '', '',
))

for i in range(0, 10):
    x = math.pow(10, i)
    accurate = math.log10(x)
    inacurate = math.log(x, 10)
    match = '' if int(inacurate) == i else '*'
    print('{:2d} {:12.1f} {:10.8f} {:20.18f} {:^5}'.format(
        i, x, accurate, inacurate, match,
    ))

'''RESULTS:
i       x        accurate       inaccurate      mismatch
-- ------------ ---------- -------------------- --------
 0          1.0 0.00000000 0.000000000000000000      
 1         10.0 1.00000000 1.000000000000000000      
 2        100.0 2.00000000 2.000000000000000000      
 3       1000.0 3.00000000 2.999999999999999556   *  
 4      10000.0 4.00000000 4.000000000000000000      
 5     100000.0 5.00000000 5.000000000000000000      
 6    1000000.0 6.00000000 5.999999999999999112   *  
 7   10000000.0 7.00000000 7.000000000000000000      
 8  100000000.0 8.00000000 8.000000000000000000      
 9 1000000000.0 9.00000000 8.999999999999998224   *  
'''

#16 log2

import math

print('{:>2} {:^5} {:^5}'.format(
    'i', 'x', 'log2',
))
print('{:-^2} {:-^5} {:-^5}'.format(
    '', '', '',
))

for i in range(0, 10):
    x = math.pow(2, i)
    result = math.log2(x)
    print('{:2d} {:5.1f} {:5.1f}'.format(
        i, x, result,
    ))

'''RESULTS:
i   x   log2 
-- ----- -----
 0   1.0   0.0
 1   2.0   1.0
 2   4.0   2.0
 3   8.0   3.0
 4  16.0   4.0
 5  32.0   5.0
 6  64.0   6.0
 7 128.0   7.0
 8 256.0   8.0
 9 512.0   9.0
'''

#17 log1p() for rows Newton-Mercator

import math

x = 0.0000000000000000000000001
print('x        :', x)
print('1 + x    :', 1 + x)
print('log(1+x) :', math.log(1 + x))
print('log1p(x) :', math.log1p(x))

'''RESULTS:
x        : 1e-25
1 + x    : 1.0
log(1+x) : 0.0
log1p(x) : 1e-25
'''

#18 math.exp()  (e**x)

import math

x = 2

fmt = '{:.20f}'
print(fmt.format(math.e ** 2))
print(fmt.format(math.pow(math.e, 2)))
print(fmt.format(math.exp(2)))

'''RESULTS:
7.38905609893064951876
7.38905609893064951876
7.38905609893065040694
'''

#19 expm1() contrarivice log1p(), and it is for e**x - 1

import math

x = 0.0000000000000000000000001

print(x)
print(math.exp(x) - 1)
print(math.expm1(x))

'''RESULTS:
1e-25
0.0
1e-25
'''

#20 radians() rad = grad*П/180

import math

print('{:^7} {:^7} {:^7}'.format(
    'Degrees', 'Radians', 'Expected'))
print('{:-^7} {:-^7} {:-^7}'.format(
    '', '', ''))

INPUTS = [
        (0, 0),
        (30, math.pi /6 ),
        (45, math.pi / 4),
        (60, math.pi / 3),
        (90, math.pi / 2),
        (180, math.pi),
        (270, 3 / 2.0 * math.pi),
        (360, 2 * math.pi),
]

for deg, expected in INPUTS:
    print('{:7d} {:7.2f} {:7.2f}'.format(
        deg,
        math.radians(deg),
        expected,
    ))

'''RESULTS:
Degrees Radians Expected
------- ------- -------
      0    0.00    0.00
     30    0.52    0.52
     45    0.79    0.79
     60    1.05    1.05
     90    1.57    1.57
    180    3.14    3.14
    270    4.71    4.71
    360    6.28    6.28
'''

#21 degrees() deg = rad * 180/П

import math

INPUTS = [
        (0, 0),
        (math.pi / 6, 30),
        (math.pi / 4, 45),
        (math.pi / 3, 60),
        (math.pi / 2, 90),
        (math.pi, 180),
        (3 * math.pi / 2, 270),
        (2 * math.pi, 360),
]

print('{:^8} {:^8} {:^8}'.format(
    'Radians', 'Degrees', 'Expected'))
print('{:-^8} {:-^8} {:-^8}'.format('', '', ''))
for rad, expected in INPUTS:
    print('{:8.2f} {:8.2f} {:8.2f}'.format(
        rad,
        math.degrees(rad),
        expected,
    ))

'''RESULTS:
Radians  Degrees  Expected
-------- -------- --------
    0.00     0.00     0.00
    0.52    30.00    30.00
    0.79    45.00    45.00
    1.05    60.00    60.00
    1.57    90.00    90.00
    3.14   180.00   180.00
    4.71   270.00   270.00
    6.28   360.00   360.00
'''

#22 trigonometry: sine, cosine, tangent

import math

print('{:^7} {:^7} {:^7} {:^7} {:^7}'.format(
    'Degrees', 'Radians', 'Sine', 'Cosine', 'Tangent'))
print('{:-^7} {:-^7} {:-^7} {:-^7} {:-^7}'.format(
    '-', '-', '-', '-', '-'))

fmt = '{:7.2f} {:7.2f} {:7.2f} {:7.2f} {:7.2f}'

for deg in range(0, 361, 30):
    rad = math.radians(deg)
    if deg in (90, 270):
        t = float('inf')
    else:
        t = math.tan(rad)
    print(fmt.format(deg, rad, math.sin(rad), math.cos(rad), t))

'''RESULTS:
Degrees Radians  Sine   Cosine  Tangent
------- ------- ------- ------- -------
   0.00    0.00    0.00    1.00    0.00
  30.00    0.52    0.50    0.87    0.58
  60.00    1.05    0.87    0.50    1.73
  90.00    1.57    1.00    0.00     inf
 120.00    2.09    0.87   -0.50   -1.73
 150.00    2.62    0.50   -0.87   -0.58
 180.00    3.14    0.00   -1.00   -0.00
 210.00    3.67   -0.50   -0.87    0.58
 240.00    4.19   -0.87   -0.50    1.73
 270.00    4.71   -1.00   -0.00     inf
 300.00    5.24   -0.87    0.50   -1.73
 330.00    5.76   -0.50    0.87   -0.58
 360.00    6.28   -0.00    1.00   -0.00
'''

#23 hypot()

import math

print('{:^7} {:^7} {:^10}'.format('X', 'Y', 'Hypotenuse'))
print('{:-^7} {:-^7} {:-^10}'.format('', '', ''))

POINTS = [
        (1, 1),
        (-1, -1),
        (math.sqrt(2), math.sqrt(2)),
        (3, 4),
        (math.sqrt(2) / 2, math.sqrt(2) / 2),
        (0.5, math.sqrt(3) / 2),
]

for x, y in POINTS:
    h = math.hypot(x, y)
    print('{:7.2f} {:7.2f} {:7.2f}'.format(x, y, h))

'''RESULTS:
  X       Y    Hypotenuse
------- ------- ----------
   1.00    1.00    1.41
  -1.00   -1.00    1.41
   1.41    1.41    2.00
   3.00    4.00    5.00
   0.71    0.71    1.00
   0.50    0.87    1.00
'''

#24 distance 2 points

import math

print('{:^8} {:^8} {:^8} {:^8} {:^8}'.format(
    'X1', 'Y1', 'X2', 'Y2', 'Distance',
))
print('{:-^8} {:-^8} {:-^8} {:-^8} {:-^8}'.format(
    '', '', '', '', '',
))

POINTS = [
        ((5, 5), (6, 6)),
        ((-6, -6), (-5, -5)),
        ((0, 0), (3, 4)),
        ((-1, -1), (2, 3)),
]

for (x1, y1), (x2, y2) in POINTS:
    x = x1 - x2
    y = y1 - y2
    h = math.hypot(x, y)
    print('{:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f}'.format(
        x1, y1, x2, y2, h,
    ))

'''RESULTS:
 X1       Y1       X2       Y2    Distance
-------- -------- -------- -------- --------
    5.00     5.00     6.00     6.00     1.41
   -6.00    -6.00    -5.00    -5.00     1.41
    0.00     0.00     3.00     4.00     5.00
   -1.00    -1.00     2.00     3.00     5.00
'''

#25 inverse trigonometry: arcsine, arccosine, arctangent

import math

for r in [0, 0.5, 1]:
    print('arcsine({:.1f})    = {:5.2f}'.format(r, math.asin(r)))
    print('arccosine({:.1f})  = {:5.2f}'.format(r, math.acos(r)))
    print('arctangent({:.1f}) = {:5.2f}'.format(r, math.atan(r)))
    print()

'''RESULTS:
arcsine(0.0)    =  0.00
arccosine(0.0)  =  1.57
arctangent(0.0) =  0.00

arcsine(0.5)    =  0.52
arccosine(0.5)  =  1.05
arctangent(0.5) =  0.46

arcsine(1.0)    =  1.57
arccosine(1.0)  =  0.00
arctangent(1.0) =  0.79
'''

#26 hyperbolic: sinh, sosh, tanh

import math

print('{:^6} {:^6} {:^6} {:^6}'.format(
    'X', 'sinh', 'cosh', 'tanh',
    ))
print('{:-^6} {:-^6} {:-^6} {:-^6}'.format('', '', '', ''))

fmt = '{:6.4f} {:6.4f} {:6.4f} {:6.4f}'

for i in range(0, 11, 2):
    x = i / 10.0
    print(fmt.format(
        x,
        math.sinh(x),
        math.cosh(x),
        math.tanh(x),
    ))

'''RESULTS:
  X     sinh   cosh   tanh 
------ ------ ------ ------
0.0000 0.0000 1.0000 0.0000
0.2000 0.2013 1.0201 0.1974
0.4000 0.4108 1.0811 0.3799
0.6000 0.6367 1.1855 0.5370
0.8000 0.8881 1.3374 0.6640
1.0000 1.1752 1.5431 0.7616
'''

#27 erf()

import math

print('{:^5} {:7}'.format('x', 'erf(x)'))
print('{:-^5} {:-^7}'.format('', ''))

for x in [-3, -2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, 3]:
    print('{:5.2f} {:7.4f}'.format(x, math.erf(x)))

'''RESULTS:
  x   erf(x) 
----- -------
-3.00 -1.0000
-2.00 -0.9953
-1.00 -0.8427
-0.50 -0.5205
-0.25 -0.2763
 0.00  0.0000
 0.25  0.2763
 0.50  0.5205
 1.00  0.8427
 2.00  0.9953
 3.00  1.0000
'''

#28 erfc() == 1 - erf(x)

import math

print('{:^5} {:7}'.format('x', 'erfc(x)'))
print('{:-^5} {:-^7}'.format('', ''))

for x in [-3, -2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, 3]:
    print('{:5.2f} {:7.4f}'.format(x, math.erfc(x)))

'''RESULTS:
  x   erfc(x)
----- -------
-3.00  2.0000
-2.00  1.9953
-1.00  1.8427
-0.50  1.5205
-0.25  1.2763
 0.00  1.0000
 0.25  0.7237
 0.50  0.4795
 1.00  0.1573
 2.00  0.0047
 3.00  0.0000
'''
