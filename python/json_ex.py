"""JavaScript Object Notation about."""

#1 encoding/decoding with JSON
'''
import json


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {
                    '_meta': '_complex',
                    'num': [obj.real, obj.imag],
            }
        return json.JSONEncoder.default(self, obj)

data = {
        'an_int': 42,
        'a_float': 3.14159265,
        'a_complex': 3 + 4j,
}

json_data = json.dumps(data, cls=ComplexEncoder)
print(json_data)

def object_hook(obj):
    try:
        if obj['_meta'] == '_complex':
            return complex(*obj['num'])
    except (KeyError, TypeError):
        return obj

data_out = json.loads(json_data, object_hook=object_hook)
print(data_out)


{"an_int": 42, "a_float": 3.14159265, "a_complex": {"_meta": "_complex", "num": [3.0, 4.0]}}
{'an_int': 42, 'a_float': 3.14159265, 'a_complex': (3+4j)}
'''
#2 json datetime

import json
from datetime import datetime, timedelta, timezone


now = datetime.now()
now_tz = datetime.now(tz=timezone(timedelta(hours=1)))

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            try:
                off = obj.utcoffset().seconds
            except AttributeError:
                off = None

            return {
                    '_meta': '_datetime',
                    'data': obj.timetuple() [:6] + (obj.microsecond, ),
                    'utcoffset': off,
            }
        return json.JSONEncoder.default(self, obj)

data = {
        'an_int': 42,
        'a_float': 3.14159265,
        'a_datetime': now,
        'a_datetime_tz': now_tz,
}

json_data = json.dumps(data, cls=DatetimeEncoder)
print(json_data)

def object_hook(obj):
    try:
        if obj['_meta'] == '_datetime':
            if obj['utcoffset'] is None:
                tz = None
            else:
                tz = timezone(timedelta(seconds=obj['utfcoffset']))
            return datetime(*obj['data'], tzinfo=tz)
    except (KeyError, TypeError):
        return obj

data_out = json.loads(json_data, object_hook=object_hook)


{"an_int": 42, "a_float": 3.14159265, "a_datetime": {"_meta": "_datetime", "data": [2023, 8, 1, 4, 53, 34, 550864], "utcoffset": null}, "a_datetime_tz": {"_meta": "_datetime", "data": [2023, 8, 1, 2, 53, 34, 550878], "utcoffset": 3600}}
