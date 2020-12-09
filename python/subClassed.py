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
