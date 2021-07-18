"""JSON about."""

# read .json

import json

with open('jill.json', 'r', encoding = 'utf-8') as json_file:
    a = json_file.read()
    b = json_file.read()
    print('a: ', a)
    print('b: ', b)

###### write to json (dump)

import json
outfile = open("mars_data_01.json", "w")
json.dump(weather, outfile)
outfile.close()
json.dumps(weather)

from pprint import pprint as pp

print(json.dumps(weather, indent=2))

###### go in json in dict for safe

outfile = open("mars_data.json", 'w')
weather_obj = {"reports": weather_list, "count": 2}
json.dump(weather, outfile)
outfile.close()

### load
with open("mars_data.json") as infile:
    weather_obj = json.load(infile)

######
