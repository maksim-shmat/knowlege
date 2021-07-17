"""Formating about."""

### 1

x = "Hello, {}!".format('world')
print(x)

### 2

f = "{}, {}, {}".format('x', 'y', 'z')
print(f)

### 3

s = "{0}, {1}, {2}".format('x', 'y', 'z')
print(s)

### 4

sok = "{2}, {1}, {0}".format('x', 'y', 'z')
print(sok)

### 5

pok = "{2}, {1}, {0}".format(*'xyz')
print(pok)

### 6

firmpr = "{0} {1} {0}".format('mann', 'gegen')
print(firmpr)

### 7

foc = "My name is {name} and i'm {years} years old"\
        .format(years=35, name="Peta")
print(foc)

### 8

var = {"years": "35", 'name': 'Pumpy'}
zuc = "My name is{name} and i'm {years} years old"\
        .format(**var)
print(zuc)

### 9

cord = (3, 5)
fihr = 'x: {0[0]}; y: {0[1]}'.format(cord)
print(fihr)

### 10

zuza = "repr() shows quotes: {!r}; str() doesn't:\
    {!s}".format('test1', 'test2')
print(zuza)

### 11

fiscrs = '{:<30}'.format('left aligned')
print(fiscrs)

### 12

fux = '{:>20}'.format('right aligned')
print(fux)

### 13

fofo = "{:^30}".format('centred')
print(fofo)

### 14

sombr = '{:*^30}'.format('centered')
print(sombr)

### 15

pipa = '{:+f}; {:+f}'.format(3.14, -3.14)
print(pipa)

### 16

jungl = '{:f}; {:f}'.format(3.14, -3.14)
print(jungl)

### 17

fumbr = '{:-f}; {:-f}'.format(3.14, -3.14)
print(fumbr)

### 18

fecr = "int:{0:d}; hex:{0:x}; oct:{0:o}; bin:{0:b}".format(42)
print(fecr)

### 19

points = 19.5
total = 22
jigl = 'correct answers: {:.2%}'.format(points/total)
print(jigl)

