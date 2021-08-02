"""Regular Expressions about."""

# re.findall() substring in string

import re

pattern = 'abc'
string = 'abcdefabcab'
result = re.findall(pattern, string)
print(result)
print()

###### re.findall() pattern in string

import re

patern = '[a-z]+'
string = 'abc---cab-efg_web'
result = re.findall(pattern, string)
print(result)
print()

###### re.findall() non-overlapping occurrences

import re

pattern = 'aba'
string = 'ababaiiaba'
result = re.findall(pattern, string)
print(result)
print()

###### re.findall() - falgs

import re

pattern = '[a-z]+'
string = 'aBC---CAB-eFg_web'
flags = re.IGNORECASE
result = re.findall(pattern, string, flags)
print(result)
print()

# ======================
# re.search() return the first match for a pattern in a string

import re

pattern = '[a-z]+'
string = '------2344-Hello--World!'
result = re.search(pattern, string)
print(result)
print(result.group())
print()

###### re.search() pattern not in string

import re

pattern = '[a-z]+'
string = '-----2344-HELLO--WORLD!'
result = re.search(pattern, string)
print(result)
print()

# ===================
# re.split()

import re

pattern = '-+'
string = '2344------------HELLO--WORLD!'
result = re.split(pattern, string)
print(result)
print()

###### re.split() split string by space

import re

pattern = '\s+'
string = 'Today   is a    present'
result = re.split(pattern, string)
print(result)
print()

###### re.split() no matches

import re

pattern = '\s+'
string = 'HelloWorld'
result = re.split(pattern, string)
print(result)
print()

###### re.split() maximum numbers of split

import re

pattern = '\s+'
string = 'Today is a present.'
result = re.split(pattern, string, maxsplit=2)
print(result)
print()

# ====================
# re.sub() replace one or many matches with a string in the given text
### re.sub() replace pattern matchings with replacement string

import re

pattern = '[0-9]+'
string = 'Account Number - 12345, Amount - 586.32'
repl = 'NN'

print('Original string')
print(string)

result = re.sub(pattern, repl, string)

print('After replacement')
print(result)
print()

###### re.sub() - limit maximum number of replacement

import re

pattern = '[0-9]+'
string = 'Account Number - 12345, Amount - 586.32'
repl = 'NN'

print('Original string')
print(string)

result = re.sub(pattern, repl, string, count=2)

print('After replacement')
print(result)
print()

###### re.sub() - optonal flags

import re

pattern = '[a-z]+'
string = 'Account Number - 12345, Amount - 586.32'
repl = 'AA'

print('Original string')
print(string)

result = re.sub(pattern, repl, string, flags=re.IGNORECASE)

print('After replacement')
print(result)
print()

###### Check if string starts with a word

import re

str = 'Python is a programming language.'
# search using regex
x = re.search('^Python', str)

if (x!=None):
    print('The line starts with \'Python\'.')
else:
    print('The line does not start with \'Python\'.')

print()

###### Check if string ends with a word

import re

str = 'Python is a programming language'
# search using regex
x = re.search('language$', str)

if (x!=None):
    print('The line ends with \'language\'.')
else:
    print('The line does not end with \'language\'.')
print()

######


