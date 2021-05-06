"""Interchange First and Last Element of a List."""

list5 = [1, 29, 51, 9, 17, 6, 7, 23]
list5[0], list5[-1] = list5[-1], list5[0]
print(list5)
'''
Expected Output:
    [23, 29, 51, 9, 17, 6, 7, 1]
    '''
