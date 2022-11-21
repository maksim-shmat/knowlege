''' stat(), lstat() == os.stat(), os.lstat().'''

import pathlib
import sys
import time

print()
if len(sys.argv) == 1:
    filename = __file__
else:
    filename = sys.argv[1]

p = pathlib.Path(filename)
stat_info = p.stat()

print('{}:'.format(filename))
print('  Size:', stat_info.st_size)
print('  Permissions:', oct(stat_info.st_mode))
print('  Owner:', stat_info.st_uid)
print('  Device:', stat_info.st_dev)
print('  Created      :', time.ctime(stat_info.st_ctime))
print('  Last modified:', time.ctime(stat_info.st_mtime))
print('  Last accessed:', time.ctime(stat_info.st_atime))

'''RESULTS:
/home/jack/django2/knowlege/python/tests_ex/test_stat.py:
  Size: 588
  Permissions: 0o100664
  Owner: 1001            # return owner number but it is not the name
  Device: 66307
  Created      : Mon Oct 17 04:16:46 2022
  Last modified: Mon Oct 17 04:16:46 2022
  Last accessed: Mon Oct 17 04:16:54 2022
'''

