""" One-liners about."""

# Consider an array of numbers. Our task is to add 1 to the numbers at odd indices and to add 2 to the number at even indices.

### with a for-loop
def addOneAndTwo(nums, n):
    for i in range(n):
        if i % 2 == 1:
            nums[i] += 1
        else:
            nums[i] += 2
    return nums

### with list comprehension
def addOneAndTwo(nums, n):
    return [nums[i] + 1 if i % 2 == 1 else nums[i] + 2 for i in range(n)]

######
Input: nums = [2,5,1,3,4,7],n = 3
Output: [2,3,5,4,1,7]

Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is
[2,3,5,4,1,7].

def shuffle(self, nums, n):
    return reduce(lambda a, b: a + b, [[nums[i], nums[j]] for i, j in zip(range(0, n), range(n, 2 * n))])

###### Number of Good Pairs
Input nums=[1,2,3,1,1,3]
Output: 4

Explanation: There are 4 good pairs(0,3),(0,4),(3,4),(2,5) O-indexed.

def numIdenticalPairs(self, nums):
    return sum([int(i != j and nums[i] == nums[j]) for i in range(0, len(nums)) for j in range(i + 1, len(nums))])

###### Kids with the Geratest Number of Candies
Input: candies = [2,3,5,1,3] extraCandies = 3
Output: [true,true,true,false,true]

def kidsWithCandies(sel, candies, extraCandies):
    return [candy + extraCandies >= max(candies) for candy in candies]

###### Decompress Run-Length Encoded List
Input: nums = [1,2,3,4]
Output: [2,4,4,4]

def decompressRLElist(self, nums):
    return reduse(lambda a, b: a + b, [[nums[i + 1]] * nums[i] for i in range(0, len(nums), 2)])

###### Reachest Customer's Wealth
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6

def maximumWealth(self, accounts):
    return max([sum(row) for row in accounts])

#1 
[x * x for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#2
[x * x for x in range(10) if x % 3 == 0]
# [0, 9, 36, 81]

#3
[(x, y) for x in range(3) for y range(3)]
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 1) (2, 2)]

# or

result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))

# 
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
[b+ '+' +g for b in boys for g in girls if b[0] == g[0]]
# ['chris+clarice', 'arnold+alice', 'bob+bernice']

# with dict
girls = ['Alice', 'Bernice', 'Clarice']
boys = ['Chris', 'Arnold', 'Bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b+ '+' +g for b in boys for g in letterGirls[b[0]]])
# ['Chris+Clarice', 'Arnold+Alice', 'Bob+Bernice']

#4 
