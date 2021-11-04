"""JSON about."""

######1 read .json

import json

with open('jill.json', 'r', encoding = 'utf-8') as json_file:
    a = json_file.read()
    b = json_file.read()
    print('a: ', a)
    print('b: ', b)

######4 Create json string from dictionary

import json

dictionary = {'a': 34, 'b': 61, 'c': 82}
jsonString = json.dumps(dictionary, indent=4)
print(jsonString)

### Create json string from list

import json

myList1 = [{'a': 54}, {'b': 41, 'c': 87}]
jsonString1 = json.dumps(myList1, indent=4)  # json.dumps! not .dump!
print(jsonString1)

### Create json string from tuple

import json

myTuple = ({'a': 54}, {'b': 42, 'c':38})
jsonString2 = json.dumps(myTuple, indent=4)
print(jsonString2)

######5 Parse json string to list

import json

jsonStr = '[{"name": "Testla", "age": 2352, "city": "New Orlan"}, {"name": "Testla", "age": 23, "city": "Radomption"}]'

pythonObj = json.loads(jsonStr)
print(type(pythonObj))
print(type(pythonObj[0]))
city = pythonObj[1]['city']
print(city)

######6 Convert Class object to json string

import json

class Laptop:
    name = 'My Laptop'
    processor = 'Intel Core'

laptop1 = Laptop()
laptop1.name = 'Dell Alienware'
laptop1.processor = 'Intel Core i7'

jsonStr4 = json.dumps(laptop1.__dict__)

print(jsonStr4)

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
jsonStr5 = json.dumps(laptop1.__dict__)
print(jsonStr5)

######7 Convert tuple to json string

import json

mytuple4 = ("python", "json", "postgreshechka")
jsonStr7 = json.dumps(mytuple4)
print(jsonStr7)

### Convert tuple with different datatypes to json string

import json

mytuple5 = ("python", "json", 22, 23.04)
jsonStr8 = json.dumps(mytuple5)
print(jsonStr8)
jsonArr = json.loads(jsonStr8)
print(jsonArr[2])

######8 Convert csv to json

import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        for row in csvReader:
            jsonArray.append(row)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

csvFilePath = r'data.csv'
jsonFilePath = r'data.json'
csv_to_json(csvFilePath, jsonFilePath)

######
