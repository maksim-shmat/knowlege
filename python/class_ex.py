"""More class examples."""

'''
#1 Using the super()

class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No thanks!')


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)

sb = SongBird()
print(sb.sing())
print(sb.eat())
print(sb.eat())

#2

def check_index(key):
    """
    Is the given key an acceptable index?
    To be acceptable, the key should be a non-negative integer.If it
    is not an integer, a TypeError is raised; if it is neragative, an
    IndexError is raised (since the sequence is of infinite length).
    """
    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError

class ArithmeticSequence:
    
    def __init__(self, start=0, step=1):
        """
        Initialize the arithmetic sequence.
        start - the first value in the sequence
        step - the difference between two adjacent values
        changed - a dictionary of values that have been modified by
        the user.
        """
        self.start = start  # Store the start value
        self.step = step  # Store the step value
        self.changed = {}  # No items have been modified

    def __getitem__(self, key):
        """Get an item from the arithmetic sequence."""
        check_index(key)
        try: return self.changed[key]  # Modified?
        except KeyError:  # otherwise...
            return self.start + key * self.step  # ...calculate the value

    def __setitem__(self, key, value):
        """Change an item in the arithmetic sequence."""
        check_index(key)
        self.changed[key] = value  # Store the changed value

s = ArithmeticSequence(1, 2)
print(s[4])  # 9
s[4] = 2
print(s[4])  # 2
print(s[5])  # 11

#3 

class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)

cl = CounterList(range(10))
print(cl)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cl.reverse()
print(cl)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

del cl[3:6]
print(cl)  # [9, 8, 7, 3, 2, 1, 0]

print(cl.counter)     # 0
print(cl[4] + cl[2])  # 9
print(cl.counter)     # 2
'''
##4 Changeable parameter

class Car():
    
    def __init__(self, make, model, year, gas_tank=''):
        """Init atributes car info."""
        self.make = make
        self.model = model
        self.year = year
        self.gas_tank = gas_tank
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return formatted describe."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def fell_gas_tank(self):
        """Benzin."""
        print("This gas tank is big.")

    def read_odometer(self):
        """Return mileage of car."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """For not rollback odometer."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add values to odometer."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.fell_gas_tank()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.fell_gas_tank()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


class Battery():  # not inherit from Car
    """Simply model acb of Ecar."""
    
    def __init__(self, battery_size=75):
        """Init attrs of acb."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Info about power of acb."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """How many miles move you car in one acb."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Specific for electrocars parameters."""

    def __init__(self, make, model, year):
        """Init parent class atributes."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fil_gas_tank(self):  # It's name cover name in the parent class
        """Electromobile not have gas_tank."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.fil_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

Results:
2019 Audi A4
This gas tank is big.
This car has 23 miles on it.
2015 Subaru Outback
This car has 23500 miles on it.
This gas tank is big.
This car has 23600 miles on it.
2019 Tesla Model S
This car doesn`t need a gas tank!
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.

##5
from time import ctime

class MyClass(object):
    def __init__(self, date):
        print("instance created at:", date)

m = myClass(ctime())
print(m)

Results:
    instance created at: Wed Aut 15 00.23.18 20xx

#6
