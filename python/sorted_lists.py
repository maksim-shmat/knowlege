# Имеется список, каждый элемент которого также является списком:
# [[1, 2, 3], [2, 1, 3], [4, 0, 1]]. Надо сортирнуть по второму элементу.
the_list = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
the_list.sort(key=lambda x: x[1])
the_list
