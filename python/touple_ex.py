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

######1 Create tuple

tuple1 = ('a', 'e', 'i', 'o', 'u')
tuple2 = tuple(['a', 'e', 'i', 'o', 'u'])

######2 Access tuple items using index

tuple1 = (14, 52, 17, 24)
print(tuple1[1])
print(tuple1[3])
print('above index results')

######3 Iterate over items of Python Tuple
# for loop

tuple1 = (14, 52, 17, 24)
for item in tuple1:
    print(item)

# while loop

tuple1 = (14, 52, 17, 24)

index = 0
while index < len(tuple1):
    print(tuple1[index])
    index = index + 1
print('above for and while loop results')

######4
