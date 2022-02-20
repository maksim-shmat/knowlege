"""Regular expression about."""

#1

import re

pattern, string = "A.C.", "xxABCDxx"
matchobj = re.search(pattern, string)
if matchobj:
    print(matchobj.start())

pattobj = re.compile("A.*C.*")
matchobj = pattobj.search("xxABCDxx")
if matchobj:
    print(matchobj.start())
print(re.search(" *A.C[DE][D-F][^G-ZE]G\t+ ?", "...ABCDEFG\t..").start())
print(re.search("(A|X)(B|Y)(C|Z)D", "..AYCD..").start())
print(re.search("(?:A|X)(?:B|Y)(?:C|Z)D", "..AYCD..").start())
print(re.search("A|XB|YC|ZD", "...AYCD..").start())
print(re.search("(A|XB|YC|ZD)YCD", "..AYCD..").start())
print(re.search(r"\bABCD", "..ABCD ").start())
print(re.search(r"ABCD\b", "..ABCD ").start())

#2

import re

patt = re.compile("A(.)B(.)C(.)")
mobj = patt.match("AOB1C2")
print(mobj.group(1), mobj.group(2), mobj.group(3))

patt = re.compile("A(.*)B(.*)C(.*)")
mobj = patt.match("AOOOB111C222")
print(mobj.groups())
print(re.search("(A|X)(B|Y)(C|Z)D", "..AYCD..").groups())
print(re.search("(?P<a>A|X)(?P<b>B|Y)(?P<c>C|Z)D", "..AYCD..").groupdict())

patt = re.compile(r"[\t ]*#\s*define\s*([a-z0-9_]*)\s*(.*)")
mobj = patt.search(" # define spam 1 + 2 + 3")
print(mobj.groups())

#3

import re

print(re.sub('[ABC]', '*', 'XAXAXBXBXCXC'))
print(re.sub('[ABC]_', '*', 'XA-XA_XB-XB_XC-XC_'))
print(re.sub('(.) spam', 'spam\\1', 'x spam, y spam'))

def mapper(matchobj):
    return 'spam' + matchobj.group(1)

print(re.sub('(.) spam', mapper, 'x spam, y spam'))

#4 """ Analise XML with re """

import re, pprint

text    = open('books.xml').read()
pattern = '(?s)isbn="(.*?)".*?<title>(.*?)</title>'
found   = re.findall(pattern, text)
mapping = {isbn: title for (isbn, title) in found}
pprint.pprint(mapping)

#5
