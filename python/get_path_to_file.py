import os.path
old_path = os.path.abspath('jill.txt')
print(old_path)
new_path = '{}.{}'.format(old_path, "old")
print(new_path)

import pathlib
path = pathlib.Path('jill.py')
abs_path = path.resolve()
print(abs_path)
new_path = str(abs_path) + ".old"
print(new_path)
