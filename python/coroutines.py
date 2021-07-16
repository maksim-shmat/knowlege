>>> def greet():
    while True:
        name = yield
        print(f'Hello, {name}')

>>> g = greet()
>>>
>>> g.send(None) # priming
>>> g.send('Mark')
Hello, Mark
>>> g.send('Alice')
Hello, Alice

##########
def cor():
    c = 1
    while True:
        name = yield
        print(f"{name} check {c} place")
        c += 1

finish = cor()

>>> finish.send(None)
>>> finish.send("Misa")
Misa check 1 place
>>> finish.send("Sasa")
Sasa check 2 place
