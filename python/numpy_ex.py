"""Numpy about. That's now numpy from pip install"""

#1 Creating arays

import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 77, 2, 3])

print(a[0])
print(b[2])

#2 Multi-dementional arrays

ao = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


#3 Much bigger array, and it is 3x3x4 matrix.

ai = np.array([
    [
        [10, 20, 30, 40], [8, 8, 2, 1], [1, 1, 1, 2]
    ],
    [
        [9, 9, 2, 39], [1, 2, 3, 3], [0, 0, 3, 2]
    ],
    [
        [12, 33, 22, 1], [22, 1, 22, 2], [0, 2, 3, 1]
    ]
    ], dtype=float)

#4 Create a 3x5x4 matrix wich is filled with sevens

aa = np.full((3, 5, 4), 7)

#4 Create 3x3 array full of zeros

a1 = np.zeros((3, 3))

#5 Create four-dimensional array full of ones

b1 = np.ones((2, 3, 4, 2))

#6 Create an empty array

a2 = np.empty((4, 4))

#7 Create array that is filled with random numbers

b2 = np.random.random((2, 3))

#8 Create a list with values that range from the min to the max

a3 = np.arange(10, 50, 5)

#9 Create a list from a min value to a max value. 

b4 = np.linspace(0, 100, 11)  # contains an eleven elements, with distance

#10 Attributes of arrays

# a.shape - Returns the shape of the array e.g.(3,3) or (3,4,7)
# a.ndim - Returns how many dimensions our array has
# a.size - Returns the amount of elements an array has
# a.dtype - Returns the data type of the values in the array

#11 Arithmetic operations

a4 = np.array([
    [1, 4, 2],
    [8, 8, 2]
])

print(a4 + 2)
print(a4 -2)
print(a4 * 2)
print(a4 / 2)

#12 Arithmetic operations with two arrays

a5 = np.array([
    [1, 4, 2],
    [8, 8, 2]
])

b5 = np.array([
    [1, 2, 3]
])

c5 = np.array([
    [1],
    [2]
])

d5 = np.array([
    [1, 2, 3],
    [3, 2, 1]
])

print(a5+b5)
print(a5+c5)

#13 NumPy mathematical function

# np.exp(a) - Takes e to the power of each value
# np.sin(a) - Returns the sine of each value
# np.tan(a) - Returns the tangent of each value
# np.log(a) - Returns the logarithm of each value
# np.sqrt(a) - Returns the square root of each value

#14 NumPy aggregate function

# a.sum() - Returns the sum of all values in the array
# a.mean() - Returns the arithmetic mean of all values in the array
# np.median(a) - Returns the median value of the array
# np.std(a) - Returns the standard deviation of the valuees in the array

#15 Manipulating arrays

a6 = np.array([
    [4, 2, 9],
    [8, 3, 2]
])

a6[1][2] = 7
print(a6)

#16
