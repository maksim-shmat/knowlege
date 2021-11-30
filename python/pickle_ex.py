"""Pickle serialization about."""

######1 Python picling or serializing

import pickle

marks = {'Alex': 87, 'Lenin': 98, 'Kuwabara': 90}
picklefile = open('marks', 'wb')
pickle.dump(marks, picklefile)
picklefile.close()

######2 Python unpacking or deserializing

import pickle

picklefile = open('marks', 'rb')
marks = pickle.load(picklefile)
picklefile.close()
print(marks)
print(type(marks))

######3 Pickle a custom python class object

import pickle

class Laptop:

    def __init__(self, name, processor, hdd, ram, cost):
        self.name = name
        self.processor = processor
        self.hdd = hdd
        self.ram = ram
        self.cost = cost

    def details(self):
        print('The details of the laptop are:')
        print('Name        :', self.name)
        print('Processor   :', self.processor)
        print('HDD Capacity:', self.hdd)
        print('RAM         :', self.ram)
        print('Cost($)     :', self.cost)

# create objedt
laptop1 = Laptop('Dell Alienware', 'Intel Core i7', 512, 8, 2500.00)

# create a pickle file
picklefile = open('laptop1', 'wb')
# pickle the dictionary and write it to file
pickle.dump(laptop1, picklefile)
picklefile.close()

### unpickle python custom class object

import pickle

class Laptop:
    
    def __init__(self, name, processor, hdd, ram, cost):
        self.name = name
        self.processor = processor
        self.hdd = hdd
        self.ram = ram
        self.cost = cost

    def details(self):
        print('The details of the laptop are: ')
        print('Name         : ', self.name)
        print('Processorus  : ', self.processor)
        print('HDD Capacity : ', self.hdd)
        print('RAM          : ', self.ram)
        print('Cost($)      : ', self.cost)

# read the pickle file
picklefile = open('laptop1', 'rb')
# unpickle the dataframe
laptop1 = pickle.load(picklefile)
#close file
picklefile.close()

print(type(laptop1))
laptop1.details()

######4 Pickle a dataframe

import numpy as np
import pandas as pd
import pickle

# dataframe
df = pd.DataFrame(
        [['Suomi', 68, 84, 78, 96],
         ['Kiki', 74, 56, 77, 98],
         ['Anlal', 77, 68, 52, 89],
         ['Lenin', 89, 23, 34, 86]],
         columns=['name', 'phisics', 'chemistry', 'algebra', 'calculus'])

# create a file
picklefile = open('df_marks', 'wb')
# pickle the dataframe
pickle.dump(df.picklefile)
piclefile.close()

### Unpickle a dataframe

import numpy as np
import pandas as pd
import pickle

# read the pickle file
picklefile = open('df_marks', 'rb')
# unpickle the dataframe
df = pickle.load(picklefile)
# close file
picklefile.close()

# print the dataframe
print(type(df))
print(df)

######5
