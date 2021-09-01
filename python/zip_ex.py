"""zip() about."""

list_a = [0, 1, 2]
list_b = ['zero', 'one', 'two']
list_c = ['adzin', 'djva', 'tsiri']
zizi = list(zip(list_a, list_b, list_c))
print(zizi)
print()
for a, b, c in zip(list_a, list_b, list_c):
    print(f'{a} is {b} in English and {c} in Murmurians.')
