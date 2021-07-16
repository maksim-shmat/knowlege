"""Dinamical math without definition."""

# eval() is not safe

a = 3

b = eval('a + 2')
print('b =', b)

exec('c = a ** 2')
print('c is', c)
