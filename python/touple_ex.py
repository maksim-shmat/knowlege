"""Touple about."""

# change value

a, b = 1, 2
print(a, b)

a, b = b, a
print(a, b)

print()
###

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
        print(a, b, c)

print()
###### how indefined anenity of elements

seq = [1, 2, 3, 4]
*a, b, c = seq
print(a, b, c)
a, *b, c = seq
print(a, b, c)
a, b, c, *d = seq
print(a, b, c, d)
a, b, c, d, *e = seq
print(a, b, c, d, e)

print()

###### how lenght different

for (a, *b, c) in [(1, 2, 3), (4, 5, 6, 7)]:
    print(a, b, c)

print()

######
