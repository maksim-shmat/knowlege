""" a, aq, aq2, aq3, ..."""

def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q**k
        if result <= 100000:
            yield result
        else:
            return
        k += 1

for n in geometric_progression(2, 5):
    print(n)

# RESULTS:
'''
2
10
50
250
1250
6250
31250
'''
