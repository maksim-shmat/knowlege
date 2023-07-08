"""map() about."""

'''
def square(n):
    return n**2

x = map(square, [1, 2, 3, 4, 5, 6])
print(list(x))
# [1, 4, 9, 16, 25, 36]

#1 map() with lambda function

x = map(lambda n: n**2, [1, 2, 3, 4, 5, 6])
print(list(x))
# [1, 4, 9, 16, 25, 36]

#2 

fur = list(map(str, range(10)))  # Equivalent to [str(i) for i in range(10)]
print(fur)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
'''
#3 gen map

def adder(*n):
    return sum(n)
s1 = sum(map(lambda *n: adder(*n), range(100), range(1, 101)))
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))
print(s1)
print(s2)

#RESULTS:
    
10000
10000

#4 gen filter

cubes = [x ** 3 for x in range(10)]

odd_cubes1 = filter(lambda cube: cube % 2, cubes)
odd_cubes2 = (cube for cube in cubes if cube % 2)
print(list(odd_cubes1))
print(list(odd_cubes2))

# RESULTS:

[1, 27, 125, 343, 729]
[1, 27, 125, 343, 729]

#5 gen map filter

N = 20

cubes1 = map(lambda n: (n, n**3), filter(lambda n: n % 3 == 0 or n % 5 == 0, range(N)))
cubes2 = ((n, n**3) for n in range(N) if n % 3 == 0 or n % 5 == 0)

print(list(cubes1))
print(list(cubes2))
# RESULTS:

[(0, 0), (3, 27), (5, 125), (6, 216), (9, 729), (10, 1000), (12, 1728), (15, 3375), (18, 5832)]
[(0, 0), (3, 27), (5, 125), (6, 216), (9, 729), (10, 1000), (12, 1728), (15, 3375), (18, 5832)]

#6 

