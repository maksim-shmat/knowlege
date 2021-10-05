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

######2 permute, use it code how file permute.py

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

### from permute import permute1, permute2
# >>> permute1('abc') - random iteration
# >>> G = permute2('abc') - step
# >>> next(G)
# >>> for x in permute2('abc'): print(x)  - auto iteration
# >>> list(permute2('spam')  # result in a list

######3
