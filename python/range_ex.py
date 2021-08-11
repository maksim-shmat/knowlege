"""range() about."""

# range() with only stop

for r in range(5):
    print(r)
print()

###### range() with start and stop

for r in range(4, 9):
    print(r)
print()

###### range() with positive step

# r[i] = start + (step * i)
# r[0] = 2     + (2    * 0)
# r[1] = 2     + (2    * 1)

for r in range(2, 8, 2):
    print(r)
print()

###### range() with negative step

for r in range(8, 2, -2):
    print(r)
print()

###### access elements of range using index

r = range(2, 100, 8)
print(r[5]) # r[5] = 2 + [8 * 5]
print(r[7]) # r[7] = 2 + [8 * 7]
print()

###### initialize python list with range

x = list(range(4, 9))
print(x)
print()

######
