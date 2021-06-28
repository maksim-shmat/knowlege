"""For example elif statement."""

a = 2
b = 4

if a<b:
    print(a, 'is less than', b)
elif a >b:
    print(a, 'is greater than', b)
else:
    print(a, 'equals', b)

###### elif with multiple elif blocks

a = 2
if a<0:
    print(a, 'is negative')
elif a==0:
    print('its a 0')
elif a>0 and a<5:
    print(a, 'is in (0,5)')
else:
    print(a, 'equals or greater than 5')

