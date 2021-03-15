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
