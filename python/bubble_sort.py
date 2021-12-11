""" Program for bubble sort."""

a = []
number = int(input('Enter the total number of elements: '))
for i in range(number):
    value = int(input('enter the %d Element of list 1: '%i))
    a.append(value)

for i in range(number-1):
    for j in range(number-i-1):
        if(a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j + 1]
            a[j+1] = temp

print('sorted list in ascending order: ', a)

#### second variant

a = []
number = int(input('enter the total number of elements: '))
for i in range(number):
    value = int(input("enter the %d element of list1: "%i))
    a.append(value)

i = 0
while(i< number-1):
    j = 0
    while(j < number -i -1):
        if (a[j] > a[j + 1]):
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
        j = j + 1
    i = i + 1

print('sorted list in ascending order: ', a)

###### third variant

def bubblesort(a, number):
    for i in range(number-1):
        for j in range(number-i-1):
            if(a[j] > a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

a = []
number = int(input('enter the total number of elements: '))
for i in range(number):
    value = int(input('enter the %d Element of List1: '%i))
    a.append(value)

bubblesort(a, number)
print("sorted list: ", a)

######
