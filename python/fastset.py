""" Class set optimisation """
import set

class Set(set.Set):
    def __init__(self, value = []):
        self.data = {}
        self.concat(value)

    def intersect(self, other):
        res = {}
        for x in self.data:
            res[x] = None
        return Set(res.keys())

    def union(self, other):
        res = {}
        for x in other:
            res[x] = None
        for x in self.data.keys():
            res[x] = None
        return Set(res.keys())

    def concat(self, value):
        for x in value: self.data[x] = None

    # inherit and, or, len
    def __getitem__(self, ix):
        return list(self.data.keys())[ix]

    def __repr__(self, ix):
        return '<Set:%r>' % list(self.data.keys())

"""
from fasteset import Set
users1 = Set(['Bob', 'Emily', 'Howard', 'Peeper'])
users2 = Set(['Jerry', 'Howard', 'Carol'])
users3 = Set(['Emily', 'Carol'])
users1 & users2

users1 | users2 & users3

(users1 | users2) & users3

users1.data
"""
