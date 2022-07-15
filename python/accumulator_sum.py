"""Accumulator of sum."""
'''
def accumulator(sum):
    def f(n):
        f.sum += n
        return f.sum
    f.sum = sum
    return f

x = accumulator(1)
n1 = x(5)
print(n1)
n1 = x(2.3)
print(n1)

x2 = accumulator(3)
n2 = x2(5)
print(n2)
n2 = x2(3.3)
print(n2)

Results:
6
8.3
8
11.3

# another version

def accumulator(sum):
    def f(n):
        nonlocal sum
        sum += n
        return sum
    return f

x = accumulator(1)
x(5)
print(accumulator(3))
print(x(2.3))

Results:
<function accumulator.<locals>.f at 0x7f916adcbc70>
8.3
'''

# more another version

def accumulator(sum):
    while True:
        sum += yield sum

x = accumulator(1)
x.send(None)
x.send(5)
print(accumulator(3))
print(x.send(2.3))

Results:
<generator object accumulator at 0x7f0667ac5ee0>
8.3

