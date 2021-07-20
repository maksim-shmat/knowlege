""" Модуль circle_cm: содержит класс Circle. """
class Circle:
    """ Класс Circle """
    all_circle = [] # Переменная содержит список всех созданных экземпляров Circle
    pi = 3.14159
    def __init__(self, r=1):
        """ Создаёт экземпляр Circle c заданным значением radius """
        self.radius = r
        self.__class__.all_circle.append(self)
    def area(self):
        """ Вычислить площадь круга для экземпляра Circle """
        return self.__class__.pi * self.radius * self.radius
    @classmethod
    def total_area(cls):
        total = 0
        for c in cls.all_circle:
            total = total + c.area()
        return total
    
    
