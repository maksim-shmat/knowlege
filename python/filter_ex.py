"""filter() about."""

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

output = filter(even, list1)

for x in output:
    print(x)
print()

###### filter() with lambda function

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

output = filter(lambda n: True if n % 2 == 0 else False, list1)

for x in output:
    print(x)
print()

######
