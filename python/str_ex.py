"""str() about."""

# str() with list object as argument

myList = [25, 'hello world', 36.25]
resultString = str(myList)
print(f'Resulting string is - "{resultString}"')
print()

###### str() with no object as argument

resultString = str()
print(f'Resulting string is - "{resultString}"')
print()

###### str() with encoding

bytes = b'\x65\x66\x67\x68\x69'
resultString = str(bytes, encoding='utf-8')
print(f'Resulting string is - "{resultString}"')
print()

######
