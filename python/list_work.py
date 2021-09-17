"""Program to check if the Given is in Ascenging Order or Not."""

######1

list1 = [1, 2, 3, 5, 4, 8, 7, 9]
temp_list = list1[:]
list1.sort()
if temp_list == list1:
    print("Given List is in Ascending Order")
    print()
else:
    print("Given List is not in Ascending Order")
    print()
"""
Expected Output:
Given List is not in Ascending Order
"""
"""Program to Find Even Numbers From a List."""

######2

list2 = [2, 3, 7, 5, 10, 17, 12, 4, 1, 13]
for i in list2:
    if i % 2 == 0:
        print(i)
        print()

######3

'''
Expected Output:
    2
    10
    12
    4
    '''
"""Program to merge two lists."""

list3 = [1, 2, 4, 6]
list4 = [9, 3, 19, 7]
list3.extend(list4)

print(list3)
print()

######4

'''
Expected output:
    [1, 2, 4, 6, 9, 3, 19, 7]
    '''
"""Interchange First and Last Element of a List."""

list5 = [1, 29, 51, 9, 17, 6, 7, 23]
list5[0], list5[-1] = list5[-1], list5[0]
print(list5)
print()

######5

'''
Expected Output:
    [23, 29, 51, 9, 17, 6, 7, 1]
    '''
"""Program to subtract a list from another list."""

a = [1, 2, 3, 5]
b = [1, 2]
l1 = []
for i in a:
    if i not in b:
        l1.append(i)
print(l1)
print()

######6

'''
Expected output:
    [3, 5]
    '''
"""Program to get data items from a list appearing odd number of times."""

x = [1, 2, 3, 4, 5, 1, 3, 3, 4]
l1 = []
for i in x:
    if x.count(i) % 2 != 0:
        if i not in l1:
            l1.append(i)
print(l1)
print()

######7

'''
Expected output:
    [2, 3, 5]
    '''

######7 using for loop to iterate through a string

separated_letters = []
for letter in 'analytics':
    separated_letters.append(letter)
    print(separated_letters)

print()

######8 using list comprehension to iterate through a String

separated_letters = [letter for letter in 'analytics']
print(separated_letters)
print()

######9 using lambda functions inside list

letters = list(map(lambda y: y, 'analytics'))
print(letters)
print()

######10 using if with list comprehensions

even_list = [i for i in range(10) if i % 2 == 0]
print(even_list)
print()

######11 nested if with list comprehension

filtered_list = [ x for x in range(50) if x % 2 == 0 if x % 5 == 0]
print(filtered_list)
print()

######12 if...else with list comprehension

listus = ["even" if y % 2 == 0 else "odd" for y in range(5)]
print(listus)
print()

######13 finding transpose of matrix using nested loops

transposed_matrix = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed_matrix.append(transposed_row)
    print(transposed_matrix)
    print()

######14 finding the elements in a list in which elements are ended with 
#      the letter 'b' and the length of that element is greater than 2

names = ['Ch', 'Dh', 'Eh', 'cb', 'Tb', 'Td', 'Chb', 'Tdb']
final_names = [name for name in names if name.lower().endswith('b')
        and len(name) > 2]
final_names
print(final_names)
print()

######15 reverse each string in a tuple
# reverse each elements in a specified tuple

List = [string[::-1] for string in ('Hello', 'Analytics', 'Vidhya')]
# Display the list
print(List)

######16 get lists of numbers and sum it

def pairwise_sum(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result

######17
# Имеется список, каждый элемент которого также является списком:
# [[1, 2, 3], [2, 1, 3], [4, 0, 1]]. Надо сортирнуть по второму элементу.
the_list = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
the_list.sort(key=lambda x: x[1])
print(the_list)
print()

######18

"""Lists about."""

# Имеется список х. Нужно безопасно удалить элемент в том и только том
# случае, если значение присутствует в списке.  
#if element in x:
#    x.remove(element)

# если более чем в одном экземпляре
#if x.count(element) > 1:
#    x.remove(element)
# Этот код удаляет только первое вхождение

###### concat lists without cicle

L = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
print(sum(L, []))

### concat lists with itertools

import itertools

L = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
print(list(itertools.chain.from_iterable(L)))
print()

######19 transposed 

original  = [('a', 'b'), ('c', 'd'), ('e', 'f')]
transposed = zip(*original)
print(list(transposed))

print()

######20 remove double in list

items = [2, 2, 3, 3, 1]
print(list(set(items)))
print()

######21 for one by one

irems = [2, 2, 3, 3, 1]
from collections import OrderedDict
print(list(OrderedDict.fromkeys(items).keys()))
print()

######22 find max often frequent element of list

a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print(max(set(a), key=a.count))
print()

### some max often values

from collections import Counter

a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
cnt = Counter(a)
print(cnt.most_common(3))
print()

######23 length of list naive method without len()

ListName = ["Hello", "Edureka", 1, 2, 3]
print("The list is: "+str(ListName))
counter = 0
for i in ListName:
    counter = counter + 1
    print("Length of list using naive method is : " + str(counter))
print()

######24 length of list with list updates

cars = ['Ford', 'Volvo', 'BMW', 'Tesla']
cars.append('Honda')
cars.append('Tata')
length = len(cars)
print('Length of the list is :', length)
print()

######25
