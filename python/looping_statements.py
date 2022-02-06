"""Python For Loop Example."""


# Python For Loop with Range

for i in range(25, 29):
    print(i)
    print()

###### For Loop with List

mylist = ['python', 'programming', 'examples', 'programs']

for x in mylist:
    print(x)
    print()

###### For Loop with Tuple

mytuple = ('python', 'programming', 'examples', 'programs')

for x in mytuple:
    print(x)
    print()

###### For Loop with Dictionary

mydictionary = {'name':'python', 'category':'programming', 'topic':'examples'}

for x in mydictionary:
    print(x, ':', mydictionary[x])
    print()

### loop through dictionary

language_creators = {
        "Python": "Guido van Rossum",
        "C": "Dennis Ritchie",
        "Java": "James Gosling",
}
for key, value in language_creators.items():
    print("Language: {}; Creator: {}".format(key, value))
    print()

###### For Loop with Set

myset = {'python', 'programming', 'examples'}

for x in myset:
    print(x)
    print()

###### For Loop with String

mystring = 'pythonexamples'

for x in mystring:
    print(x)
    print()

###### For Loop - break

for x in range(2, 10):
    if(x==7):
        break
    print(x)
    print()

###### For Loop - continue

for x in range(2, 10):
    if(x==7):
        continue
    print(x)
    print()

###### For Loop with Else Block

for x in range(2, 6):
    print(x)
    print()
else:
    print('Out of for loop')
    print()

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
            print()
            break # but how outher from two cicles?

###### bad with func and return

def func():
    s = "teste"
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                print(i, j)
                print()
                return
func()

###### bad with exception

try:
    s = "teste"
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                print(i, j)
                print()
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
            print()
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
        print()
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
        print()
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
        print()
        break

##### simple while loops

level = 0
while(level < 10):
    level += 1

#1 Parallel iteration

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')
# anne is 12 years old
# beth is 45 years old

# or
list(zip(names, ages))
# [('anne': 12), ('beth': 45)....]
# then unpack tuples
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')
# anne is 12 years old
# beth is 45 years old

#2 While True idiom

while True:
    word = input('Please enter a word:')
    if not word: break
    # do something with the word:
    print('The word was', word)


