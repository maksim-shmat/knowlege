def simple():
    spam = 'ni'
    def action():
        print(spam)
    return action
act = simple()
act()
#--------------
def normal():
    def action():
        return spam
    spam = 'ni'
    return action
act = normal()
print(act())
#-------------
def weird():
    spam = 42
    return (lambda: spam * 2)
act = weird()
print(act())
#-------------
def weird():
    tmp = (lambda: spam * 2)
    spam = 42
    return tmp
act = weird()
print(act())
#------------
def weird():
    spam = 42
    handler = (lambda: spam * 2)
    spam = 50
    print(handler())
    spam = 60
    print(handler())
weird()
#------------
def odd():
    funcs = []
    for c in 'abcdefg':
        funcs.append((lambda: c))
    return funcs
for func in odd():
    print(func(), end=' ')
#------------
def odd():
    funcs = []
    for c in 'abcdefg':
        funcs.append((lambda c=c: c))
    return funcs
for func in odd():
    print(func(), end=' ')
#------------
funcs = []
for c in 'abcdefg':
    funcs.append((lambda c=c: c))
for func in funcs:
    print(func(), end=' ')
