"""Make heap for heapq_showtree.py."""

import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

print('random :', data)
heapq.heapify(data)
print('heapified :')
show_tree(data)

"""RESULTS:
random : [10, 9, 4, 10, 11]
heapified :

                 4                  
        9                 10        
    10       11   
------------------------------------
"""
