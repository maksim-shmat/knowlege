"""Sort list example."""

my_list = ["leaf", "cherry", "fish"]
my_list1 = ["D", "C", "B", "A"]
my_list2 = [1,2,3,4,5]

my_list.sort() # ['cherry', 'fish', 'leaf']
my_list1.sort() # ['A', 'B', 'C', 'D']
print(sorted(my_list2, reverse=True)) # [5, 4, 3, 2, 1]

# new Apr 16

points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)
print(type(points))
