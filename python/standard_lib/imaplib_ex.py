"""imaplib about."""

#1 imaplib connect

import imaplib
import configparser
import os

'''
def open_connection(verbose=False):
    # Read configuration file
    config = configparser.ConfigParser()
    config.read([os.path.expanduser('~/.pymotw')])

    # Connect to the server
    hostname = config.get('server', 'hostname')
    if verbose:
        print('Connecting to', hostname)
    connection = imaplib.IMAP4_SSL(hostname)

    # LogIn
    username = config.get('account', 'username')
    password = config.get('account', 'password')
    if verbose:
        print('Logging in as', username)
    connection.login(username, password)
    return connection


if __name__ == "__main__":
    with open_connection(verbose=True) as c:
        print(c)
'''

#2 imaplib connect fail

import imaplib
import configparser
import os

'''
# Read configuration file
config = configparser.ConfigParser()
config.read([os.path.expanduser('~/.pymotw')])

# Connect to the server
hostname = config.get('server', 'hostname')
print('Connection to', hostname)
connection = imaplib.IMAP4_SSL(hostname)

# LogIn
username = config.get('account', 'usrname')
password = 'this_is_the_wrong_password'
print('Logging in as ', username)
try:
    connection.login(username, password)
except Exception as err:
    print('ERROR:', err)
'''

#3 imaplib list

import imaplib
from pprint import pprint
from imaplib_connect import open_connection

'''
with open_connection() as c:
    typ, data = c.list()
    print('Response code:', typ)
    print('Response:')
    pprint(data)
'''

#4 imaplib list parse

import imaplib
import re

from imaplib_connect import open_connection

'''
list_response_pattern = re.compile(
        r'\((?P<flag>.*?)\) "(?P<deimiter>.*)" (?P<name>.*)'
)

def parse_list_response(line):
    match = list_response_pattern.match(line.decode('utf-8'))
    flags, delimiter, mailbox_name = match.groups()
    mailbox_name = mailbox_name.strip('"')
    return (flags, delimiter, mailbox_name)

with open_connection() as c:
    typ, data = c.list()
print('Response code:', typ)

for line in data:
    print('Server response:', line)
    flags, delimiter, mailbox_name = parse_list_response(line)
    print('Parse response:', (flags, delimiter, mailbox_name))
'''

#5 imaplib list subfolders

import imaplib

from imaplib_connect import open_connection

'''
with open_connection() as c:
    typ, data = c.list(directory='Example')

print('Response code:', typ)

for line in data:
    print('Server response:', line)
'''

#6 imaplib list pattern

import imaplib

from imaplib_connect import open_connection
'''
with open_connection() as c:
    typ, data = c.list(pattern='*Example*')

print('Response code:', typ)

for line in data:
    print('Server resonse:', line)
'''

#7 imaplib status

import imaplib
import re

from imaplib_connect import open_connection
from imaplib_list_parse import parse_list_response

'''
with open_connection() as c:
    typ, data = c.list()
    for line in data:
        flags, delimiter, mailbox = parse_list_response(line)
        print('Mailbox:', mailbox)
        status = c.status(
                '"{}"'.format(mailbox),
                '(MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)',
        )
        print(status)
'''

#8 imaplib select

import imaplib
import imaplib_connect

'''
with imaplib_connect.open_connection() as c:
    typ, data = c.select('INBOX')
    print(typ, data)
    num_msgs = int(data[0])
    print('There are {} messages in INBOX'.format(num_msgs))
'''

#9 imaplib select invalid

import imaplib
import imaplib_connect

'''
wiht imaplib_connect.open_connection() as c:
    typ, data = c.select('Does-Not-Exist')
    print(typ, data)
'''

#10 imaplib search all

import imaplib
import imaplib_connect

from imaplib_list_parse import parse_list_response

'''
with imaplib_connection.open_connection() as c:
    typ, mbox_data = c.list()
    for line in mbox_data:
        flags, delimiter, mbox_name = parse_list_response(line)
        c.select('"{}"'.format(mbox_name), readonly=True)
        typ, msg_ids = c.search(None, 'ALL')
        print(mbox_name, typ, msg_ids)
'''

#11 imaplib search subject

import imaplib
import imaplib_connect

from imaplib_list_parse import parse_list_response

'''
with imaplib_connect.open_connection() as c:
    typ, mbox_data = c.list()
    for line in mbox_data:
        flags, delimiter, mbox_name = parse_list_response(line)
        c.select('"{}"'.format(mbox_name), readonly=True)
        typ, msg_ids = c.search(
                None,
                '(SUBJECT "Example message 2")',
        )
        print(mbox_name, typ, msg_ids)
'''

#12 imaplib search from

import imaplib
import imaplib_connect

from imaplib_list_parse import parse_list_response


'''
with imaplib_connect.open_connection() as c:
    typ, mbox_data = c.list()
    for line in mboxf_data:
        flags, delimiter, mbox_name = parse_list_response(line)
        c.select('"{}"'.format(mbox_name), readonly=True)
        typ, msg_ids = c.search(
                None,
                '(FROM "Doug" SUBJECT "Example message 2")',
        )
        print(mbox_name, typ, msg_ids)
'''

#13 imaplib fetch raw

import imaplib
import pprint
import imaplib_connect

'''
imaplib.Debug = 4
with imaplib_connect.open_connection() as c:
    c.select('INBOX', readonly=True)
    typ, msg_data = c.fetch('1', '(BODY.PEEK[HEADER] FLAGS)')
    pprint.pprint(mag_data)
'''

#14 imaplib fetch separately

import imaplib
import pprint
import imaplib_connect

'''
with imaplib_connect.open_connection() as c:
    c.select('INBOX', readonly=True)
    print('HEADER:')
    typ, msg_data = c.fetch('1', '(BODY.PEEK[HEADER])')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            print(response_part[1])

    print('\nFLAGS:')
    typ, msg_data = c.fetch('1', '(FLAGS)')
    for response_part in msg_data:
        print(response_part)
        print(imaplib.ParseFlags(response_part))
'''

#15 imaplib fetch rfc822

import imaplib
import email
import email.parser

import imaplib_connect

'''
with imaplib_connect.open_connection() as c:
    c.select('INBOX', readonly=True)
    typ, msg_data = c.fetch('1', '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            email_parser = email.parser.BytesFeedParser()
            email_parser.feed(response_part[1])
            msg = email_parser.close()
            for header in ['subject', 'to', 'from']:
                print('{:^8}: {}'.format(
                    header.upper(), msg[header]))
'''

#16 imaplib append

import imaplib
import time
import email.message
import imaplib_connect

'''
new_message = email.message.Message()
new_message.set_unixfrom('pymotw')
new_message['Subject'] = 'subject goes here'
new_message['From'] = 'pymotw@example.com'
new_message['To'] = 'example@example.com'
new_message.set_payload('This is the body of the message.\n')

print(new_message)

with imaplib_connect.open_connection() as c:
    c.append('INBOX', '',
            imaplib.Time2Internaldate(time.time()),
            str(new_message).encode('utf-8'))
    # Show headers for all messages in mailbox
    c.select('INBOX')
    typ, [msg_ids] = c.search(None, 'ALL')
    for num in msg_ids.split():
        typ, msg_data = c.fetch(num,'(BODY.PEEK(HEADER])')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                print('\n{}:'.format(num))
                print(response_part[1])
'''

#17 imaplib archive read

import imaplib
import imaplib_connect

'''
with imaplib_connect.open_connection() as c:
    # Search message with "SEEN" flag in INBOX dir
    c.select('INBOX')
    typ, [response] = c.search(None, 'SEEN')
    if typ != 'OK':
        raise RuntimeError(response)
    msg_ids = ','.join(response.decode('utf-8').split(' '))

    # Create new postbox "Example.Today"
    typ, crate_response = c.create('Example.Today')
    print('CREATED Example.Today:', create_response)

    # Copy message
    print('COPYING:', msg_ids)
    c.copy(msg_ids, 'Example.Today')

    # Check results
    c.select('Example.Today')
    typ, [response] = c.search(None, 'ALL')
    print('COPIED:', response)
'''

#18 imaplib delete messages

import lmaplib
import imaplib_connect

from imaplib_list_parse import parse_list_response

'''
with imaplib_connect.open_connection() as c:
    c.select('Example.Today')
    
    # Which id's of messages in mailbox?
    typ, [msg_ids] = c.search(None, 'ALL')
    print('Starting messages:', msg_ids)

    # Search message/s
    typ, [msg_ids] = c.search(
            None,
            '(SUBJECT "subject goes here")',
    )
    msg_ids = ','.join(msg_ids.decode('utf-8').split(' '))
    print('Matching messages:', msg_ids)

    # Which currently position of flags?
    typ, response = c.fetch(msg_ids, '(FLAGS)')
    print('Flags before:', response)

    # Change Deleted flag
    typ, response = c.store(msg_ids, '+FLAGS', r'(\Deleted)')

    # Which positino of flags now?
    typ, response = c.fetch(msg_ids, '(FLAGS)')
    print('Flags after:', response)

    # Delete message forever
    typ, response = c.expunge()
    print('Expunged:', response)

    # Which id's last messages
    typ, [msg_ids] = c.search(None, 'ALL')
    print('Remaining messages:', msg_ids)
'''
