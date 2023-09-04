"""pdb about."""

#1
import pdb

d = {'first': 'v1', 'second': 'v2', 'fourth': 'v4'}

keys = ('first', 'second', 'third', 'fouth')  # 'third' is left for debuging

def do_something_with_value(value):
    print(value)

for key in keys:
    do_something_with_value(d[key])

breackpoint()

