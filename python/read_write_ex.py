"""Read/write files about."""

'''
#1 Read 4 leters

with open('jill.txt', 'r') as f:  # not need close()
    print(f.read(4))
    print(f.read())  # next 4 leters

# Count words

import sys

text = sys.stdin.read()  # it for interpreter. Use input. 
words = text.split()
wordcount = len(words)
print('Wordcount:', wordcount)

#2 Random? access (bookmarks?)

f1 = open('jill.txt', 'w')
print(f1.write('01234567890123456789'))  # 20
print(f1.seek(5))  # 5 <----------
print(f1.write('Hello, World!'))  #13
f1.close()

f2 = open('jill.txt')
print(f2.read())  # '01234Hello, World!89' 
f2.close()

f3 = open(r'jill.txt')
try:
    print(f3.read(3))  # '012'
    print(f3.read(2))  # '34'
    print(f3.tell())  # 5 <----------
finally:
    f3.close()
print('next')

#3 

f4 = open(r'jill.txt')
for i in range(3):
    print(str(i) + ':' + f4.readline(), end='')
f4.close()
# 1...
# 2...
# 3...

#4

import pprint

pprint.pprint(open(r'jill.txt').readlines())

f5 = open(r'jill.txt','w')
f5.write('this\nis no\nhaiku')
f5.close()

f5 = open(r'jill.txt')
lines = f5.readlines()
f5.close()
lines[1] = "isn't a\n"

f5 = open(r'jill.txt', 'w')
f5.writelines(lines)
f5.close()

#5 read one character

def process(string):
    print('Processing:', string)

with open(r'jill.txt') as f6:
    char = f6.read(1)
    while char:
        process(char)
        char = f6.read(1)
# Processing: t
# Processing: h
# Processing: i
# Processing: s ...

#6 read one line at a time, for big file

def process1(string):
    print('Processing:', string)

with open(r'jill.txt') as f7:
    while True:
        line = f7.readline()
        if not line: break
        process1(line)

# Processing: this
# Processing: isn't...

#7 reading everything char, for isn't too large files

def process2(string):
    print('Processing: ', string)

with open(r'jill.txt') as f8:
    for char in f8.read():
        process2(char)

#8 rading everithing

def process3(string):
    print('Processing: ', string)

with open(r'jill.txt') as f9:
    for line in f9.readlines():
        process3(line)

#9 Lazy line iteration with fileinput

import fileinput

def process4(string):
    print('Processing: ', string)
    
for line in fileinput.input(r'jill.txt'):
    process4(line)
'''
#10 Iterating over a file

def process5(string):
    print('Processing: ', string)

with open(r'jill.txt') as f10:
    for line in f10:
        process5(line)

#11
