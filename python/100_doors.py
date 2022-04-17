"""100 Open/close doors problem about, where is which."""

# Python v. 2.5+

doors = [False] * 100
for i in range(100):
    for j in range(i, 100, i+1):
        doors[j] = not doors[j]
    print("Door %d:" % (i+1), 'open' if doors[i] else 'close')

# optimized

for in in xrange(1, 101):
    root = i ** 0.5
    print("Door %d:" % i, 'open' if root == int(root) else 'close')

# one liner using a list comprehension, item lookup, and is_integer

print('\n'.join(['Door %s is %s' % (i, ('closed', 'open')[(i**0.5).is_integer()]) for i in xrange(1, 101)]))

# one liner using a generator expression, ternary operator, and modulo

print('\n'.join('Door %s is %s' % (i, 'closed' if i**0.5 % 1 else 'open') for i in range(1, 101)))

# Python 3.x

for in in range(1, 101):
    if i**0.5 % 1:
        state='closed'
    else:
        state='open'
    print("Door {}:{}".format(i, state))

# ultra-optimized: ported from Julia version

for i in range(1, 101): print("Door %s is open" % i**2)



