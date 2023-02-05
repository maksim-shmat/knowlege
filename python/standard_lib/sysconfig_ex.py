"""sysconfig about."""

#1 sysconfig get config vars

import sysconfig

'''
config_values = sysconfig.get_config_vars()
print('Found {} configuration settings'.format(
    len(config_values.keys())))

print('\nSome highlights:\n')

print(' Installation prefixes:')
print(' prefix={prefix}'.format(**config_values))
print(' exec_prefix={exec_prefix}'.format(**config_values))

print('\n Version info:')
print(' py_version={py_version}'.format(**config_values))
print(' py_version_short={py_version_short}'.format(
    **config_values))
print(' py_version_nodot={py_version_nodot}'.format(
    **config_values))

print('\n Base directories:')
print('  base={base}'.format(**config_values))
print('  platbase={platbase}'.format(**config_values))
print('  userbase={userbase}'.format(**config_values))
print('  srcdir={srcdir}'.format(**config_values))

print('\n Compiler and linker flags:')
print(' LDFLAGS={LDFLAGS}'.format(**config_values))
print(' BASECFLAGS={BASECFLAGS}'.format(**config_values))
print(' Py_ENABLE_SHARED={Py_ENABLE_SHARED}'.format(
    **config_values))

RESULTS:
Found 725 configuration settings

Some highlights:

 Installation prefixes:
 prefix=/usr
 exec_prefix=/usr

 Version info:
 py_version=3.10.6
 py_version_short=3.10
  py_version_nodot=310

 Base directories:
  base=/usr
  platbase=/usr
  userbase=/home/jack/.local
  srcdir=/usr/lib/python3.10/config-3.10-x86_64-linux-gnu

 Compiler and linker flags:
 LDFLAGS=-Wl,-Bsymbolic-functions      -g -fwrapv -O2   
 BASECFLAGS=-Wno-unused-result -Wsign-compare
 Py_ENABLE_SHARED=1
'''

#2 sysconfig get confgig vars by name

import sysconfig

'''
bases = sysconfig.get_config_vars('base', 'platbase', 'userbase')
print('Base directories:')
for b in bases:
    print('  ', b)

RESULTS:
Base directories:
   /usr
   /usr
   /home/jack/.local
'''

#3 sysconfig get config var

import sysconfig

'''
print('User base directory:',
        sysconfig.get_config_var('userbase'))
print('Unknown variable :',
        sysconfig.get_config_var('NoSuchVariable'))

RESULTS:
User base directory: /home/jack/.local
Unknown variable : None
'''

#4 sysconfig get scheme names

import sysconfig

'''
for name in sysconfig.get_scheme_names():
    print(name)

RESULTS:
deb_system
nt
nt_user
osx_framework_user
posix_home
posix_local
posix_prefix
posix_user
'''

#5 sysconfig get path names

import sysconfig

'''
for name in sysconfig.get_path_names():
    print(name)

RESULTS:
stdlib
platstdlib
purelib
platlib
include
scripts
data
'''

#6 sysconfig get paths

import sysconfig
import pprint
import os

'''
for scheme in ['posix_prefix', 'posix_user']:
    print(scheme)
    print('=' * len(scheme))
    paths = sysconfig.get_paths(scheme=scheme)
    prefix = os.path.commonprefix(paths.values())
    print('prefix = {}\n'.format(prefix))
    for name, path in sorted(paths.items()):
        print('{}\n .{}'.format(name, path[len(prefix):]))
    print()

RESULTS:
posix_prefix
============
Traceback (most recent call last):
  File "<stdin>", line 143, in <module>
  File "/usr/lib/python3.10/genericpath.py", line 76, in commonprefix
    if not isinstance(m[0], (list, tuple)):
TypeError: 'dict_values' object is not subscriptable

shell returned 1
'''

#7 sysconfig get path

import sysconfig
import pprint

'''
for scheme in ['posix_prefix', 'posix_user']:
    print(scheme)
    print('=' * len(scheme))
    print('purelim =', sysconfig.get_path(name='purelib',
                                          scheme=scheme))
    print()

RESULTS:
posix_prefix
============
purelim = /usr/lib/python3.10/site-packages

posix_user
==========
purelim = /home/jack/.local/lib/python3.10/site-packages
'''
#8 sysconfig get platform

import sysconfig

'''
print(sysconfig.get_platform())

RESULTS:
linux-x86_64
'''

#9 sysconfig get python version

import sysconfig
import sys

'''
print('sysconfig.get_python_version():',
        sysconfig.get_python_version())
print('\nsys.version_info:')
print(' major       :', sys.version_info.major)
print(' minor       :', sys.version_info.minor)
print(' micro       :', sys.version_info.micro)
print(' releaselevel:', sys.version_info.releaselevel)
print(' serial      :', sys.version_info.serial)

RESULTS:
sysconfig.get_python_version(): 3.10

sys.version_info:
 major       : 3
 minor       : 10
 micro       : 6
 releaselevel: final
 serial      : 0
'''
