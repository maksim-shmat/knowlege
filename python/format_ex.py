"""Formating about."""

### 1

x = "Hello, {}!".format('world')
print(x)
print()
### 2

f = "{}, {}, {}".format('x', 'y', 'z')
print(f)
print()
### 3

s = "{0}, {1}, {2}".format('x', 'y', 'z')
print(s)
print()
### 4

sok = "{2}, {1}, {0}".format('x', 'y', 'z')
print(sok)
print()
### 5

pok = "{2}, {1}, {0}".format(*'xyz')
print(pok)
print()
### 6

firmpr = "{0} {1} {0}".format('mann', 'gegen')
print(firmpr)
print()
### 7

foc = "My name is {name} and i'm {years} years old"\
        .format(years=35, name="Peta")
print(foc)
print()
### 8

var = {"years": "35", 'name': 'Pumpy'}
zuc = "My name is{name} and i'm {years} years old"\
        .format(**var)
print(zuc)
print()
### 9

cord = (3, 5)
fihr = 'x: {0[0]}; y: {0[1]}'.format(cord)
print(fihr)
print()
### 10

zuza = "repr() shows quotes: {!r}; str() doesn't:\
    {!s}".format('test1', 'test2')
print(zuza)
print()
### 11

fiscrs = '{:<30}'.format('left aligned')
print(fiscrs)
print()
### 12

fux = '{:>20}'.format('right aligned')
print(fux)
print()
### 13

fofo = "{:^30}".format('centred')
print(fofo)
print()
### 14

sombr = '{:*^30}'.format('centered')
print(sombr)
print()
### 15

pipa = '{:+f}; {:+f}'.format(3.14, -3.14)
print(pipa)
print()
### 16

jungl = '{:f}; {:f}'.format(3.14, -3.14)
print(jungl)
print()
### 17

fumbr = '{:-f}; {:-f}'.format(3.14, -3.14)
print(fumbr)
print()
### 18

fecr = "int:{0:d}; hex:{0:x}; oct:{0:o}; bin:{0:b}".format(42)
print(fecr)
print()
### 19

points = 19.5
total = 22
jigl = 'correct answers: {:.2%}'.format(points/total)
print(jigl)
print()

###### more examples with numbers

num1 = '{0:d}'.format(999999999999)
print(num1)
print()
###

num2 = '{0:,d}'.format(999999999999)
print(num2)
print()

###

num3 = '{:,d} {:,d}'.format(99999999, 88888888)
print(num3)
print()

###

num4 = '{:,.2f}'.format(296999.2567)
print(num4)
print()

###### 
