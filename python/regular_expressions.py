"""Regular Expressions about."""

'''
\d - Some digit
\D - Everything BUT a digit
\s - White space
\S - Everything BUT a white space
\w - Some letter
\W - Everything BUT a letter
 . - Every character except for new lines
\b - White spaces around a word
\. - A dot

{x,y} - A number that has a length between x and y
+ - At least one
? - None or one
* - Everything
$ - At the end of a string
^ - At the beginning of a string
| - Either Or
[] - Value range
{x} - x times
{x,y} - x to y times

\n - New line
\t - Tab
\s - White Space

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

###### get the list of all numbers in a string

import re

str = 'We live at 9-162 Malibeu. My phone number is 666688888.'
# search using regex
x = re.findall('[0-9]+', str)
print(x)
print()

###### get the list of all continuous digits in a string

import re

str = 'We four guys, live at 2nd street of Malibeu. I had a cash of $248 \
        in my pocket. I got a ticket with serial number 88796451-52.'
# search using regex
x = re.findall('[0-9]+', str)
print(x)
print()

###### Find numbers of specific length in a string

import re

str = 'We four guys, live at 2nd street of Malibeu 521. I had a cash of $248\
        in my pocket. I got a ticket with werial number 88796451-52.'
# search using regex
x = re.findall('[0-9]+', str)
print('All Numbers\n', x)

# digits of length N
N=3

def filterNumber(n):
    if (len(n)==N):
        return True
    else:
        return False

# filter the list
finalx = list(filter(filterNumber, x))
print('Final List\n', finalx)
print()


#1 Find ages
import re

text = """
Mike is 20 years old and George is 29!
My grandma is even 104 years old!
"""
ages = re.findall(r'\d{1,3}', text)
print(ages)

# replace all ages
text = re.sub(r'\d{1,3}', "100", text)
print(text)

'''
#2 Apply regular expression for mails

import re

text = "test@mail.com"

result = re.fullmatch(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@{a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", text)
if result != None:
    print("VALID!")
else:
    print("INVALID!")

#3
