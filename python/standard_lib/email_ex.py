"""email about."""

#1 mailbox mbox create

import mailbox
import email.utils

'''i
from_addr = email.utils.formataddr(('Author',
                                    'autor@example.com'))
to_addr = email.utils.formataddr(('Recipient',
                                 'recipient@example.com'))

payload = """This is the body.
From (will not be escaped).
There are 3 lines.
"""

mbox = mailbox.mbox('example.mbox')
mbox.lock()
try:
    msg = mailbox.mboxMessage()
    msg.set_unixfrom('author Sat Feb 11 02:01:33 2023')
    msg['From'] = from_addr
    msg['Subject'] = 'Sample message 1'
    msg.set_payload(payload)
    mbox.add(msg)
    mbox.flush()

    msg = mailbox.mboxMessage()
    msg.set_unixfrom('author')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Sample message 2'
    msg.set_payload('This is the second body.\n')
    mbox.add(msg)
    mbox.flush()
finally:
    mbox.unlock()

print(open('example.mbox', 'r').read())

RESULTS:
From MAILER-DAEMON Sun Jan  8 05:21:47 2023
From: Author <autor@example.com>
Subject: Sample message 1

This is the body.
>From (will not be escaped).
There are 3 lines.

From MAILER-DAEMON Sun Jan  8 05:21:47 2023
From: Author <autor@example.com>
To: Recipient <recipient@example.com>
Subject: Sample message 2

This is the second body.
'''

#2 mailbox mbox read

import mailbox

'''
mbox = mailbox.mbox('example.mbox')
for message in mbox:
    print(message['subject'])

RESULTS:
Sample message 1
Sample message 2
'''

#3 mailbox mbox remove

import mailbox

'''
mbox = mailbox.mbox('example.mbox')
mbox.lock()
try:
    to_remove = []
    for key, msg in mbox.iteritems():
        if '2' in msg['subject']:
            print('Removing:', key)
            to_remove.append(key)
    for key in to_remove:
        mbox.remove(key)
finally:
    mbox.flush()
    mbox.close()

print(open('example.mbox', 'r').read())

RESULTS:
Removing: 1
From MAILER-DAEMON Sun Jan  8 05:21:47 2023
From: Author <autor@example.com>
Subject: Sample message 1

This is the body.
>From (will not be escaped).
There are 3 lines.
'''

#4 mailbox maildir create

import mailbox
import email.utils
import os

'''
from_addr = email.utils.formataddr(('Author',
                                    'author@example.com'))
to_addr = email.utils.formataddr(('Recipient',
                                  'recipient@example.com'))

payload = """This is the body.
From (will not be escaped).
There are 3 lines.
"""

mbox = mailbox.Maildir('Example')
mbox.lock()
try:
    msg = mailbox.mboxMessage()
    msg.set_unixfrom('author Sun Mar 12 03:00:33 2023')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Sample message 1'
    msg.set_payload(payload)
    mbox.add(msg)
    mbox.flush()

    msg = mailbox.mboxMessage()
    msg.set_unixfrom('author Mon Jun 30 11:03:33 2023')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Sample message 2'
    msg.set_payload('This is the second body.\n')
    mbox.add(msg)
    mbox.flush()
finally:
    mbox.unlock()

for dirname, subdirs, files in os.walk('Example'):
    print(dirname)
    print('Directories:', subdirs)
    for name in files:
        fullname = os.path.join(dirname, name)
        print('\n***', fullname)
        print(open(fullname).read())
        print('*' * 20)
'''

#5 mailbox maildir set subdir

import mailbox
import os

'''
print('Before:')
mbox = mailbox.Maildir('Example')
mbox.lock()
try:
    for message_id, message in mbox.iteritems():
        print('{:6} "{}"'.format(message.get_subdir(),
                                 message['subject']))
        message.set_subdir('cur')
        # Renew message
        mbox[message_id] = message
finally:
    mbox.flush()
    mbox.close()

print('\nAfter:')
mbox = mailbox.Maildir('Example')
for message in mbox:
    print('{:6} "{}"'.format(message.get_subdir(),
                             message['subject']))

print()
for dirname, subdirs, files in os.walk('Example'):
    print(dirname)
    print('Directories:', subdirs)
    for name in files:
        fullname = os.path.join(dirname, name)
        print(fullname)

RESULTS:
Before:
new    "Sample message 1"
new    "Sample message 2"
new    "Sample message 2"
new    "Sample message 2"
new    "Sample message 1"
new    "Sample message 1"

After:
cur    "Sample message 1"
cur    "Sample message 2"
cur    "Sample message 2"
cur    "Sample message 2"
cur    "Sample message 1"
cur    "Sample message 1"

Example
Directories: ['new', 'cur', 'tmp']
Example/new
Directories: []
Example/cur
Directories: []
Example/cur/1673156826.M486859P754545Q1.Cesar
Example/cur/1673156794.M460809P754530Q2.Cesar
Example/cur/1673156813.M646547P754537Q2.Cesar
Example/cur/1673156826.M488070P754545Q2.Cesar
Example/cur/1673156813.M645205P754537Q1.Cesar
Example/cur/1673156794.M459575P754530Q1.Cesar
Example/tmp
Directories: []
'''

#6 mailbox maildir read

import mailbox

'''
mbox = mailbox.Maildir('Example')
for message in mbox:
    print(message['subject'])
'''

#7 mailbox maildir remove

import mailbox
import os

'''
mbox = mailbox.Maildir('Example')
mbox.lock()
try:
    to_remove = []
    for key, msg in mbox.iteritems():
        if '2' in msg['subject']:
            print('Removing:', key)
            to_remove.append(key)
    for key in to_remove:
        mbox.remove(key)
finally:
    mbox.flush()
    mbox.close()

for dirname, subdirs, files in os.walk('Example'):
    print(dirname)
    print('Directories:', subdirs)
    for name in files:
        fullname = os.path.join(dirname, name)
        print('\n***', fullname)
        print(open(fullname).read())
        print('*' * 20)
'''

#8 mailbox maildir folders

import mailbox
import os


'''
def show_maildir(name):
    os.system('find {} -print'.format(name))

mbox = mailbox.Maildir('Example')
print('Before:', mbox.list_folders())
show_maildir('Example')

print('\n{:#^30}\n'.format(''))

mbox.add_folder('subfolder')
print('subfolder created:', mbox.list_folders())
show_maildir('Example')

subfolder = mbox.get_folder('subfolder')
print('subfolder contents:', subfolder.list_folders())

print('\n{:#^30}\n'.format(''))
subfolder.add_folder('second_level')
print('second_level created:', subfolder.list_folders())
show_maildir('Example')

print('\n{:#^30}\n'.format(''))

subfolder.remove_folder('second_level')
print('second_level removed:', subfolder.list_folders())
show_maildir('Example')
'''

#9 mailbox maildir add flag

import mailbox

'''
print('Before:')
mbox = mailbox.Maildir('Example')
mbox.lock()
try:
    for message_id, message in mbox.iteritems():
        print('{:6} "{}"'.format(message.get_flags(),
                                 message['subject']))
        message.add_flag('F')
        # Renew message
        mbox[message_id] = message
finally:
    mbox.flush()
    mbox.close()

print('\nAfter:')
mbox = mailbox.Maildir('Example')
for message in mbox:
    print('{:6} "{}"'.format(message.get_flags(),
                             message['subject']))
RESULTS:
Before:
       "Sample message 1"
       "Sample message 1"
       "Sample message 1"

After:
F      "Sample message 1"
F      "Sample message 1"
F      "Sample message 1"
'''

#10 mailbox maildir set flags

import mailbox

'''
print('Before:')
mbox = mailbox.Maildir('Example')
mbox.lock()
try:
    for message_id, message in mbox.iteritems():
        print('{:6} "{}"'.format(message.get_flags(),
                                 message['subject']))
        message.set_flags('S')
        # Renew message
        mbox[message_id] = message
finally:
    mbox.flush()
    mbox.close()

print('\nAfter:')
mbox = mailbox.Maildir('Example')
for message in mbox:
    print('{:6} "{}"'.format(message.get_flags(),
                             message['subject']))
'''
