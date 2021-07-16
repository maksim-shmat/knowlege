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
"""How make double break from two cicle or more."""

# Check all pairs of char in a string and stop how find two equels chars.

# bad
s = "something string"
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            print(i, j)
            break # but how outher from two cicles?

###### bad with func and return

def func():
    s = "teste"
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                print(i, j)
                return
func()

###### bad with exception

try:
    s = "teste"
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                print(i, j)
                raise Exception()
except:
    print("the end")

###### bad with bool

exitFlag = False
s = "teste"
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            print(i, j)
            exitFlag = True
            break
    if(exitFlag):
        break

###### bad while 

s = "teste"
i = 0
j = 1
while i <len(s):
    if s[i] == s[j]:
        print(i, j)
        break
    j = j + 1
    i = i + j // len(s)
    j = j % len(s)

###### good

def unique_pairs(n):
    for i in range(n):
        for j in range(i+1, n):
            yield i, j

s = "a string to example"
for i, j in unique_pairs(len(s)):
    if s[i] == s[j]:
        print(i, j)
        break

###### good
# itertools.combinations(s, 2)

#######==============
item_list = [3, 'string1', 23, 14, 0, 'string2', 49, 64, 80]
for x in item_list:
    if not isinstance(x, int):
        continue
    if not x % 7:
        print("Found an integer divisible by seven: %d" %x)
        break

######
