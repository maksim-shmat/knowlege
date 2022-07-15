"""Count abundant odd numbers."""

# Functional style

from math import sqrt
from itertools import chain, count, islice

# abundant Tuple :: Int -> [(Int, Int)]
def abundantTuple(n):
    """A list containing the tuple of N and it's divisor sum,
    if n is abundant, or an empty list.
    """
    x = divisorSum(n)
    return[(n, x)] if n < x else []

# divisorSum :: Int -> Int
def divisorSum(n):
    """Sum or the divisors of n."""
    floatRoot = sqrt(n)
    intRoot = sqrt(n)
    intRoot = int(floatRoot)
    blnSquare = intRoot == floatRoot
    lows = [x for x in range(1, 1 + intRoot) if 0 == n % x]
    return sum(lows + [
        n // x for x in (
            lows[1:-1] if blnSquare else lows[1:]
        )
    ])

# ------- TEST --------
# main :: IO ()
def main():
    """Subsets of abundant odd numbers."""
    # First 25.
    print("First 25 abundant odd numbers with their divisor sums:")
    for x in take(25)(
            concatMap(abundantTuple)(
                enumFromThen(1)(3)
            )
    ):
        print(x)

    # The 1000th.
    print("\n1000th odd abundant number with it's divisor sum:")
    print(
            take(1000)(
                concatMap(abundantTuple)(
                    enumFromThen(1)(3)
                )
            )[-1]
    )

    # First over 10^9.
    print("\nFirst odd abundant number over 10^9, with it's divisor sum:")
    billion = (10 ** 9)
    print(
            take(1)(
                concatMap(abundantTuple)(
                    enumFromThen(1 + billion)(3 + billion)
                )
            )[0]
    )

# -------- GENERAL FUNCTIONS --------

# enumFromThen :: Int -> Int -> [Int]
def enumFromThen(m):
    """A non-finite stream of integers starting at m, and continuing
    at the interval between m and n.
    """
    return lambda n: count(m, n - m)

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    """A concatenated list over which a function f has been mapped.
    The list monad can be derived by usin an (a -> [b])
    function which wraps it's output in a list (using an empty list
    to represent cumputational failure).
    """
    return lambda xs: (
            chain.from_iterable(map(f, xs))
    )

# take :: Int -> [a] -> [a]
def take(n):
    """The prefix of xs of length n, or xs itself if n > length xs."""
    return lambda xs: (
            list(islice(xs, n))
    )

if __name__ == '__main__':
    main()

Results:
    w !python3
First 25 abundant odd numbers with their divisor sums:
(945, 975)
(1575, 1649)
(2205, 2241)
(2835, 2973)
(3465, 4023)
(4095, 4641)
(4725, 5195)
(5355, 5877)
(5775, 6129)
(5985, 6495)
(6435, 6669)
(6615, 7065)
(6825, 7063)
(7245, 7731)
(7425, 7455)
(7875, 8349)
(8085, 8331)
(8415, 8433)
(8505, 8967)
(8925, 8931)
(9135, 9585)
(9555, 9597)
(9765, 10203)
(10395, 12645)
(11025, 11946)

1000th odd abundant number with it's divisor sum:
(492975, 519361)

First odd abundant number over 10^9, with it's divisor sum:
(1000000575, 1083561009)


