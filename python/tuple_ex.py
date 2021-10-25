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

### create tuple from string

str = 'Python'
tuple_from_string = tuple(str)
print(tuple_from_string)

### create tuple from list

my_list = ['a', 'e', 'i', 'o', 'u']
tuple_from_list = tuple(my_list)
print(tuple_from_list)

### create tuple from range

my_range = range(5)
tuple_from_range = tuple(my_range)
print(tuple_from_range)

### create tuple from set

my_set = {'a', 'e', 'i', 'o', 'u'}
tuple_from_set = tuple(my_set)
print(tuple_from_set)
print()

######2 Access tuple items using index

vowels = ('a', 'e', 'i', 'o', 'u')
item = vowels[1]
print(item)
print('above index results')

######3 Iterate over items of Python Tuple
# for loop

tuple1 = (14, 52, 17, 24)
for item in tuple1:
    print(item)

# sum with for loop
tuple11 = (5, 3, 2, 8, 4, 4, 6, 2)
sum = 0

for num in tuple11:
    sum += num

print(sum)
print('above one sum')

# while loop

tuple1 = (14, 52, 17, 24)

index = 0
while index < len(tuple1):
    print(tuple1[index])
    index = index + 1
print('above for and while loop results')

######4 Change tuple values
# 1. Convert the tuple to a list
# 2. Update the required item of the list
# 3. Covert the list back to tuple and assign it to the original tuple

tuple12 = (5, 3, 2, 8, 4, 4, 6, 2)
list1 = list(tuple12)
list1[2] = 63
tuple12 = tuple(list1)
print(tuple12)

### Remove item from the tuple

tuple13 = (5, 3, 2, 8, 4, 7, 23)
list2 = list(tuple13)
list2.remove(2)
tuple13 = tuple(list2)
print(tuple13)
print()

######5 if..not to check if item is present in tuple

tuple14 = (5, 3, 2, 8, 457)
if 8 in tuple14:
    print('8 is in the tuple', tuple14)
else:
    print('8 is not in the tuple', tuple14)

### Use for loop to check if item is present in tuple

tuple15 = (5, 3, 2, 88, 946)
check_item = 88
is_item_present = False

for item in tuple15:
    if item==check_item:
        is_item_present = True
        break
print('Is', check_item, 'Present? ', is_item_present)
print()

######6
