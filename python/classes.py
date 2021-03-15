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

######
