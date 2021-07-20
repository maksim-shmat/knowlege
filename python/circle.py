""" Модуль circle: содержит класс Circle. """
class Circle:
    """ Класс Circle """
    all_circles = [] # Переменная класса содержит список всех созданных экземпляров Circle
    pi = 3.14159
    def __init__(self, r=1):
        """ Создать экземпляр Circle с заданным значением radius """
        self.radius = r
        self.__class__.all_circle.append(self) # При инициализации экземпляра он добавляет
# себя в список def area(self):
        """ Вычислить площадь круга для экземпляра Circle """
        return self.__class__.pi * self.radius * self.radius
    @staticmethod
    def total_area():
        """ Статический метод для вычесления площади всех Circle """
        total = 0
        for c in Circle.all_circles:
            total = total + c.area()
        return total
