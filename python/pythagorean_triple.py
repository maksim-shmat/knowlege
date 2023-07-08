"""Pythagorean triple."""

''' functions.py
def gcd(a, b):
    """Calculate the Greatest Common Divisor of (a, b)."""
    while b != 0:
        a, b = b, a % b
    return a
'''

from functions import gcd


N = 50

triples = sorted(
        ((a, b, c) for a, b, c in (
            ((m**2 - n**2), (2 * m * n), (m**2 + n**2))
            for m in range(1, int(N**.5) + 1)
            for n in range(1, m)
            if (m - n) % 2 and gcd(m, n) == 1
        ) if c <= N), key=lambda * triple: sum(*triple)
)
print(triples)

#RESULTS:
#[(3, 4, 5), (5, 12, 13), (15, 8, 17), (7, 24, 25), (21, 20, 29), (35, 12, 37), (9, 40, 41)]
#2 much better

from functions import gcd


def gen_triples(N):
    for m in range(1, int(N**.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 and gcd(m, n) == 1:
                c = m**2 + n**2
                if c <= N:
                    a = m**2 - n**2
                    b = 2 * m * n
                    yield (a, b, c)

triples2 = sorted(
        gen_triples(50), key=lambda * triple: sum(*triple))

print(triples2)

#RESULTS:

#[(3, 4, 5), (5, 12, 13), (15, 8, 17), (7, 24, 25), (21, 20, 29), (35, 12, 37), (9, 40, 41)]
