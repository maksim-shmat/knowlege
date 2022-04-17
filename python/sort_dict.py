"""Sort dict example."""

orders = {
        'pizza': 200,
        'burger': 56,
        'pepsi': 25,
        'Coffee': 14
}
sorted_dic = sorted(orders.items(), key=lambda x: x[1])
print(sorted_dic) # [('Coffee', 14), ('pepsi', 25), ('burger', 56), ('pizza', 200)]

#1 sort with lambda for list of dicts

points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)
print(type(points))
