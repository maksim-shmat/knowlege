"""Find least number how divi without tails for all numbers from 1 to 10."""

import math

def compute():
    answer = 1
    for i in range(1, 21):
        answer *= i // math.gcd(i, answer)
        return answer

if __name__ == "__main__":
    print(compute())

######### 2520 - least number
###### variants:
# C-ctyle

import time
x,y=20,0

while x!=y:
  for i in range(2,21):
    if x%i !=0:
      x+=20
      break
    else:
      y=x
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
print(x)

###### vs Python style, how fast?

import time
x, y = 20,0

while x != y:
    for i in range(2, 21):
        if x % i != 0:
            x += 20
            break
        else:
            y = x
start_time = time.time()
print("---%s seconds---" % (time.time() - start_time))
print(x)

######

from functools import reduce
from math import gcd

def lcm(n):
    return reduce(lambda x,y:x*y//gcd(x,y), range(1,n+1))
print(lcm(20))

######

nums = range(1,21)
result = 1
while len(nums) != 0:
    n = nums[0]
    nums = [num // n if (num % n) == 0 else num for num in nums]
    nums.remove(1)
    result *= n
print(result)

######

def gcd(a, b): # greatest_common_divisor
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b): # smallest common multiple
    return a * b // gcd(a, b) # integer division

d = 1    # keep lcm
for i in range(2, 21):
    d = lcm(d, i)

print(d) 

###### it is speed up my cooler in nootebook
"""
current = 20
lcm = 0
while (lcm == 0):
    for i in range(2, 21):
        if current % i != 0:
            break
    else:
        lcm = current
    current += 20

print(lcm)
"""
######
