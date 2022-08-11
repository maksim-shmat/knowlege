"""Regular Expressions about."""

# : - means regular expressions for vim
'''
.  - any symbol (p.p = pip, pep etc)
*  - bugs* = bugss, bug, bugs, bugsss etc
^  - ^Part = Part at the begining a string, else ^ is carret
$  - here:$ = here: at the end of string, else $ is dollar
\  - next simbol is casual, \. - merely dot, \\ - is backslash
[ ] - [AB] = A or B, p[aeiou]t = pat, pet, pit, pot, put
/[Tt]he = The or the

[^0-9] = that carret means - NOT, anybody but not number
[[:alpha:]!] = a, l, p, h, or !
[[.ch.]] = ch only, but not c and h
[[=e=]] = e, franch e with`, and other e deviation

[:alnum:] - char and num
[:alpha:] - Alphabetical symb
[:blank:] - space and tab
[:cntrl:] - Control symb
[:digit:] - num only
[:graph:] - all visual symb, without spaces or tabs
[:lower:] - lowercase
[:print:] - printable symb, with spaces etc
[:punct:] - punctuation symb
[:space:] - space symb
[:upper:] - upercase
[:xdigit:] - sixteenth num

\( \) - save to the buffer, \(That\) or \(this\) = That to buffer1, this to b2
:s/\(That\) or \(this\)/\2 or \1/  # changing to this or That (result: this or That)
:s/\(That\) or \(this\)/\u\2 or \l\1/  # changing places and change low/up cases (result: This or that)

:s/\(abcd/)\1/alphabet-soup  # changeing abcd to alphabet-soup

\< - start of word, \<ac = action
\> - end of word, ac\> = maninac

& - same name, :%s/Cuchinski/&, Zax/ = :%s/Cuchinski/Cuchinski;, Zax/
:1, 10s/.*/(&)/  - make ->(every str into brakets)<- from 1-10 str

\u - Upercase, :%s/yes, doctor/\uyes, \udoctor (result: Yes, Doctor)
\l - Lower Case 

\U, \L - UPPER/LOWER CASES 
:%s/Fortran/\UFortran/  (result: FORTRAN)
:%S/Fotran/\U&/  (same)

-----------------------
# Case1: change child to children, with the same punctuation
# In the text is: child , child, child,, child., etc
# And we need is: childred , children, children,, children., etc
:%s/child\([ ,.;:!?]\)/children\1/g  # \( \)-save to buffer1 punctuation
:%s/\<child\>/children/g  # That is for not change words as Fairchild
-----------------------

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
+ - ho(use|me)+ = house, home, but without ho
? - None or one, free?d = fred an freed
* - Everything, ho(use|me)* = ho, house, home
$ - At the end of a string
^ - At the beginning of a string
| - A Or B
[] - Value range
{x} - x times, (home|house){2} = homehome, homehouse, househome, househouse, nothing more.
{n,} - min n and more repeats
{x,y} - repeat from x to y
* = {0,}
+ = {1,}
* = {0,1}

(...) - ho(use|me) = house|home, (house|home) = home, homehouse, househomhousehome etc.

\n - New line
\t - Tab
\s - White Space

#0.1 Function/Description of the re module

compile(pattern[,flags])  # Creates a pattern object from a string with a re

search(pattern, string[,flags])  # Matches pattern at the begining of string

split(pattern,string[,maxsplit=0])  # Splits a string by occurences of pattern in string

findall(pattern, string)  # Returna a list of all occurences of pattern in string

sub(pat, repl, string[,count=0])  # Substitute occurences of pat in string with repl

escape(string)  # Escapes all special regular expression characters in string

#0.2 re match object methods

group([group1, ...])  # Retrives the occurrences of the given subpatterns(groups)

start([group])  # Returns the starting position of the occurrence of a given group

end([group])  # Returns the ending position (an exclusive limit, as in slices) of the occurrence of a given group.

span([group])  # Returns both the beginning and ending position of a group

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

#3 re.split()

some_text = 'alpha, beta,,,,gamma delta'

print(re.split('[,     ]+', some_text))  # ['alpha', 'beta', 'gamma', 'delta']
print(re.split('[,     ]+',some_text, maxsplit=2))  # ['alpha', 'beta', 'gamma delta']

#4 re.findall()

pat = '[a-zA-Z]+'
text = '"Hm... Err -- are you sure?" he said, somethting insecure.'
print(re.findall(pat, text))  # ['Hm', 'Err', 'are', 'you', 'sure', 'he', 'said', 'something', 'insecure']

pat = r'[.?\-",]+'
print(re.findall(pat, text))  # ['", '...', '--' '?"', ',','.']

#5 re.sub()

pat = '{name}'
text = 'Dear {name}...'
print(re.sub(pat, 'Mr.Gibmly', text))  # 'Dear Mr.Gibmly...'

#6 re.escape()

print(re.escape('www.python.org'))  # 'www\.python\.org'

#7 re.match()

m = re.match(r'www\.(.*)\..{3}', 'www.python.org')

print(m.group(1))  # 'python'
print(m.start(1)) # 4
print(m.end(1))  # 10
print(m.span(1))  # (4, 10)

#8 
emphasis_pattern = r'\*([^\*]+)\*'

print(re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!'))  # 'Hello, <em>world</em>!'

#9 Greedy pattern

emphasis_pattern1 = r'\*(.+)\*'
print(re.sub(emphasis_pattern1, r'<em>\1</em>', '*This*is*it*!'))  # '<em>This*is*it</em>!'

#10 Nongreedy pattern

emphasis_pattern2 = r'\*\*(.+?)\*\*'
print(re.sub(emphasis_pattern2, r'<em>\1</em>', '**This**is**it**!'))  # '<em>This</em>is<em>it</em>!'

