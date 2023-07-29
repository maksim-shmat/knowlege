"""Check content of directory."""

#1 listing
'''
import os


with os.scandir('.') as it:
    for entry in it:
        print(
                entry.name, entry.path,
                'File' if entry.is_file() else 'Folder'
        )
'''
#2 walking

import os


for root, dirs, files in os.walk('.'):
    print(os.path.abspath(root))
    if dirs:
        print('Directories:')
        for dir_ in dirs:
            print(dir_)
        print()
    if files:
        print('Files:')
        for filename in files:
            print(filename)
        print()
