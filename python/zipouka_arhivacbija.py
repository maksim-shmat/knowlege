import datetime
import pathlib
import zipfile

FILE_PATTERN = "*.txt"
ARCHIVE = "archive"

if __name__ == '__main__':
    date_string = datetime.date.today().strftime("%Y-%m-%d")

    cur_path = pathlib.Path(".")
    paths = cur_path.glob(FILE_PATTERN)

    zip_file_path = cur_path.joinpath(ARCHIVE, date_string + ".zip")
    zip_file = zipfile.ZipFile(str(zip_file_path), "w")
    for path in paths:
        zip_file.write(str(path))
        path.unlink()

# another example. Not use call os, use zipfile()

import os
import time

source = ['"Files for backup"', 'And_more']  # make a list for backup
target_dir = <path>  # dir for backups

today = target_dir + os.sep + time.strftime('%Y%m%d')  # date is name for archive
now = time.strftime('%H%M%S')

comment = input('Enter comment: ')  # add comment to zip archive
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today = os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
if not os.path.exists(today):  # make a dir if it's not exist
    os.mkdir(today)
print('Directory created succesfully', today)

target = today + os.set + now + '.zip'  # name of zip file

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source)) # zipped files
if os.system(zip_command) == 0:
    print('Backup copy created', target)
else:
    print('Backup copy FAILED, KARL?')


