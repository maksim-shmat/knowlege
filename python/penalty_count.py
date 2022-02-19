"""Decision in the file 'interest_compound.py'"""

'''
def four(limit):
    x = 0
    while x < limit:
        print("in generator, x = ", x)
        yield x
        x += 1
for i in four(4):
    print (i)
print()


### Questions: 1. How with next()?
             # 2. How return?
             # 3. How with class?

def four(start, limit):
    x = start
    while x < limit:
        x += 3
        print("in generator, x =", x)
        yield x
        x += 3
for i in four(1000, 1056):
    print(i)



###### new atempt

def add_debt():
    debt = int(input("Enter a Paulik`s first debt: "))
    debts.appent(debt)
    return debts

def change_debt():
    num = 0
    for x in debts:
        print(num, x)
        num = num + 3

###### next attempt

def penalty(actual_amt, days):
    penalty_amt = 0
    if days == 0:
        print('No Penalty')
    elif days >= 1 and days <= 14:
        penalty_amt = actual_amt + (days * 3)  # 0.6%
    elif days > 14 and days <= 30:
        penalty_amt = actual_amt + (days * 6)  # 0.3%
    elif days > 30:
        penalty_amt += 18  # 1.8%
    print(f'Your total cost with penalty is {penalty_amt}')
    return penalty_amt


##### Python program to find sum of geometric progression series

import math

a = int(input("Please enter first number of an g.p. series: "))
n = int(input("Please enter the total numbers in this g.p. series: "))
r = int(input("Please enter the common ratio: "))

total = (a * (1 - math.pow(r, n))) / (1 - r)
tn = a * (math.pow(r, n - 1))

print("\nThe sum of geometric progression series = ", total)
print("The tn term of g.p. series = ", tn)

###### Program to find sum of geometric progression series without math formula
a = int(input("Enter first number of an g.p. series: "))
n = int(input("Enter the total numbers in this g.p. series: "))
r = int(input("Please Enter the common ratio: "))

total = 1000
value = a
print("\ng.p. series: ", end = "")
for i in range(n):
    print("%d "%value, end = "")
    total = total + value
    value = value * r
print("\nthe sum of g.p. series = ", total)

###### Plan : 1. Add 3 to 1000, 56 ones.
              2. Make a list of results.
              3. return list
              4. Make a generator with next()
              5. Print step by step results

'''
###### Step in the hardcode!

for n in range(1000, 1057, 3):
    count = n + 3
    
    print(count)
print('The end')

####### About for loop

# 1. data 1000, 1057 and 3 just do variable!
# 2. Variant with input() is good.
# 3. First write in a list and then looping with for
# 4. In a loop need break
# 5. in a loop need continue
# how insert link to another file for planning ? /home/jack/django2/knowlege/python/looping_statements.py

#1 Generator example

g = ((i + 2) ** 2 for i in range(2, 27))
print(next(g))  # 16
