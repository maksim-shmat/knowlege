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
