# "(name, date),\n" to "name, date"
x.rstrip("\n)(,")

# del quotation mark
x = ['"abc"', 'def', '"ghi"','"klm"', 'nop']
for item in x:
    print(item.strip('"'))
"""
abc
def
ghi
klm
nop

"""
