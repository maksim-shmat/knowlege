"""import about."""

#1 importlib suffixes

import importlib.machinery

'''
SUFFIXES = [
        ('Source:', importlib.machinery.SOURCE_SUFFIXES),
        ('Debug:',
            importlib.machinery.DEBUG_BYTECODE_SUFFIXES),
        ('Optimized:',
            importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES),
        ('Bytecode:', importlib.machinery.BYTECODE_SUFFIXES),
        ('Extension:', importlib.machinery.EXTENSION_SUFFIXES),
]


def main():
    tmpl = '{:<10}  {}'
    for name, value in SUFFIXES:
        print(tmpl.format(name, value))

if __name__ == '__main__':
    main()

RESULTS:
Source:     ['.py']
Debug:      ['.pyc']
Optimized:  ['.pyc']
Bytecode:   ['.pyc']
Extension:  ['.cpython-310-x86_64-linux-gnu.so', '.abi3.so', '.so']
'''

#2 importlib import module

import importlib
'''
m1 = importlib.import_module('example.submodule')
print(m1)

m2 = importlib.import_module('.submodule', package='example')
print(m2)

print(m1 is m2)
'''
#3 importlib import module error

import importlib

'''
try:
    importlib.import_module('example.nosuchmodule')
except ImportError as err:
    print('Error:', err)
'''

#4 importlib reload

import importlib

'''
m1 = importlib.import_module('example.submodule')
print(m1)

m2 = importlib.reload(m1)
print(m1 is m2)
'''

#5 importlib find loader

import importlib

'''
loader = importlib.find_loader('example')
print('Loader:', loader)

m = loader.load_module()
print('Module:', m)

RESULTS:
<stdin>:74: DeprecationWarning: Deprecated since Python 3.4 and slated for removal in Python 3.12; use importlib.util.find_spec() instead
Loader: <_frozen_importlib_external.SourceFileLoader object at 0x7f449c5b11b0>
Module: <module 'example' from '/home/jack/django2/knowlege/python/standard_lib/example.py'>
'''

#6 importlib submodule

import importlib

'''
pkg_loader = importlib.find_loader('example')
pkg = pkg_loader.load_module()

loader = importlib.find_loader('submodule', pkg.__path__)
print('Loader:', loader)

m = loader.load_module()
print('Module:', m)

RESULTS:
<stdin>:91: DeprecationWarning: Deprecated since Python 3.4 and slated for removal in Python 3.12; use importlib.util.find_spec() instead
Traceback (most recent call last):
  File "<stdin>", line 94, in <module>
AttributeError: module 'example' has no attribute '__path__'. Did you mean: '__name__'?
'''
