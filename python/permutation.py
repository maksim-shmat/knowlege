"""Easy example."""

#1

from itertools import permutations

print(list(permutations('ABC')))

# RESULTS:
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
