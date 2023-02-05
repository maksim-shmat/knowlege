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

#2 
