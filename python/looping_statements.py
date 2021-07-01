"""Python For Loop Example."""


# Python For Loop with Range

for i in range(25, 29):
    print(i)

###### For Loop with List

mylist = ['python', 'programming', 'examples', 'programs']

for x in mylist:
    print(x)

###### For Loop with Tuple

mytuple = ('python', 'programming', 'examples', 'programs')

for x in mytuple:
    print(x)

###### For Loop with Dictionary

mydictionary = {'name':'python', 'category':'programming', 'topic':'examples'}

for x in mydictionary:
    print(x, ':', mydictionary[x])

###### For Loop with Set

myset = {'python', 'programming', 'examples'}

for x in myset:
    print(x)

###### For Loop with String

mystring = 'pythonexamples'

for x in mystring:
    print(x)

###### For Loop - break

for x in range(2, 10):
    if(x==7):
        break
    print(x)

###### For Loop - continue

for x in range(2, 10):
    if(x==7):
        continue
    print(x)

###### For Loop with Else Block

for x in range(2, 6):
    print(x)
else:
    print('Out of for loop')

###### Nested For Loop

for x in range(5):
    for y in range(6):
        print(x, end=' ')
    print()

######
