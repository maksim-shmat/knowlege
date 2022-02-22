"""Read/write files about."""

#1 Read 4 leters

f = open('jill.txt', 'r')
f.read(4)
f.read()  # next 4 leters

# Count words

import sys

text = sys.stdin.read()  # it for interpreter. Use input. 
words = text.split()
wordcount = len(words)
print('Wordcount:', wordcount)
f.close()

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
print(f3.read(3))  # '012'
print(f3.read(2))  # '34'
print(f3.tell())  # 5 <----------
f3.close()

#3
