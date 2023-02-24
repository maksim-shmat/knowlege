"""Find dir and make data file."""

#1 import from filesystem

import os
import example_package

'''
pkg_dir = os.path.dirname(example_package.__file__)
data_filename = os.path.join(pkg_dir, 'RADME.txt')

print(data_filename, ':')
print(open(data_filename, 'r').read())
'''

#2 import from ZIP archive

import sys
'''
sys.path.insert(0, 'zipimport_example.zip')

import os
import example_package
print(example_package.__file__)
data = example_package.__loader__.get_data(
        'example_package/README.txt')
print(data.decode('utf-8'))
'''
