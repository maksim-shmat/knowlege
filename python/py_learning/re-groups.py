import re

patt = re.compile("A(.)B(.)C(.)")
mobj = patt.match("AOB1C2")
print(mobj.group(1), mobj.group(2), mobj.group(3))

patt = re.compile("A(.*)B(.*)C(.*)")
mobj = patt.match("AOOOB111C222")
print(mobj.groups())
print(re.search("A|X)(B|Y)(C|Z)D", "..AYCD..").groups())
print(re.search("?P<a>A|X)(?P<b>B|Y)(?P<c>C|Z)D", "..AYCD..").groupdict())

patt = re.compile(r"[\t ]*#\s*define\s*([a-z0-9_]*)\s*(.*)")
mobj = patt.search(" # define spam 1 + 2 + 3")
print(mobj.groups())
