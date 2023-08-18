"""profile and pstats about."""


#1 profile fibonacci raw

import profile

'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq

profile.run('print(fib_seq(20)); print()')

RESULTS:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

         57359 function calls (69 primitive calls) in 0.070 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       21    0.000    0.000    0.000    0.000 :0(append)
        1    0.000    0.000    0.060    0.060 :0(exec)
       20    0.000    0.000    0.000    0.000 :0(extend)
        2    0.000    0.000    0.000    0.000 :0(print)
        1    0.010    0.010    0.010    0.010 :0(setprofile)
     21/1    0.000    0.000    0.060    0.060 <stdin>:18(fib_seq)
 57291/21    0.060    0.000    0.060    0.003 <stdin>:9(fib)
        1    0.000    0.000    0.060    0.060 <string>:1(<module>)
        1    0.000    0.000    0.070    0.070 profile:0(print(fib_seq(20)); print())
        0    0.000             0.000          profile:0(profiler)

'''

#2 profile fibonacci memoized

import functools
import profile

'''
@functools.lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq

if __name__ == '__main__':
    profile.run('print(fib_seq(20)); print()')

RESULTS:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

         89 function calls (69 primitive calls) in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       21    0.000    0.000    0.000    0.000 :0(append)
        1    0.000    0.000    0.000    0.000 :0(exec)
       20    0.000    0.000    0.000    0.000 :0(extend)
        2    0.000    0.000    0.000    0.000 :0(print)
        1    0.011    0.011    0.011    0.011 :0(setprofile)
       21    0.000    0.000    0.000    0.000 <stdin>:54(fib)
     21/1    0.000    0.000    0.000    0.000 <stdin>:64(fib_seq)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.012    0.012 profile:0(print(fib_seq(20)); print())
        0    0.000             0.000          profile:0(profiler)

'''

#3 profile runctx

import profile
'''
from profile_fibonacci memoized import fib, fib_seq


if __name__ == '__main__':
    profile.runctx(
            'print(fib_seq(n)); print()',
            globals(),
            {'n': 20},
    )
'''

#4 profile stats

import cProfile as profile
import pstats
'''
from profile_fibonacci_memorized import fib, fib_seq


# Create 5 sets of static objects
for i in range(5):
    filename = 'profile_stats_{}.stats'.format(i)
    prifile.run('print({}, fib_seq(20))'.format(i), filename)

# Read all 5 file stats in one object
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add('profile_stats_{}.stats'.format(i))

# Remove info paths about from all files
stats.strip_dirs()

# Sort stats on total runtime
stats.sort_stats('cumulative')

stats.print_stats()

'''

#5 profile stats restricted

import profile
import pstats
'''
from profile_fibonacci_memoized imiport fib, fib_seq


# Read all stats in one
stats = pstast.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add('profile_stats_{}.stats'.format(i))
stats.strip_dirs()
stats.sort_stats('cumulative')

# restrict "(fib" only
stats.print)stats('\(fib')
'''

#6 profile stats callers

import cProfile as profile
import pstats
'''
from profile_fibonacci_memoized import fib, fib_seq


# Read all 5 files in one object
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add('profile_stats_{}.stats'.format(i))
stats.strip_dirs()
stats.sort_stats('cumulative')

print('INCOMING CALLERS:')
stats.print_callers('\(fib')

print('OUTGOING CALLERS:')
stats.print_callers('\(fib')
'''

#7 timeit example

import timeit

'''
t = timeit.Timer("print('main statement')", "print('setup')")

print('TIMEIT:')
print(t.timeit(2))

print('REPEAT:')
print(t.repeat(3, 2))

RESULTS:
TIMEIT:
setup
main statement
main statement
3.0780211091041565e-06
REPEAT:
setup
main statement
main statement
setup
main statement
main statement
setup
main statement
main statement
[2.252054400742054e-06, 2.1149171516299248e-06, 2.152053639292717e-06]
'''
#8 triples

def calc_triples(mx):
    triples = []
    for a in range(1, mx + 1):
        for b in range(a, mx + 1):
            hypotenuse = calc_hypotenuse(a, b)
            if is_int(hypotenuse):
                triples.append((a, b, int(hypotenuse)))
    return triples

def calc_hypotenuse(a, b):
    return (a**2 + b**2) ** .5  # or return (a*a + b*b) ** .5 for increase speed run

def is_int(n):  # n is expected to be a float
    return n.is_integer()  # or return n == int(n) for increase speed run

triples = calc_triples(1000)

# $ python -m cProfile profile_test_ex.py

#9
