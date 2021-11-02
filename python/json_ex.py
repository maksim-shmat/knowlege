"""JSON about."""

######1 read .json

import json

with open('jill.json', 'r', encoding = 'utf-8') as json_file:
    a = json_file.read()
    b = json_file.read()
    print('a: ', a)
    print('b: ', b)

######2 write to json (dump)

import json
outfile = open("mars_data_01.json", "w")
json.dump(weather, outfile)
outfile.close()
json.dumps(weather)

from pprint import pprint as pp

print(json.dumps(weather, indent=2))

######3 go in json in dict for safe

outfile = open("mars_data.json", 'w')
weather_obj = {"reports": weather_list, "count": 2}
json.dump(weather, outfile)
outfile.close()

### load
with open("mars_data.json") as infile:
    weather_obj = json.load(infile)

######4 Create json string from dictionary

import json

dictionary = {'a': 34, 'b': 61, 'c': 82}
jsonString = json.dumps(dictionary, indent=4)
print(jsonString)

### Create json string from list

import json

myList = [{'a': 54}, {'b': 41, 'c': 87}]
jsonString = json.dump(myList, indent=4)
print(jsonString)

### Create json string from tuple

import json

myTuple = ({'a': 54}, {'b': 42, 'c':38})
jsonString = json.dumps(myTuple, indent=4)
print(jsonString)

######5 Parse json string to list

import json

jsonStr = '[{"name": "Testla", "age": 2352, "city": "New Orlan"}, {"name": "Testla", "age": 23, "city": "Radomption"}]'

pythonObj = json.loads(jsonStr)
print(type(pythonObj))
print(type(pythonObj[0]))
city = pythonObj[1]['city']
print(city)

###### Convert Class object to json string

import json

class Laptop:
    name = 'My Laptop'
    processor = 'Intel Core'

laptop1 = Laptop()
laptop1.name = 'Dell Alienware'
laptop1.processor = 'Intel Core i7'

jsonStr = json.dumps(laptop1.__dict__)

print(jsonStr)

### Convert properties of python class object to json string

import json

class Laptop:
    def __init__(self, name, processor, hdd, ram, cost):
        self.name = name
        self.processor = processor
        self.hdd = hdd
        self.ram = ram
        self.cost = cost

laptop1 = Laptop('Dell Alienware', 'Intel core I4', 512, 8, 2500.98)
jsonStr = json.dumps(laptop1.__dict__)
print(jsonStr)

######
