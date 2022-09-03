"""Get max/min values from heap."""

import heapq
from heapq_heapdata import data

print('all       :', data)
print('3 largest :', heapq.nlargest(3, data))
print('from sort :', list(reversed(sorted(data)[-3:])))
print('3 smallest:', heapq.nsmallest(3, data))
print('from sort :', sorted(data)[:3])

"""RESULTS:
all       : [10, 9, 4, 10, 11]
3 largest : [11, 10, 10]
from sort : [11, 10, 10]
3 smallest: [4, 9, 10]
from sort : [4, 9, 10]
"""
