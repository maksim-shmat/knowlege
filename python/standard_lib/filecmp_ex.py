"""filecmp about."""

#1 mkexamples

import os

def mkfile(filename, body=None):
    with open(filename, 'w') as f:
        f.write(body or filename)
    return


def make_example_dir(top):
    if not os.path.exists(top):
        os.mkdir(top)
    curdir = os.getcwd()
    os.chdir(top)

#    os.mkdir('dir1')
#    os.mkdir('dir2')

    mkfile('dir1/file_only_in_dir1')
    mkfile('dir2/file_only_in_dir2')

#    os.mkdir('dir1/dir_only_in_dir1')
#    os.mkdir('dir2/dir_only_in_dir2')

#    os.mkdir('dir1/common_dir')
#    os.mkdir('dir2/common_dir')

    mkfile('dir1/common_file', 'this file is the same')
    mkfile('dir2/common_file', 'this file is the same')

    mkfile('dir1/file_in_dir1', 'This is a file in dir1')
 #   os.mkdir('dir2/file_in_dir1')

    os.chdir(curdir)
    return

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__) or os.getcwd())
    make_example_dir('example')
    make_example_dir('example/dir1/common_dir')
    make_example_dir('example/dir2/common_dir')

#2 cmp == compare

import filecmp

print('common_file:', end=' ')
print(filecmp.cmp('example/dir1/common_file',
                  'example/dir2/common_file'),
                  end=' ')
print(filecmp.cmp('example/dir1/common_file',
                  'example/dir2/common_file',
                  shallow=False))
print('not_the_same:', end=' ')
print(filecmp.cmp('example/dir1/not_the_same',
                  'example/dir2/not_the_same',
                  shallow=False))
print('identical   :', end=' ')
print(filecmp.cmp('example/dir1/file_only_in_dir1',
                  'example/dir1/file_only_in_dir1'),
                  end=' ')
print(filecmp.cmp('example/dir1/file_only_in_dir1',
                  'example/dir1/file_only_in_dir1',
                  shallow=False))

'''RESULTS:
common_file: True True
not_the_same: False
identical   : True True
'''

#3 cmpfiles

import filecmp
import os

# compare elements exists on both directories

d1_contents = set(os.listdir('example/dir1'))
d2_contents = set(os.listdir('example/dir2'))
common = list(d1_contents & d2_contents)
common_files = [
        f
        for f in common
        if os.path.isfile(os.path.join('example/dir1', f))
]
print('Common files:', common_files)

# Compare dirs

match, mismatch, errors = filecmp.cmpfiles(
        'example/dir1',
        'example/dir2',
        common_files,
)
print('Match     :', match)
print('Mismatch  :', mismatch)
print('Errors    :', errors)

'''RESULTS:
Common files: ['not_the_same', 'common_file', 'file_in_dir1']
Match     : ['common_file']
Mismatch  : ['not_the_same', 'file_in_dir1']
Errors    : []
'''

#4 dircmp, report()

import filecmp

dc = filecmp.dircmp('example/dir1', 'example/dir2')
dc.report()

'''RESULTS:
diff example/dir1 example/dir2
Only in example/dir1 : ['dir_only_in_dir1', 'file_only_in_dir1']
Only in example/dir2 : ['dir_only_in_dir2', 'file_only_in_dir2']
Identical files : ['common_file']
Differing files : ['not_the_same']
Common subdirectories : ['common_dir']
Common funny cases : ['file_in_dir1']
'''

#5 dircmp, report_full_closure()

import filecmp

print()
dc = filecmp.dircmp('example/dir1', 'example/dir2')
dc.report_full_closure()

'''RESULTS:
diff example/dir1/common_dir example/dir2/common_dir
Common subdirectories : ['dir1', 'dir2']

diff example/dir1/common_dir/dir1 example/dir2/common_dir/dir1
Identical files : ['common_file', 'file_in_dir1', 'file_only_in_dir1']
Common subdirectories : ['common_dir', 'dir_only_in_dir1']

diff example/dir1/common_dir/dir1/common_dir example/dir2/common_dir/dir1/common_dir

diff example/dir1/common_dir/dir1/dir_only_in_dir1 example/dir2/common_dir/dir1/dir_only_in_dir1

diff example/dir1/common_dir/dir2 example/dir2/common_dir/dir2
Identical files : ['common_file', 'file_only_in_dir2']
Common subdirectories : ['common_dir', 'dir_only_in_dir2', 'file_in_dir1']

diff example/dir1/common_dir/dir2/common_dir example/dir2/common_dir/dir2/common_dir

diff example/dir1/common_dir/dir2/dir_only_in_dir2 example/dir2/common_dir/dir2/dir_only_in_dir2

diff example/dir1/common_dir/dir2/file_in_dir1 example/dir2/common_dir/dir2/file_in_dir1
'''

#6 dircmp list

import filecmp
import pprint

dc = filecmp.dircmp('example/dir1', 'example/dir2')
print('Left:')
pprint.pprint(dc.left_list)

print('\nRight:')
pprint.pprint(dc.right_list)

'''RESULTS:
Left:
['common_dir',
 'common_file',
 'dir_only_in_dir1',
 'file_in_dir1',
 'file_only_in_dir1',
 'not_the_same']

Right:
['common_dir',
 'common_file',
 'dir_only_in_dir2',
 'file_in_dir1',
 'file_only_in_dir2',
 'not_the_same']
'''

#7 dircmp list filter, default filtering RCS, CVS and tags

import filecmp
import pprint

dc = filecmp.dircmp('example/dir1', 'example/dir2',
                    ignore=['common_file'])

print('Left:')
pprint.pprint(dc.left_list)

print('\nRight:')
pprint.pprint(dc.right_list)

'''RESULTS:
Left:
['common_dir',
 'dir_only_in_dir1',
 'file_in_dir1',
 'file_only_in_dir1',
 'not_the_same']

Right:
['common_dir',
 'dir_only_in_dir2',
 'file_in_dir1',
 'file_only_in_dir2',
 'not_the_same']
'''

#8 dircmp membership

import filecmp
import pprint

dc = filecmp.dircmp('example/dir1', 'example/dir2')
print('Common:')
pprint.pprint(dc.common)

print('\nLeft:')
pprint.pprint(dc.left_only)

print('\nRight:')
pprint.pprint(dc.right_only)

'''RESULTS:
Common:
['common_dir', 'common_file', 'file_in_dir1', 'not_the_same']

Left:
['dir_only_in_dir1', 'file_only_in_dir1']

Right:
['dir_only_in_dir2', 'file_only_in_dir2']
'''

#9 dircmp common

import filecmp
import pprint

dc = filecmp.dircmp('example/dir1', 'example/dir2')
print('Common:')
pprint.pprint(dc.common)

print('\nDirectories:')
pprint.pprint(dc.common_dirs)

print('\nFiles:')
pprint.pprint(dc.common_files)

print('\nFunny:')
pprint.pprint(dc.common_funny)

'''RESULTS:
Common:
['common_dir', 'common_file', 'file_in_dir1', 'not_the_same']

Directories:
['common_dir']

Files:
['common_file', 'not_the_same']

Funny:
['file_in_dir1']
'''

#10 dircmp diff

import filecmp

print()
dc = filecmp.dircmp('example/dir1', 'example/dir2')
print('Same     :', dc.same_files)
print('Different:', dc.diff_files)
print('Funny    :', dc.funny_files)

'''RESULTS:
Same     : ['common_file']
Different: ['not_the_same']
Funny    : []
'''

#11 subdirs

import filecmp

print()
dc = filecmp.dircmp('example/dir1', 'example/dir2')
print('Subdirectories:')
print(dc.subdirs)

'''RESULTS:
Subdirectories:
{'common_dir': <filecmp.dircmp object at 0x7f56bd2bb880>}
'''
