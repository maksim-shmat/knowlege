"""socet about."""

#1 socket file

import sys
import socketserver

'''
class Echo(socketserver.BaseRequestHandler):

    def handle(self):
        """Get bytes and return it to client.
        Decode data not need, then it not use there.
        """
        data = self.request.recv(1024)
        self.request.send(data)


class PassThrough:

    def __init__(self, other):
        self.other = other

    def write(self, data):
        print('Writing:', repr(data))
        return self.other.write(data)

    def read(self, size=-1):
        print('Reading:', end=' ')
        data = self.other.read(size)
        print(repr(data))
        return data

    def flush(self):
        return self.other.flush()

    def close(self):
        return self.other.close()

if __name__ == '__main__':
    import codecs
    import socket
    import threading

    address = ('localhost', 0)  # The core check port
    server = socketserver.TCPServer(address, Echo)
    ip, port = server.server_address  # How port is checked?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  # make thread to the daemon thread
    t.start()

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Wrapping socket from read/write object
    read_file = s.makefile('rb')
    incoming = codecs.getreader('utf-8')(PassThrough(read_file))
    write_file = s.makefile('wb')
    outgoing = codecs.getwriter('utf-8')(PassThrough(write_file))

    # Send data
    # Not encoded first!
    text = 'français'
    print('Sending:', repr(text))
    outgoing.write(text)
    outgoing.flush()

    # get an ansver
    response = incoming.read()
    print('Received:', repr(response))

    # Empty source
    s.close()
    server.socket.close()

RESULTS:
<stdin>:50: DeprecationWarning: setDaemon() is deprecated, set the daemon attribute instead
Sending: 'français'
Writing: b'fran\xc3\xa7ais'
Reading: b'fran\xc3\xa7ais'
Reading: b''
Received: 'français'
'''

#2 socket gethostname

import socket

print(socket.gethostname())

#3 change hostname to numbers with gethostbyname()

import socket

'''
HOSTS = [
        'apy',
        'pymotw.com',
        'www.python.com',
        'nosuchname',
]

for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host, msg))
'''

#4 socket gethostbynamei_ex()

import socket

'''
HOSTS = [
        'apu',
        'pymotw.com',
        'www.python.org',
        'nosuchname',
]

for host in HOSTS:
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print('  Hostname:', name)
        print('   Aliases:', aliases)
        print(' Addresses:', addresses)
    except socket.error as msg:
        print('ERROR:', msg)
    print()
'''

#5 socket getfqdn() for get true host name

import socket
'''
for host in ['apu', 'pymotw.com']:
    print('{:>10} : {}'.format(host, socket.getfqdn(host)))
'''
#6 socket gethostbyaddr()

import socket
'''
hostname, aliases, addresses = socket.gethostbyaddr('10.9.0.10')

print('Hostname :', hostname)
print('Aliases  :', aliases)
print('Addresses:', addresses)

EXPECTED RESULTS:
Hostname  : apu.hellfy.net
Aliases   : ['apu']
Addresses : ['10.9.0.10']
'''

#7 socket getservbyname

'''
import socket
from urllib.parse import urlparse


URLS = [
        'http://www.python.org',
        'https://www.mybank.com',
        'ftp://prep.ai.mit.edu',
        'gopher://gopher.micro.umn.edu',
        'smtp://mail.example.com',
        'imap://mail.example.com',
        'pop3://pop.example.com',
        'pop3s://pop.example.com',
]

for url in URLS:
    parsed_url = urlparse(url)
    port = socket.getservbyname(parsed_url.scheme)
    print('{:>6} : {}'.format(parsed_url.scheme, port))

RESULTS:
 http : 80
 https : 443
   ftp : 21
gopher : 70
  smtp : 25
  imap : 143
  pop3 : 110
 pop3s : 995
'''

#8 socket getservebyport
