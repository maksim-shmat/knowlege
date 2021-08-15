"""examples with [as]."""

# create alias for module

import numpy as np

a = np.array([4, 5, 3, 7])
print(a)

###### create alias for sub-module

from numpy.lib import scimath as smath

print(smath.log(10))

###### create alias for module

with open('jill.txt') as myfile:
    fileContents = myfile.read()

print(fileContents)

###### as in except clause

try:
    with open('no_file.txt') as myfile:
        fileContents = myfile.read()
except FileNotFoundError as ex:
    print(ex)

######
