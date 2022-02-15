"""Properties about."""

#1

class Rectangle():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if new_x >= 0:
            self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        if new_y >= 0:
            self.__y = new_y

my_rect = Rectangle(1,2)
print(my_rect.x, my_rect.y)
my_rect.x = 4
my_rect.y = 5
print(my_rect.x, my_rect.y)

#2

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height
    size = property(get_size, set_size)  # property string

r = Rectangle()
r.width = 10
r.height = 5
print(r.get_size())  # (10, 5)  without property string
#r.set_size((150, 100))
print(r.width)  # 150  witout property string

print(r.size)  # (10, 5)  with property
r.size = 151, 101
print(r.width)

#3
