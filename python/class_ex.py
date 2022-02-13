"""More class examples."""

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
