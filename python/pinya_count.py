"""Count Paulik's debt."""

"""
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

"""
'''
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
'''
###### next attempt

def penalty(actual_amt, days):
    penalty_amt = 0
    if days == 0:
        print('No Penalty')
    elif days >= 1 and days <= 14:
        penalty_amt = actual_amt + (days * 3)
    elif days > 14 and days <= 30:
        penalty_amt = actual_amt + (days * 6)
    elif days > 30:
        penalty_amt += 18
    print(f'Your total cost with penalty is {penalty_amt}')
    return penalty_amt


