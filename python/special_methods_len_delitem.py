class TypedList:
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must "\
                    "be a list.")

        for element in initial_list:
            self.__check(element)
        self.elements = initial_list[:]

    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of "\
                    "incorrect type to a typed list. ")

    def __setitem__(self, i, element):
        self.__check(element)
        self.elements[i] = element
    def __getitem__(self, i):
        return self.elements[i]

    def __delitem__(self, i):
        del self.elements[i]
    def __len__(self):
        return len(self, element)
    def append(self, element):
        self.__check(element)
        self.elements.append(element)

    x = TypedList(1, [1,2,3])
    print(len(x))
    x.append(1)
    del x[2]
# Hz TypedList is not defined
