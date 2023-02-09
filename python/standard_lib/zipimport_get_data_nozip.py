"""Find dir and make data file."""

import os
import example_package


pkg_dir = os.path.dirname(example_package.__file__)
data_filename = os.path.join(pkg_dir, 'RADME.txt')

print(data_filename, ':')
print(open(data_filename, 'r').read())
