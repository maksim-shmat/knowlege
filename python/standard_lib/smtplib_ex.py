"""smtplib about."""

#1 smtplib sendmail

import smtplib
import email.utils
from email.mime.text import MIMEText

'''
# Create message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'recipient@example.com'))
msg['From'] = email.utils.formataddr(('Author',
                                      'author@example.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(True)

try:
    server.sendmail('author@example.com',
                    ['recipient@example.com'],
                    msg.as_string())
finally:
    server.quit()
'''

#2 smtplib authenticated

import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass

'''
to_email = input('Recipient:')
servername = input('Mail server name:')
serverport = input('Server port:')
if serverport:
    serverport = int(serverport)
else:
    serverport = 25
use_tls = input('Use TSL? (yes/no):').lower()
username = input('Mail username:')
password = getpass.getpass("%s's password:" % username)

# Create message
msg = MIMEText('Test message from cooCOO.')
msg.set_unixfrom('author')
msg['To'] = email.utils.formataddr(('Recipient', to_email))
msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
msg['Subject'] = 'Test from cooCOO'

if use_tls == 'yes':
    print('starting with a secure connection')
    server = smtplib.SMTP_SSL(servername, serverport)
else:
    print('starting with an insecure connection')
    server = smtplib.SMTP(servername, serverport)
try:
    server.set_debuglevel(True)
    # identification oneself
    server.ehlo()

    # use encription if is it
    if server.has_extn('STARTTLS'):
        print('(starting TSL)')
        server.starttls()
        server.ehlo()  # second identification with TSL connection
    else:
        print('(no STARTTLS)')
    
    if server.has_extn('AUTH'):
        print('(logging in)')
        server.login(username, password)
    else:
        print('(no AUTH)')

    server.sendmail('author@example.com',
                   [to_email],
                   msg.as_string())
finally:
    server.quit()
'''

#3 smtplib verify. Commonly it OFF, because spammer checked true name with email

import smtplib

'''
serve = smtplib.SMTP('mail')
server.set_debuglevel(True)

try:
    dhellhound_result = server.verify('dhellhound')
    notthere_result = serve.verify('notthere')
finally:
    server.quit()

print('dhellhound:', dhellhound_result)
print('notthere  :', notthere_result)
'''

#4 smtp custom for first window

import smtpd
import asyncore

'''
class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))

server = CustomSMTPServer(('127.0.0.1', 1025), None)

asyncore.loop()
'''

#5 smtpd_senddata. for second window

import smtplib
import email.utils
from email.mime.text import MIMEText

'''
# Create message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'recipient@example.com'))
msg['From'] = email.utils.formataddr(('Author',
                                      'author@example.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('127.0.0.1', 1025)
server.set.debuglevel(True)

try:
    server.sendmail('author@example.com',
                    ['recipient@example.com'],
                    msg.as_string())
finally:
    server.quit()
'''    

#6 smtp debug without send msg real server

import smtpd
import asyncore

'''
server = smtpd.DebuggingServer(('127.0.0.1', 1025), None)

asyncore.loop()
'''

#7 smtpd proxy, not safe

import smtpd
import asyncore

'''
server = smtpd.PureProxy(('127.0.0.1', 1025), ('mail', 25))

asyncore.loop()
'''
