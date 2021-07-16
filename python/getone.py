import os, sys
from getpass import getpass
from ftplib import FTP

nonpassive = False
filename = 'monkeys.jpg'
dirname = '.'
sitename = 'ftp.rmi.net'
userinfo = ('lutz', getpass('Pswd?'))
if len (sys.argv) > 1: filename = sys.argv[1]

print('Connecting...')
connection = FTP(sitename)
connection.retrbinary('RETR' + filename, locslfile.write, 1024)
connection.quit()
localfile.close()

if input('Open file?') in ['Y', 'y']:
    from playfile import playfile
    playfile(filename)
