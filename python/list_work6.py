"""Program to get data items from a list appearing odd number of times."""

x = [1, 2, 3, 4, 5, 1, 3, 3, 4]
l1 = []
for i in x:
    if x.count(i) % 2 != 0:
        if i not in l1:
            l1.append(i)
print(l1)
'''
Expected output:
    [2, 3, 5]
    '''
