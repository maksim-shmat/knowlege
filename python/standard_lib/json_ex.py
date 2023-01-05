"""JSON about."""

######1 read .json

import json
'''
with open('jill.json', 'r', encoding = 'utf-8') as json_file:
    a = json_file.read()
    b = json_file.read()
    print('a: ', a)
    print('b: ', b)

### read json file

import json

fileObject1 = open("jill.json", "r")
jsonContent1 = fileObject1.read()
aList1 = json.loads(jsonContent1)
print(aList1)

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
jsonFilePath = r'jill.json'
csv_to_json(csvFilePath, jsonFilePath)

######9 json object to dictionary

import json

jsonString = '{"a": 54, "b": 28}'
aDict = json.loads(jsonString)
print(aDict)
print(aDict['a'])
print(aDict['b'])
print()

### json nested object to dictionary

import json

jsonString = '{"a": 54, "b": {"c": 87}}'
aDict = json.loads(jsonString)
print(aDict)
print(aDict['a'])
print(aDict['b'])
print(aDict['b']['c'])
print()

######10 convert json array string to python list

import json

jsonStr = '[{"a": 1, "b": 2}, {"c": 3, "d": 4}]'
aList = json.loads(jsonStr)
print(aList[0]['b'])

### convert json array of arrays string to python list

import json

jsonStr = '[[{"a": 1, "b": 2}], [{"c": 3, "d": 4}]]'
aList = json.loads(jsonStr)
print(aList[0][0])
print(type(aList))

######11 convert pytnon list of lists to json

import json

aList = [[{'a': 1, 'b': 2}], [{'c': 3, 'd': 4}]]
jsonStr = json.dumps(aList)
print(jsonStr)
print(type(jsonStr))

######12 Write json (object) to file

aDict = {"a": 54, "b":87}
jsonString = json.dumps(aDict)
jsonFile = open("jill.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

### Write json (list of object) to file

import json

aList = [{"a": 54, "b": 87}, {"c": 81, "d": 63}, {"e": 17, "f": 39}]
jsonString = json.dumps(aList)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

##13 write json

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'jill.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

##14 Save/Load

import json

def get_stored_username():
    """Get saved username, if it exists."""

    filename = 'jill.json'
    try:
        with open(filename) as f:
            username = json.load(f)  # load if name save lately
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Asc now name of user."""
    username = input("What is your name? ")  # in another case asc name
    filename = 'jill.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
    
def greet_user():
    """Greeting user for his name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
'''
#1 json simple types (str, int, float, list, tuple, dict)

import json

'''
data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA:', repr(data))

data_string = json.dumps(data)
print('JSON:', data_string)

RESULTS:
DATA: [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
JSON: [{"a": "A", "b": [2, 4], "c": 3.0}]
'''

#2 json simple types decode with change types not liberately

import json

'''
data =[{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA  :', data)

data_string = json.dumps(data)
print('ENCODED:', data_string)

decoded = json.loads(data_string)
print('DECODED:', decoded)

print('ORIGINAL:', type(data[0]['b']))
print('DECODED :', type(decoded[0] ['b']))

RESULTS:
DATA  : [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
ENCODED: [{"a": "A", "b": [2, 4], "c": 3.0}]
DECODED: [{'a': 'A', 'b': [2, 4], 'c': 3.0}]
ORIGINAL: <class 'tuple'>
DECODED : <class 'list'>
'''

#3 json sort keys

import json

'''
data = [{'a': 'A', 'b':(2, 4), 'c': 3.0}]
print('DATA:', repr(data))

unsorted = json.dumps(data)
print('JSON:', json.dumps(data))
print('SORT:', json.dumps(data, sort_keys=True))

first = json.dumps(data, sort_keys=True)
second = json.dumps(data, sort_keys=True)

print('UNSORTED MATCH:', unsorted == first)
print('SORTED MATCH  :', first == second)

RESULTS:
DATA: [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
JSON: [{"a": "A", "b": [2, 4], "c": 3.0}]
SORT: [{"a": "A", "b": [2, 4], "c": 3.0}]
UNSORTED MATCH: True
SORTED MATCH  : True
'''

#4 json indent

import json

'''
data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA:', repr(data))

print('NORMAL:', json.dumps(data, sort_keys=True))
print('INDENT:', json.dumps(data, sort_keys=True, indent=2))

RESULTS:
DATA: [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
NORMAL: [{"a": "A", "b": [2, 4], "c": 3.0}]
INDENT: [
  {
    "a": "A",
    "b": [
      2,
      4
    ],
    "c": 3.0
  }
]
'''

#5 json compact encoding

import json

'''
data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]

print('DATA:', repr(data))

print('repr(data)        :', len(repr(data)))

plain_dump = json.dumps(data)
print('dumps(data))      :', len(plain_dump))

small_indent = json.dumps(data, indent=2)
print('dumps(data, indent=2) :', len(small_indent))

with_separators = json.dumps(data, separators=(',', ':'))
print('dumps(data, separators):', len(with_separators))

RESULTS:
DATA: [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
repr(data)        : 35
dumps(data))      : 35
dumps(data, indent=2) : 73
dumps(data, separators): 29
'''

#6 json skipkeys, that it use string as keys (string as keys, Karl!)

import json

'''
data = [{'a': 'A', 'b': (2, 4),'c': 3.0, ('d',): 'D tuple'}]

print('First attempt')
try:
    print(json.dumps(data))
except TypeError as err:
    print('ERROR:', err)

print()
print('Second attempt')
print(json.dumps(data, skipkeys=True))

RESULTS:
First attempt
ERROR: keys must be str, int, float, bool or None, not tuple

Second attempt
[{"a": "A", "b": [2, 4], "c": 3.0}]
'''

#7 json myobj
'''
class MyObj:

    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return '<MyObj({})>'.format(self.s)

#7.1 json dump default

import json
import json_myobj


obj = json_myobj.MyObj('instance value goes here')

print('First attempt')
try:
    print(jaon.dumps(obj))
except TypeError as err:
    print('ERROR:', err)

def convert_to_builtin_type(obj):
    print('default(', repr(obj), ')')
    # Change object in dict
    d = {
            '__class__':obj.__class__.__name__,
            '__module__':obj.__module__,
    }
    d.update(obj.__dict__)
    return d

print()
print('With default')
print(json.dumps(obj, default=convert_to_builtin_type)))
'''

#7.2 json load object hook

import json

'''
def dict_to_object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        print('MODULE:', module.__name__)
        class_ = getattr(module, class_name)
        print('CLASS:', class_)
        args = {
                key: value
                for key, value in d.items()
        }
        print('INSTANCE ARGS:', args)
        inst = class_(**args)
    else:
        inst = d
    return inst

encoded_object = """
[{"s": "instance value goes here",
  "__module__": "json_myobj", '__class__": "MyObj"}]
  """

myobj_instance = json.loads(
        encoded_object,
        object_hook=dict_to_object,
)
print(myobj_instance)
'''

#8 json encoder iterable

import json

'''
encoder = json.JSONEncoder()
data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]

for part in encoder.iterencode(data):
    print('PART:', part)

RESULTS:
PART: [
PART: {
PART: "a"
PART: : 
PART: "A"
PART: , 
PART: "b"
PART: : 
PART: [2
PART: , 4
PART: ]
PART: , 
PART: "c"
PART: : 
PART: 3.0
PART: }
PART: ]
'''

#9 json encoder default

import json
import json_myobj  # from #7

'''
class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        print('default(', repr(obj), ')')
        # change object to dict
        d = {
                '__class__':__class__.__name__,
                '__module__':obj.__module__,
        }
        d.update(obj.__dict__)
        return d

obj = json_myobj.MyObj('internal date')
print(obj)
print(MyEncoder().encode(obj))
'''

#10 json decoder object hook

import json

'''
class MyDecoder(json.JSONDecoder):

    def __init__(self):
        json.JSONDecoder.__init__(
                self,
                object_hook=self.dict_to_object,
        )

    def dict_to_object(self, d):
        if '__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            print('MODULE:', module.__name__)
            class_ = getattr(module, class_name)
            print('CLASS:', class_)
            args = {
                    key: value
                    for key, value in d.items()
            }
            print('INSTANCE ARGS:', args)
            inst = class_(**args)
        else:
            inst = d
        return inst


encodede_object = """
[{"s": "instance value goes here",
  "__module__": "json_myobj", "__class__": "MyObj"}]
"""

myobj_instance = MyDecoder().decode(encoded_object)
print(myobj_instance)
'''
