"""Pairs for loop."""

#1 classical for loop
items = 'ABCD'
pairs = []

for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))

print(pairs)

# RESULTS:

#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'C'), ('C', 'D'), ('D', 'D')]

#2 list comprehension

items2 = 'EFJH'
pairs2 = [(items2[a], items2[b])
        for a in range(len(items2)) for b in range(a, len(items2))]

print(pairs2)

# RESULTS
#[('E', 'E'), ('E', 'F'), ('E', 'J'), ('E', 'H'), ('F', 'F'), ('F', 'J'), ('F', 'H'), ('J', 'J'), ('J', 'H'), ('H', 'H')]
