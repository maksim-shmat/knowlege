"""for about."""

'''
for word in ['cpitalize', 'these' 'words']:
    print(word.upper())

# results
CAPITALIZE
THESE
WORDS
#2
for i in range(0, 5):
    print(i)

# results:
0
1
2
3
4

#3
surnames = ['Rivalier', 'Shamire', 'Autlemer']
for position in range(len(surnames)):
    print(position, surnames[position])

# results:
0 Rivalier
1 Shamire
2 Autlemer

#3.1 More Pythonic

for surname in surnames:
    print(surname)

#3.2 With enumerate

for position, surname in enumerate(surnames):
    print(position, surname)

#4 iterating multiple sequences

people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person, age)

# results:
Conrad 29
Deepak 30
Heinrich 34
Tom 36
'''
#4.1 with enumerate

people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
for position, person in enumerate(people):
    age = ages[position]
    print(person, age)

#4.2

people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages [29, 30, 34, 36]
nationalities = ['Poland', 'India', 'South Africa', 'England']
for person, age, nationalitiy in zip(people, ages, nationalities):
    print(person, age, nationality)

#4.3

people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages [29, 30, 34, 36]
nationalities = ['Poland', 'India', 'South Africa', 'England']
for data in zip(people, ages, nationalities):
    person, age, nationality = data
    print(person, age, nationality)

#5 infinite iterators

from itertools import count

for n in count(5, 3):
    if n > 20:
        break
    print(n, end=', ')

# Results:
# 5, 8, 11, 14, 17, 20,

#6.1 for with exception alternative

n = 100
found = False
for a in range(n):
    if found: break
    for b in range(n):
        if found: break
        for c in range(n):
            if 42 * a + 17 * b + c == 5096:
                found = True
                print(a, b, c) # 79 99 95

#6.2

class ExitLoopException(Exception):
    pass

try:
    n = 100
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if 42 * a + 17 * b + c == 5096:
                    raise ExitLoopException(a, b, c)
except ExitLoopException as ele:
    print(ele) # (79, 99, 95)

#7


