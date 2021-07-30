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

######
