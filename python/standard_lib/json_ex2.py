"""json about."""

#1 json dump file

import io
import json

'''
data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]

f = io.StringIO()
json.dump(data, f)

print(f.getvalue())

RESULTS:
[{"a": "A", "b": [2, 4], "c": 3.0}]
'''

#2 json load file

import io
import json

'''
f = io.StringIO('[{"a": "A", "c": 3.0, "b": [2, 4]}]')
print(json.load(f))

RESULTS:
[{'a': 'A', 'c': 3.0, 'b': [2, 4]}]
'''    

#3 json mixed data

import json

'''
decoder = json.JSONDecoder()

def get_decoded_and_remainder(input_data):
    obj, end = decoder.raw_decode(input_data)
    remaining = input_data[end:]
    return (obj, end, remaining)


encoded_object = '[{"a": "A", "c": 3.0, "b": [2, 4]}]'
extra_text = 'This text is not JSON.'

print('JSON first:')
data = ' '.join([encoded_object, extra_text])
obj, end, remaining = get_decoded_and_remainder(data)

print('Object             :', obj)
print('End of parsed input:', end)
print('Remaining text     :', repr(remaining))

print()
print('JSON embeded:')
try:
    data = ' '.join([extra_text, encoded_object, extra_text])
    obj, end, remaining = get_decoded_and_remainder(data)
except ValueError as err:
    print('ERROR:', err)

RESULTS:
JSON first:
Object             : [{'a': 'A', 'c': 3.0, 'b': [2, 4]}]
End of parsed input: 35
Remaining text     : ' This text is not JSON.'

JSON embeded:
ERROR: Expecting value: line 1 column 1 (char 0)
'''
