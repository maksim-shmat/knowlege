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

######6 Reverse tuple

myTuple = ('a', 'b', 'c')
reversed_tuple = reversed(myTuple)
result = tuple(reversed_tuple)
print(result)
print()

######7 List of tuples
### Append tuple to list of tuples

list_of_tuples = [(1, 'Saranya', 92), (2, 'Surya', 95), (3, 'Mania', 93)]
list_of_tuples.append((4, 'Reshmi', 94))
print(list_of_tuples)

### Update a tuple in list of tuples

list_of_tupless = [(1, 'Sui', 92), (2, "Zuzu", 95), (3, "Mana", 94)]
list_of_tupless[1] = (2, 'Recshmi', 99)
print(list_of_tupless)

### Remove a tuple from list of tuples

list_of_tuples1 = [(1, 'Sui', 92), (2, 'Quzu', 99), (53, 'Mumu', 88)]
del list_of_tuples1[2]
print(list_of_tuples1)
print()

######8 Sort list of tuples using list.sort()

list_students = [('Sara', 84), ('Sui', 92), ('Mark', 86), ('Ritha', 89)]
list_students.sort(key=lambda x: x[1])  # index 1 mean second element
print(list_students)

### and reverse
list_students = [('Sara', 84), ('Sui', 92), ('Mark', 86), ('Ritha', 89)]
list_students.sort(key=lambda x: x[1], reverse=True)
print(list_students)
print()

######9 Sort list of tuples using bubble sort algorithm

list_ = [('Sara', 84), ('Suita', 92), ('Mazurka', 86), ('Givi', 89)]
# sort by second element of tuple
ith = 1  # or 0 first element of tuple
list_length = len(list_)
for i in range(0, list_length):
    for j in range(0, list_length-i-1):
        if (list_[j][ith] > list_[j + 1][ith]):
                temp = list_[j]
                list_[j] = list_[j + 1]
                list_[j + 1] = temp

print(list_)
print()

######10 Convert tuple to list
# use list() constructor

tuple_1 = ('a', 'e', 'i', 'o', 'u')
list_1 = list(tuple_1)
print(list_1)
print(type(list_1))

### unpack tuple inside square brackets

tuple_1 = ('a', 'e', 'i', 'o', 'u')
list_1 = [*tuple_1,]
print(list_1)
print(type(list_1))
print()

######11 Convert tuple to string using join()

tuple11 = ('p', 'yt', 'ho', 'n')
str = ''.join(tuple11)
print(str)

### convert tuple to string using for loop

tuple01 = ('p', 'y', 'th', 'o', 'n')
str = ''
for item in tuple01:
    str = str + item
print(str)
print()

######12 Slice a tuple
# slice with specific start and end position

tuple_1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
start = 2
stop = 7
# step = 2
slice_object = slice(start, stop)  # slice(start, stop, step)
result = tuple_1[slice_object]
print(result)
print()

#1 traditional way

a, b = 1, 2
c = a
a = b
b = c
print(a, b)
(2, 1)

#1.1 other

a, b = 0, 1
a, b = b, a
print(a, b)
(1, 0)

#2 
