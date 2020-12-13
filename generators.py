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
