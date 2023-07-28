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
'''
#13

filename = 'jill.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
        print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(f"{pi_string[:52]}...")
print(len(pi_string))

#14 len of words in file and exceptp FileNotFoundError:

def count_words(filename):
    """Count words in file."""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")  # or pass
    else:
        # Count words in file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['jill.txt', 'jill.py']
for filename in filenames:
    count_words(filename)

#15 Reading ang writing in binary mode

with open('example.bin', 'wb') as fw:
    fw.write(b'This is binary data...')

with open('example.bin', 'rb') as f:
    print(f.read())  # prints: b'This is binary data...'


#16 Protecting agains overriding an existing file

with open('write_x.txt', 'x') as fw:
    fw.write('Writing line 1')  # this succeeds

with open('write_x.txt', 'x') as fw:
    fw.write('Writing line 2')  # Traceback... FileExistError

#17 Checking for file and directory existence

import os

filename = 'jill.txt'
path = os.path.dirname(os.path.abspath(filename))

print(os.path.isfile(filename))  # True
print(os.path.isdir(path))  # True
print(path)

#18 Manipulation file and directories

from collections import Counter
from string import ascii_letters

chars = ascii_letters + ' '

def sanitize(s, chars):
    return ''.join(c for c in s if c in chars)

def reverse(s):
    return s[::-1]

with open('jill.txt') as stream:
    lines = [line.rstrip() for line in stream]

with open('claire.txt', 'w') as stream:
    stream.write('\n'.join(reverse(line) for line in lines))

# now we can calculate some statistics
lines = [sanitize(line, chars) for line in lines]
whole = ' '.join(lines)
cnt = Counter(whole.lower().split())
print(cnt.most_common(3))

#19 Manipulation oriented to disc operations

import shutil
import os


BASE_PATH = 'ops_example'  # this will be out base path
os.mkdir(BASE_PATH)

path_b = os.path.join(BASE_PATH, 'A', 'B')
path_c = os.path.join(BASE_PATH, 'A', 'C')
path_d = os.path.join(BASE_PATH, 'A', 'D')

os.makedirs(path_b)
os.makedirs(path_c)

for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(os.path.join(path_b, filename), 'w') as stream:
        stream.write(f'Some content here in {filename}\n')

shutil.move(path_b, path_d)

shutil.move(
        os.path.join(path_d, 'ex1.txt'),
        os.path.join(path_d, 'ex1d.txt')
)

#20 Manipulating pathnames

import os

filename = 'fear.txt'
path  = os.path.abspath(filename)

print(path)
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.splitext(path))
print(os.path.split(path))

readme_path = os.path.join(
        os.path.dirname(path), '..', '..', 'README.rst')
print(readme_path)
print(os.path.normpath(readme_path))

#21 Temporary files and directories

import os
from tempfile import NamedTemporaryFile, TemporaryDirectory

with TemporaryDirectory(dir='.') as td:
    print('Temp directory:', td)
    with NamedTemporaryFile(dir=td) as t:
        name = t.name
        print(os.path.abspath(name))

#22
