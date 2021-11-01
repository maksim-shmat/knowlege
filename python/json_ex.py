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

######
