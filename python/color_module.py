class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue
    def __str__(self):
        return "Color: R={0:d}, G={1:d}, B={2:d}".format (self._red, \
                self._green, self._blue)
# from color_module import Color
# c = Color(15, 35, 3)
# print(c)
# Color: R=15, G=35, B=3
