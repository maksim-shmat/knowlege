def four(limit):
    x = 0
    while x < limit:
        print("in generator, x = ", x)
        yield x
        x += 1
for i in four(4):
    print (i)

def four(start, limit):
    x = start
    while x < limit:
        print("in generator, x =", x)
        yield x
        x += 1
for i in four(1, 4):
    print(i)
print()

#2 permute, use it code how file permute.py

def permute1(seq):
    if not seq:
        return[seq]  # random iteration
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]  # remove currently block
        return res

def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]  # remove currently block
            for x in permute2(rest):  # random iteration
                yield seq[i:i+1] + x

# from permute import permute1, permute2
# >>> permute1('abc') - random iteration
# >>> G = permute2('abc') - step
# >>> next(G)
# >>> for x in permute2('abc'): print(x)  - auto iteration
# >>> list(permute2('spam')  # result in a list

#3 Make a list of lists

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested = [[1, 2], [3, 4], [5]]
for num in flatten(nested):
    print(num)  # 1 2 3 4 5
print(list(flatten(nested)))  # [1, 2, 3, 4, 5]

#4 Loopy generators

g = ((i + 2) ** 2 for i in range(2, 27))
print(next(g))  # 16
print(next(g))  # 25

# or that in this case
print(sum(i ** 2 for i in range(10)))  # 285

#5 Recursion generator (potential danger infinite recursion)

def flatten1(nested1):
    try:
        for sublist in nested1:
            for element in flatten1(sublist):
                yield element
    except TypeError:
        yield nested1

print(list(flatten1([[[1], 2], 3, 4,[5, [6, 7]], 8])))  # [1, 2, 3, 4, 5, 6, 7, 8]

#6 If you really want to use send on a newly started generator, you can use
#it with None as it's parameter

def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new

r = repeater(42)
print(next(r))

print(r.send("Hello, world!"))

#7
