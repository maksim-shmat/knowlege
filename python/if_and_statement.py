"""About if and."""

a = 5
b = 2

# nested if 
if a==5:
    if b>0:
        print('a is 5 and',b,'is greater than zero.')

# or you can combine the conditions as
if a==5 and b>0:
    print('a is 5 and',b,'is greater than zero.')

###### Python if-else statement with and operator
a = 3
b = 2

if a==5 and b>0:
    print('a is 5 and',b,'is greater than zero.')
else:
    print('a is not 5 or',b,'is not greater than zero.')

###### Python elif statement with and operator
a = 8

if a<0:
    print('a is less than zero.')
elif a>0 and a<8:
    print('a is in(0,8)')
elif a>7 and a<15:
    print('a is in (7,15)
