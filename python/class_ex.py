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
'''
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

#4
