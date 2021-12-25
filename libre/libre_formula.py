"""Libreoffice formula about."""

#1 Enter with new lin

new line  # five lines available

#2 Square and not equal

a^2  # a in square
i <>j  # not equal

#3 Square root

sqrt {a}  #square root

#4 Little n

a_n  # a in underscore n

#5 Intergral

int f(x) dx  # integral

#6 Less

a <= b  # less or equals

#7 X

a times b  # multiplication

#8 

sum a_n  # unknow awful

#9 Mebius

infinity  # Mebius character

#10

x cdot y  # emmm, something dot

#11 Greek

%lambda  # Greek character
%LAMBDA  # UPPERCASE LAMBDAAAA
%iTHETA  # italic Greek character

#12 underline

2 over x +1  # first and underline second and after + 1

2 over {x + 1} # first ungerline x+1

x over lbrace -x+1 rbrace  # result underline into curly braces

#13 Matrix

matrix {a # b ## c # d}     # a and b, then underline, c and d

(matrix {a # b ## c # d})   # add small braces

left(matrix {a # b ## c # d}right)  # add big braces

left(matrix {1 # 2 # 3 ## 4 # ` # 6} right)  # where ` then empty
    )}}}))}  # it's brakets for python

#14 Unpaired brackets

abs x = left lbrace stack {x "for" x >= 0 # -x "for" x <0} right none
        } # it's braket for python

#15 Empty after equals character (if you need)

="", ={}, =`, =~

#16 Space between characters in a formula

`, ~, ""

#17 Adding limits to sum/integral commands

sum from k = 1 to n a_k  # n above, k=1 beneath

sum from{i=1} to{n} sum from{j=1; i<>j} to{m} x_ij  # n,m above; i=1,j=1 beneathe

int from 0 to x f(t) dt  # x above; 0 beneathe

int_0^x f(t) dt  # x above and after integral; 0 beneathe and after integral

int from Re f  # Re beneathe integral

#18 Derivatives

{df} over {dx}

{partial f} over {partial y}

{partial^2 f} over {partial t^2}

#19 Write caracter as text

2"%" = 0.02  # 2%=0.02

#20 Italic text

"Hello "World""  # World is italic

#21 Aligning formulas

matrix{alignr x+y # {}={} # alignl 2 ## alignr x {}={} # alignl 2-y}
        ## x + y and x in one column; 2 and 2-y in another column
        } # this bracket for python

#22 Color characters

color red { 5 times 4}
# magenta, purple, black, grey, red, blue, green, yellow, white

#23 
