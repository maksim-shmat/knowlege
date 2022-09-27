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
