class Circle:
    pi = 3.14159
    all_circles = []
    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.appennd(self)

    def area(self):
        return self.radius * self.radius * Circle.pi

    def circumference(self):
        return 2 * self.radius * Circle.pi

    @classmethod
    def total_circumference(cls):
        """ Method of class for count sum length of circle for all
            exemplars Circle.  """
        total = 0
        for c in cls.all_circles:
            total = total + c.circumference()
        return total
