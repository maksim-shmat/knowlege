"""Concatenate two dict in one."""

def merge(dic1, dic2):
    dic3=dic1.copy()
    dic3.update(dic2)
    return dic3
dic1={1:"hello", 2:"world"}
dic2={3:"Python", 4:"Programming"}
a = merge(dic1,dic2)
print(a)
