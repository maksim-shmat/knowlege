"""Check file system."""

#1 os listdir

import os
import sys

'''
print(os.listdir(sys.argv[1]))

'''

#2 os walk

import os
import sys

'''
if len(sys.argv) == 1:
    root = '/tmp'
else:
    root = sys.argv[1]

for dir_name, sub_dirs, files in os.walk(root):
    print(dir_name)
    # Ending dir names with /
    sub_dirs = [n + '/' for n in sub_dirs]
    # Create common list of subdirs and files
    contents = sub_dirs + files
    contents.sort()
    # Show content
    for c in contents:
        print('  {}'.format(c))
    print()
'''

#3 os scandir for more details

import os
import sys

'''
for entry in os.scandir(sys.argv[1]):
    if entry.is_dir():
        typ = 'dir'
    elif entry.is_file():
        typ = 'file'
    elif entry.is_symlink():
        typ = 'link'
    else:
        typ = 'unknown'
    print('{name} {typ}'.format(
        name=entry.name,
        typ=typ,
    ))
'''

#4 os stat

import os
import sys
import time

'''
if len(sys.argv) == 1:
    filename = __file__
else:
    filename = sys.argv[1]

stat_info = os.stat('jill.txt')

print('os.stat({}):'.format('jill.txt'))
print('Size:', stat_info.st_size)
print('Permissions:', oct(stat_info.st_mode))
print('Owner:', stat_info.st_uid)
print('Device:', stat_info.st_dev)
print('Created:', time.ctime(stat_info.st_ctime))
print('Last modified:', time.ctime(stat_info.st_mtime))
print('Last accessed:', time.ctime(stat_info.st_atime))

RESULTS:
os.stat(jill.txt):
Size: 3860
Permissions: 0o100664
Owner: 1001
Device: 66307
Created: Sun Aug 28 19:29:32 2022
Last modified: Sun Aug 28 19:29:32 2022
Last accessed: Wed Aug 31 04:59:26 2022
'''

#5 os stat chmod for change permissions

import os
import stat

'''
filename = 'os_stat_chmod_example.txt'
if os.path.exists(filename):
    os.unlink(filename)
with open(filename, 'wt') as f:
    f.write('contents')

# check permissions with stat_existing_permissions = stat.S_IMODE(os.stat(filename).st_mode)
existing_permissions = stat.S_IMODE(os.stat(filename).st_mode)

if not os.access(filename, os.X_OK):
    print('Adding execute permission')
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print('Removing execute permission')
    # Use XOR operation for remove access to execute
    new_permissions = existing_permissions ^ stat.S_IXUSR

os.chmod(filename, new_permissions)
'''

#6 os access

import os

'''
print('Testing:', __file__)
print('Exists:', os.access(__file__, os.F_OK))
print('Readable:', os.access(__file__, os.R_OK))
print('Writable:', os.access(__file__, os.W_OK))
print('Executable:', os.access(__file__, os.X_OK))
'''

#7 
