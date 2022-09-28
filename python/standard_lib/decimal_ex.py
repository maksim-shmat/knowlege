"""Decimal about."""

#1 create

import decimal

fmt = '{0:<25} {1:<25}'
print(fmt.format('Input', 'Output'))
print(fmt.format('-' * 25, '-' * 25))

# Whole number
print(fmt.format(5, decimal.Decimal(5)))

# String
print(fmt.format('3.14', decimal.Decimal('3.14')))

# Number with float dot
f = 0.1
print(fmt.format(repr(f), decimal.Decimal(str(f))))
print('{:<0.23g} {:<25}'.format(
    f,
    str(decimal.Decimal.from_float(f))[:25])
)

'''RESULTS:
Input                     Output                   
------------------------- -------------------------
5                         5                        
3.14                      3.14                     
0.1                       0.1                      
0.10000000000000000555112 0.10000000000000000555111
'''

#2 decimal tuple

import decimal

print()
t = (1, (1, 1), -2)
print('Input  :', t)
print('Decimal:', decimal.Decimal(t))

'''RESULTS:
Input  : (1, (1, 1), -2)
Decimal: -0.11
'''
#3 format()

import decimal

print()
d = decimal.Decimal(1.1)
print('Precision:')
print('{:.1}'.format(d))
print('{:.2}'.format(d))
print('{:.3}'.format(d))
print('{:.18}'.format(d))

print('\nWidth and precision combined:')
print('{:5.1f} {:5.1g}'.format(d, d))
print('{:5.2f} {:5.2g}'.format(d, d))
print('{:5.2f} {:5.2g}'.format(d, d))

print('\nZero padding:')
print('{:05.1}'.format(d))
print('{:05.2}'.format(d))
print('{:05.3}'.format(d))

'''RESULTS:
Precision:
1
1.1
1.10
1.10000000000000009

Width and precision combined:
  1.1     1
 1.10   1.1
 1.10   1.1

Zero padding:
00001
001.1
01.10
'''

#4 operators

import decimal

a = decimal.Decimal('5.1')
b = decimal.Decimal('3.14')
c = 4
d = 3.14

print('a =', repr(a))
print('b =', repr(b))
print('c =', repr(c))
print('d =', repr(d))
print()

print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print()

print('a + c =', a + c)
print('a - c =', a - c)
print('a * c =', a * c)
print('a / c =', a / c)
print()

#print('a + d =', end=' ')  # decimal not friendly for float
#try:
#    print(a + d)
#except TypeError as e:
#    print(e)

#5 special

import decimal

for value in ['Infinity', 'NaN', '0']:
    print(decimal.Decimal(value), decimal.Decimal('-' + value))
print()

# Operations with Infinity
print('Infinity + 1:', (decimal.Decimal('Infinity') + 1))
print('-Infinity + 1:', (decimal.Decimal('-Infinity') + 1))

# Show the results the equation with NaN
print(decimal.Decimal('NaN') == decimal.Decimal('Infinity'))
print(decimal.Decimal('NaN') != decimal.Decimal(1))

'''RESULTS:
Infinity -Infinity
NaN -NaN
0 -0

Infinity + 1: Infinity
-Infinity + 1: -Infinity
False
True
'''

#6 getcontext()

import decimal

context = decimal.getcontext()

print('Emax      =', context.Emax)
print('Emin      =', context.Emin)
print('capitals  =', context.capitals)
print('prec      =', context.prec)
print('rounding  =', context.rounding)
print('flags     =')
for f, v in context.flags.items():
    print(' {}: {}'.format(f, v))
print('traps     =')
for t, v in context.traps.items():
    print(' {}: {}'.format(t, v))

'''RESULTS:
Emax      = 999999
Emin      = -999999
capitals  = 1
prec      = 28
rounding  = ROUND_HALF_EVEN
flags     =
 <class 'decimal.InvalidOperation'>: False
 <class 'decimal.FloatOperation'>: True
 <class 'decimal.DivisionByZero'>: False
 <class 'decimal.Overflow'>: False
 <class 'decimal.Underflow'>: False
 <class 'decimal.Subnormal'>: False
 <class 'decimal.Inexact'>: True
 <class 'decimal.Rounded'>: True
 <class 'decimal.Clamped'>: False
traps     =
 <class 'decimal.InvalidOperation'>: True
 <class 'decimal.FloatOperation'>: False
 <class 'decimal.DivisionByZero'>: True
 <class 'decimal.Overflow'>: True
 <class 'decimal.Underflow'>: False
 <class 'decimal.Subnormal'>: False
 <class 'decimal.Inexact'>: False
 <class 'decimal.Rounded'>: False
 <class 'decimal.Clamped'>: False
'''

#7 precision

import decimal

d = decimal.Decimal('0.123456')

for i in range(1, 5):
    decimal.getcontext().prec = i
    print(i, ':', d, d * 1)

'''RESULTS:
1 : 0.123456 0.1
2 : 0.123456 0.12
3 : 0.123456 0.123
4 : 0.123456 0.1235
'''

#8 rounding

import decimal

context = decimal.getcontext()

ROUNDING_MODES = [
        'ROUND_CEILING',
        'ROUND_DOWN',
        'ROUND_FLOOR',
        'ROUND_HALF_DOWN',
        'ROUND_HALF_EVEN',
        'ROUND_HALF_UP',
        'ROUND_UP',
        'ROUND_05UP',
]

header_fmt = '{:10} ' + ' '.join(['{:^8}'] * 6)

print(header_fmt.format(
    ' ',
    '1/8 (1)', '-1/8 (1)',
    '1/8 (2)', '-1/8 (2)',
    '1/8 (3)', '-1/8 (3)',
))
for rounding_mode in ROUNDING_MODES:
    print('{0:10}'.format(rounding_mode.partition('_')[-1]),
            end=' ')
    for precision in [1, 2, 3]:
        context.prec = precision
        context.rounding = getattr(decimal, rounding_mode)
        value = decimal.Decimal(1) / decimal.Decimal(8)
        print('{0:^8}'.format(value), end=' ')

        value = decimal.Decimal(-1) / decimal.Decimal(8)
        print('{0:^8}'.format(value), end=' ')
    print()

'''RESULTS:
              1/8 (1)  -1/8 (1) 1/8 (2)  -1/8 (2) 1/8 (3)  -1/8 (3)
CEILING      0.2      -0.1     0.13    -0.12    0.125    -0.125
DOWN         0.1      -0.1     0.12    -0.12    0.125    -0.125
FLOOR        0.1      -0.2     0.12    -0.13    0.125    -0.125
HALF_DOWN    0.1      -0.1     0.12    -0.12    0.125    -0.125
HALF_EVEN    0.1      -0.1     0.12    -0.12    0.125    -0.125
HALF_UP      0.1      -0.1     0.13    -0.13    0.125    -0.125
UP           0.2      -0.2     0.13    -0.13    0.125    -0.125
05UP         0.1      -0.1     0.12    -0.12    0.125    -0.125
'''

#9 context manager

import decimal

with decimal.localcontext() as c:
    c.prec = 2
    print('Local precision:', c.prec)
    print('3.14 / 3 =', (decimal.Decimal('3.14') / 3))

print()
print('Default precision:', decimal.getcontext().prec)
print('3.14 / 3 =', (decimal.Decimal('3.14') / 3))

'''RESULTS:
Local precision: 2
3.14 / 3 = 1.1

Default precision: 3
3.14 / 3 = 1.04
'''

#10 instance context

