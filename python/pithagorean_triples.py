"""Pithagorean triples."""

#1 
from math import sqrt


# this will generate all possible pairs

mx = 10
triples = [(a, b, sqrt(a**2 + b**2))
        for a in range(1, mx) for b in range(a, mx)]
# this will filter out all non pythagorean triples
triples = list(
        filter(lambda triple: triple[2].is_integer(), triples))

print(triples)

# RESULTS:
#
[(3, 4, 5.0), (6, 8, 10.0)]

#2 get integers against the float with map

from math import sqrt


mx1 = 10
triples2 = [(a, b, sqrt(a**2 + b**2))
        for a in range(1, mx1) for b in range(a, mx1)]
triples2 = filter(lambda triple: triple[2].is_integer(), triples2)
# this will make the third number in the tuples integer
triples2 = list(
        map(lambda triple: triple[:2] + (int(triple[2]), ), triples2))

print(triples2)

# RESULTS:
#[(3, 4, 5), (6, 8, 10)]

#3 with list comprehension

from math import sqrt


mx2 = 10
triples3 = [(a, b, sqrt(a**2 + b**2))
        for a in range(1, mx2) for b in range(a, mx2)]
# here we combine filter and map in one CLEAN list comprehension
triples3 = [(a, b, int(c)) for a, b, c in triples if c.is_integer()]
print(triples2)

# RESULTS:
#[(3, 4, 5), (6, 8, 10)]
