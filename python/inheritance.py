"""Inheritance about."""

class Engine:
    def start(self):
        pass

    def stop(self):
        pass


class ElectricEngine(Engine):  # Is-A Engine
    pass


class V8Engine(Engine):  # Is-A Engine
    pass


class Car:
    engine_cls = Engine

    def __init__(self):
        self.engine = self.engine_cls()  # Has-A Engine

    def start(self):
        print(
                'Starting engine {0} for car {1}... Wroom, wroom!'
                .format(
                    self.engine.__class__.__name__,
                    self.__class__.__name__)
        )
        self.engine.start()

    def stop(self):
        self.engine.stop()


class RaceCar(Car):  # Is_A Car
    engine_cls = V8Engine


class CityCar(Car):  # Is-A Car
    engine_cls = ElectricEngine


class F1Car(RaceCar):  # Is-A RaceCar and alse Is_A Car
    pass  # engine_cls same as parent

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]

for car in cars:
    car.start()

# RESULTS:
#Starting engine Engine for car Car... Wroom, wroom!
#Starting engine V8Engine for car RaceCar... Wroom, wroom!
#Starting engine ElectricEngine for car CityCar... Wroom, wroom!
#Starting engine V8Engine for car F1Car... Wroom, wroom!

#2 Check it in the diff file for those code

from inheritance import Car, RaceCar, F1Car



car = Car()
racecar = RaceCar()
f1car = F1Car()
cars = [(car, 'car'), (racecar, 'racecar'), (f1car, 'f1car')]
car_classes = [Car, RaceCar, F1Car]

for car, car_name in cars:
    for class_ in car_classes:
        belongs = isinstance(car, class_)
        msg = 'is a' if belongs else 'is not a'
        print(car_name, msg, class_.__name__)

""" Prints:
    car is a Car
    car is not a RaceCar
    car is not a F1Car
    racecar is a Car
    racecar is a RaceCar
    racecar is not F1Car
    f1car is a Car
    f1car is a RaceCar
    f1car is a F1Car
    """

#3 Check it 

for class1 in car_classes:
    for class2 in car_classes:
        is_subclass = issubclass(class1, class2)
        msg = '{0} a subclass of'.format(
                'is' if is_subclass else 'is not')
        print(class1.__name__, msg, class2.__name__)
"""Prints:
Car is a subclass of Car
Car is not a subclass of F1Car
Car is not a subclass of F1Car
RaceCar is a subclass of Car
RaceCar is a subclass of RaceCar
RaceCar is not a subclass of F1Car
F1Car is a subclass of Car
F1Car is a subclass of RaceCar
F1Car is a subclass of F1Car
"""

