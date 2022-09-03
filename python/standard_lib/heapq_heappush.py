"""Make a heap for heapq_showtree.py."""

import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

heap = []
print('random :', data)
print()

for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)

'''RESULTS:
random : [10, 9, 4, 10, 11]

add  10:

                 10                 
------------------------------------

add   9:

                 9                  
        10        
------------------------------------

add   4:

                 4                  
        10                9         
------------------------------------

add  10:

                 4                  
        10                9         
    10   
------------------------------------

add  11:

                 4                  
        10                9         
    10       11   
------------------------------------
'''
