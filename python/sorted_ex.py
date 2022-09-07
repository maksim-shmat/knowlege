"""sorted() about."""

nums = [2, 8, 1, 6, 3, 7, 4, 9]
nums_sorted = sorted(nums)
print(nums_sorted)
print()

###### sorted() with reverse

nums = [2, 8, 1, 6, 3, 7, 4, 9]
nums_sorted = sorted(nums, reverse = True)
print(nums_sorted)
print()

###

nums = [2, 8, 1, 6, 3, 7, 4, 9]
nums_sorted = sorted(nums, reverse = False)
print(nums_sorted)
print()

###### sorted() with key

names = ['apple', 'banana', 'mango', 'orange', 'kiwi', 'plum', 'fig']
names_sorted = sorted(names, key = len)
print(names_sorted)
print()

###

def vowels(x):
    vowel_count = 0
    for char in x.lower():
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
    return vowel_count

names = ['apple', 'banana', 'mango', 'orange', 'kiwi', 'plum', 'fig']
names_sorted = sorted(names, key = vowels)
print(names_sorted)
print()

###### limitation ojn Type of items in iterable with sorted() and key

def myFunc(x):
    if isinstance(x, str):
        return len(x)
    else:
        return x

nums = [2, 8, 1, 7, 'apple', 'watermelon']
nums_sorted = sorted(nums, key = myFunc)
print(nums_sorted)
print()

###### sorted with lambda function as key

names = ['apple', 'banana', 'mango', 'orange', 'kiwi', 'plum', 'fig']
names_sorted = sorted(names, key = lambda name : len(name))
print(names_sorted)
print()

###### sorted() with custom objects

class Fruit:
    def __init__(self, name, count):
        self.name = name
        self.count = count

fruits = [Fruit('apple', 10),
          Fruit('banana', 60),
          Fruit('mango', 5),
          Fruit('orange', 14),
          Fruit('kiwi', 20),
          Fruit('plum', 25),
          Fruit('fig', 100)]

fruits_sorted = sorted(fruits, key = lambda fruit : fruit.count)

for fruit in fruits_sorted:
    print(fruit.name, ',', fruit.count)
print()

###### sorted() with tuples

mytuple = (3, 4, 1, 6, 2)
mytuple_sorted = sorted(mytuple)
print(mytuple_sorted)
print()

###### sorted() with string

mystring = 'apple'
mystring_sorted = sorted(mystring)
print(mystring_sorted)
print()

###### sorted() with sets

myset = {5, 8, 4, 3, 1, 6}
myset_sorted = sorted(myset)
print(myset_sorted)
print()

