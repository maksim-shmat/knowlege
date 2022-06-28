"""Classical problem a + b about."""

# Console
try: raw_input  # for python2
except: raw_input = input

print(sum(map(int, raw_input().split())))

# File

import sys

for line in sys.stdin:
    print(sum(map(int, line.split())))

# Console Python3 only

a = int(input("First number: "))
b = int(input("Second number: "))
print("Result: ", a+b)

