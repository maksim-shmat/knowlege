"""Program to check if the Given is in Ascenging Order or Not."""

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

list2 = [2, 3, 7, 5, 10, 17, 12, 4, 1, 13]
for i in list2:
    if i % 2 == 0:
        print(i)
        print()
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
'''
Expected output:
    [1, 2, 4, 6, 9, 3, 19, 7]
    '''
"""Interchange First and Last Element of a List."""

list5 = [1, 29, 51, 9, 17, 6, 7, 23]
list5[0], list5[-1] = list5[-1], list5[0]
print(list5)
print()
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
'''
Expected output:
    [2, 3, 5]
    '''

###### using for loop to iterate through a string

separated_letters = []
for letter in 'analytics':
    separated_letters.append(letter)
    print(separated_letters)

print()
###### using list comprehension to iterate through a String

separated_letters = [letter for letter in 'analytics']
print(separated_letters)
print()

###### using lambda functions inside list

letters = list(map(lambda y: y, 'analytics'))
print(letters)
print()

###### using if with list comprehensions

even_list = [i for i in range(10) if i % 2 == 0]
print(even_list)
print()

###### nested if with list comprehension

filtered_list = [ x for x in range(50) if x % 2 == 0 if x % 5 == 0]
print(filtered_list)
print()

###### if...else with list comprehension

list = ["even" if y % 2 == 0 else "odd" for y in range(5)]
print(list)
print()

###### finding transpose of matrix using nested loops

transposed_matrix = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed_matrix.append(transposed_row)
    print(transposed_matrix)
    print()

###### finding the elements in a list in which elements are ended with 
#      the letter 'b' and the length of that element is greater than 2

names = ['Ch', 'Dh', 'Eh', 'cb', 'Tb', 'Td', 'Chb', 'Tdb']
final_names = [name for name in names if name.lower().endswith('b')
        and len(name) > 2]
final_names
print(final_names)
print()

###### reverse each string in a tuple
# reverse each elements in a specified tuple

List = [string[::-1] for string in ('Hello', 'Analytics', 'Vidhya')]
# Display the list
print(List)

