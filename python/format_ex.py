"""Formating about."""

#1

x = "Hello, {}!".format('world')
print(x)
print()
#2

f = "{}, {}, {}".format('x', 'y', 'z')
print(f)
print()
#3

s = "{0}, {1}, {2}".format('x', 'y', 'z')
print(s)
print()
#4

sok = "{2}, {1}, {0}".format('x', 'y', 'z')
print(sok)
print()
#5

pok = "{2}, {1}, {0}".format(*'xyz')
print(pok)
print()
#6

firmpr = "{0} {1} {0}".format('mann', 'gegen')
print(firmpr)
print()
#7

foc = "My name is {name} and i'm {years} years old"\
        .format(years=35, name="Peta")
print(foc)
print()
#8

var = {"years": "35", 'name': 'Pumpy'}
zuc = "My name is{name} and i'm {years} years old"\
        .format(**var)
print(zuc)
print()
#9

cord = (3, 5)
fihr = 'x: {0[0]}; y: {0[1]}'.format(cord)
print(fihr)
print()
#10

zuza = "repr() shows quotes: {!r}; str() doesn't:\
    {!s}".format('test1', 'test2')
print(zuza)
print()
#11

fiscrs = '{:<30}'.format('left aligned')
print(fiscrs)
print()
#12

fux = '{:>20}'.format('right aligned')
print(fux)
print()
#13

fofo = "{:^30}".format('centred')
print(fofo)
print()
#14

sombr = '{:*^30}'.format('centered')
print(sombr)
print()
#15

pipa = '{:+f}; {:+f}'.format(3.14, -3.14)
print(pipa)
print()
#16

jungl = '{:f}; {:f}'.format(3.14, -3.14)
print(jungl)
print()
#17

fumbr = '{:-f}; {:-f}'.format(3.14, -3.14)
print(fumbr)
print()
#18

fecr = "int:{0:d}; hex:{0:x}; oct:{0:o}; bin:{0:b}".format(42)
print(fecr)
print()
#19

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

#20 
"{3}{0}{2}{1}{3}{0}".format("be", "not", "or", "to")
# 'to be or not to be'

#21 
from math import pi

pi = '{name} is aproximately {value:.2f}.'.format(value=pi, name="\u03C0")
print(pi)

# and equivalent with f-string
from math import pi
pi1 = f"\u03C0 is aproximately {pi}."
print(pi1)

#22

zutsct = "{foo}{}{bar}{}".format(1, 2, bar=4, foo=3)
print(zutsct)  # 3142

#23

zibrst = "{foo}{1}{bar}{0}".format(1,2, bar=4, foo=3)
print(zibrst)  # 3241

#24

fullname = ["Alfred", "Smoketoomuch"]
vustr = "Mr {name[1]}".format(name=fullname)
print(vustr)  # Mr Smoketoomuch

#25 

import math
tmpl = "The {mod.__name__} module defines the value {mod.pi} for '\u03C0'"
tmpl.format(mod=math)
print(tmpl)  # that's old version?

#26

print("{pi!s}{pi!r}{pi!a}".format(pi="п"))  # s-str, r-repr, a-ascii
# п 'п' '\u03c0'

#27 

print("The number is {num}".format(num=42))  # 42
print("numbe is{num:f}".format(num=42))  # 42.000000
print("num is {num:b}".format(num=42))  # 101010
print("num is {num:%}".format(num=42))  # 4200.000000%
print("num is {num:x}".format(num=42))  # 2a
print("num is {num:o}".format(num=42))  # 52

#28      Width format

print("{num:10}".format(num=3))
print("{name:10}".format(name="Bob"))
print("Pi day is {pi:.2f}".format(pi=pi))
print("{pi:10.2f}".format(pi=pi))
print("{:.5}".format("Guido van Rossum"))
print("One googol is {:,}".format(10**100))

#29 Sign, alignment, and Zero-padding

print('{:010.2f}'.format(pi))
print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi))
print("{:$^15}".format(" WIN BIG"))  # $$$ WIN BIG $$$
print('{0:10.2f}\n{1:10.2f}'.format(pi, -pi))
print('{0:10.2f}\n{1:=10.2f}'.format(pi, -pi))
print('{0:-.2}\n{1:-2}'.format(pi, -pi)) # Default
print('{0:+.2}\n{1:+.2}'.format(pi, -pi))
print('{0:.2}\n{1:.2}'.format(pi, -pi))

print("{:b}".format(42))
print("{:#b}".format(42))

print("{:g}".format(42))
print("{:#g}".format(42))  # with decimal zeroes


