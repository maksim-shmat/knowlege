"""pow() about <Степень>."""

# find base to the power

base = 5
exp = 3
result = pow(base, exp)
print(f'{base} to the power of {exp} is {result}.')
print()

###### find base to the power of zero

base = 5
exp = 0
result = pow(base, exp)
print(f'{base} to the power of {exp} is {result}.')
print()

###### negative power

base = 5
exp = -1
result = pow(base, exp)
print(f'{base} to the power of {exp} is {result}.')
print()

###### pow() with mod parameter

base = 5
exp = 3
mod = 10
result = pow(base, exp, mod)
print(f'{base} to the power of {exp}, % {mod} is {result}.')
print()

######
