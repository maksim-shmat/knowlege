"""Class about."""

class Developer:
    def createProject(self):    # create a method, self is default argument
        print('The developer created a project.')

### calling the method

class Developer:
    hoursperday = 8

    def createProject(self):
        print('The developer crated a project.')

# create object
dev1 = Developer()

# call object's mehtod
dev1.createProject()

###### createf an object for Class

class Laptop:
    name = 'My Laptop'
    processor = 'Intel Core'

    @staticmethod
    def start():
        print('Laptop is starting..')

    @staticmethod
    def restart(self):
        print('Laptop is restarting')

    def details(self):
        print('My laptop name is:', self.name)
        print('It has', self.processor, 'processor.')

# create object
laptop1 = Laptop()
laptop1.name = 'Dell Alienware'
laptop1.processor = 'Intel Core i7'
laptop1.details()

######
"""Classes and Subclasses."""

###### Python class syntax and behavior

class Drink():
    """Drink class"""
    def __init__(self,size):
        self.size = size
    # Used to display object instance
    def __str__(self):
        return 'Drink: size %s' % (self.size)
    # Helper method for size in ounces
    def sizeinoz(self):
        if self.size == "small":
            return "8 oz"
        elif self.size == "medium":
            return "12 oz"
        elif self.size == "large":
            return "24 oz"
        else:
            return "Unknown"

thedrink = Drink("small")
print(thedrink)
print("thedrink is %s " % thedrink.sizeinoz())

###### Python subclass syntax and behavior

class Coffee(Drink):
    """Coffee class"""
    beans = "arabica"
    def __init__(self,*args,**kwargs):
        Drink.__init__(self,*args)
        self.temperature = kwargs['temperature']
    # Used to display object instance
    def __str__(self):
        return 'Coffee: beans %s, size %s, temperature %s' % (self.beans,self.size,self.temperature)

thecoffee = Coffee("large",temperature="cold")
print(thecoffee)
print("thecoffee is %s " % thecoffee.sizeinoz())

######
class TypedListList(list):
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must "\
                    "be a list.")
        for element in initial_list:
            self.__check(element)
        super().__init__(initial_list)
    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Atttmpted to add an element of "\
                    "incorrect type to a typed list.")
    def __setitem__(self, i, element):
        self.__check(element)
        super().__setitem__(i, element)
x = TypedListList("", 5 * [""])
x[2] = "Hello"
x[3] = "There"
print(x[2] + ' ' + x[3])
a, b, c, d, e = x
print(a, b, c, d)
print(x[:])
x.sort()
print(x[:])
