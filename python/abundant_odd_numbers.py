"""An abundant number is a number n for which the sum of divisors sigma(n)>2n,

or equivalently the sum of proper divisors (or aliquot sum) s(n) > n.
E.G.: 12 is abundant, it has the proper divisors 1,2,3,4 & 6 which sum to 16(>12 or n),
or alternately, has the sigma sum of 1,2,3,4,5,6 & 12 which sum to 28 (>24 or 2n)
Abundant numbers are common, though even abundant numbers seem to be much more
common than odd abundant numbers.
"""

# Procedural style
oddNumber = 1
aCount = 0
dSum = 0

from math import sqrt

def divisorSum(n):
    sum = 1
    i = int(sqrt(n)+1)

    for d in range (2, i):
        if n % d == 0:
            sum += d
            otherD = n // d
            if otherD != d:
                sum += otherD
    return sum

print("The first 25 abundant odd numbers: ")
while aCount < 25:
    dSum = divisorSum(oddNumber)
    if dSum > oddNumber:
        aCount += 1
        print("{0:5} proper divisor sum: {1}".format(oddNumber, dSum))
    oddNumber += 2

while aCount < 1000:
    dSum = divisorSum(oddNumber)
    if dSum > oddNumber:
        aCount += 1
    oddNumber += 2
print("\n1000th abundant odd number:")
print("    ",(oddNumber - 2)," proper division sum: ",dSum)

oddNumber = 1000000001
found = False
while not found:
    dSum = divisorSum(oddNumber)
    if dSum > oddNumber:
        found = True
        print("\nFirst abundant odd number > 1 000 000 000:")
        print("    ", oddNumber, 'proper divisor sum: ', dSum)
    oddNumber += 2

Results:
    :w !python3
The first 25 abundant odd numbers:
  945 proper divisor sum: 975
 1575 proper divisor sum: 1649
 2205 proper divisor sum: 2241
 2835 proper divisor sum: 2973
 3465 proper divisor sum: 4023
 4095 proper divisor sum: 4641
 4725 proper divisor sum: 5195
 5355 proper divisor sum: 5877
 5775 proper divisor sum: 6129
 5985 proper divisor sum: 6495
 6435 proper divisor sum: 6669
 6615 proper divisor sum: 7065
 6825 proper divisor sum: 7063
 7245 proper divisor sum: 7731
 7425 proper divisor sum: 7455
 7875 proper divisor sum: 8349
 8085 proper divisor sum: 8331
 8415 proper divisor sum: 8433
 8505 proper divisor sum: 8967
 8925 proper divisor sum: 8931
 9135 proper divisor sum: 9585
 9555 proper divisor sum: 9597
 9765 proper divisor sum: 10203
10395 proper divisor sum: 12645
11025 proper divisor sum: 11946

1000th abundant odd number:
     492975  proper division sum:  519361

First abundant odd number > 1 000 000 000:
     1000000575 proper divisor sum:  1083561009


