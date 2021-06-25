"""Algorithm named is 'strategy', about it."""

# print on the screen strategy
def console_writer(info):
    print(info)

# write to the file strategy
def file_writer(info):
    with open('log.txt', 'a') as file:
        file.write.(info + '\n')

# user chose strategy
if input('Write to file?
        [Y/N]') == 'Y':
    client(writer=file_writer)
else:
    client(writer=console_writer)

###### In object variation
class Adder:
    def do_work(self, x, y):
        return x + y


class Multiplicator:
    def do_work(self, x, y):
        return x * y


class Calculator:
    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, x, y):
        print('Result is', self.strategy.do_work(x, y))

calc = Calculator()
calc.set_strategy(Adder())
calc.calculate(10, 20)

calc.set_strategy(Multiplicator())
calc.calculate(10, 20)

###### with inherit
from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    @abstractmethod
    def do_work(self, x, y):
        pass


class Adder(BaseStrategy):
    def do_work(self, x, y):
        return x + y


class Multiplicator(BaseStrategy):
    def do_work(self, x, y):
        return x * y


class Calculator:
    def set_strategy(self, strategy: BaseStrategy):
        self.strategy = strategy

    def calculate(self, x, y):
        print('Result is', self.strategy.do_work(x, y))

######
