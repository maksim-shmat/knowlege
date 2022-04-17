"""About work with files."""
'''
######1 Read text file

fileObject = open('jill.py', 'r')
data = fileObject.read()
print(data)
fileObject.close()

######2 Read only some characters in the file

f = open('jill.py', 'r')
data = f.read(8)  # 20 characters
print(data)
f.close()

######3 Read file in text mode

f = open('jill.py', 'rt')
data = f.read()
print(data)
f.close()

######4 Read file line by line

f = open("jill.py", 'r')

while(True):
    line = f.readline()
    if not line:
        break
    print(line.strip())
f.close

######5 Crate a new file using open()

#f = open('jill.txt', 'x')
#f.close
#print('if file is exist, you get Traceback')

######6 Remove file

#import os
#os.remove('jill.txt')
#print('The file is removed.')

######7 Create a directory

import os

dirPath = 'jack'
if not os.path.isdir(dirPath):
    print('The directory is not presented. Creating a new one..')
    os.mkdir(dirPath)
else:
    print('The directory is present.')
print()

######8 Find unique words in text file

text_file = open('jill.py', 'r')
text = text_file.read()
text_file.close()

# cleaning
text = text.lower()
words = text.split()
words = [word.strip('.,!()[]') for word in words]
words = [word.replace("'s", '') for word in words]

# finding unique
unique = []
for word in words:
    if word not in unique:
        unique.append(word)

# sort
unique.sort()

# print
print(unique)
text_file.close()

######9 Append text to file

fin = open("jill.txt", 'a')  # or 'at'
fin.write('\nI love you Jill!')
fin.close

######10 Replace string in file,  # full rewrite file?

#fin = open("jill.py", "rt")
#fout = open("jill.txt", "wt")
#for line in fin:
#    fout.write(line.replace('yebat', 'wow'))
#fin.close()
#fout.close()

### Replace string in the same file

fin = open("jill.txt", "rt")
data = fin.read()
data = data.replace('wow', 'yebat')
fin.close()
fin = open("jill.txt", "wt")
fin.write(data)
fin.close()

######11 Count how many times a word occured in given text file

file1 = open('jill.txt')
data = file.read()
occurrences = data.count("love")
print('Number of occurences of the word : ', occurrences)
file1.close()
'''
#12 Finally and slow load

import time

try:
    f = open('jill.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('!! You aborted read file.')  # for Ctrl-C interruption
finally:
    f.close()
    print('(Cleance: Close file)')

#13
