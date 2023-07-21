"""Method resolution order about."""

#1

class A:
    label = 'a'


class B(A):
    label = 'b'


class C(A):
    label = 'c'


class D(B, C):
    pass

d = D()
print(d.label)  # b
print(d.__class__.mro())

b
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


