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

import socket
from urllib.parse import urlunparse

'''
for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
    url = '{}://example.com/'.format(socket.getservbyport(port))
    print(url)

RESULTS:
http://example.com/
https://example.com/
ftp://example.com/
gopher://example.com/
smtp://example.com/
imap2://example.com/
imaps://example.com/
pop3://example.com/
pop3s://example.com/
'''

#9 socket getprotobyname() for get port number

import socket

'''
def get_constants(prefix):
    """Make a dict."""
    return{
            getattr(socket, n):
            n for n in dir(socket)
            if n.startswith(prefix)
    }

protocols = get_constants('IPPROTO_')

for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print('{:>4} -> {:2d} (socket.{:<12} = {:2d})'.format(
        name, proto_num, const_name,
        getattr(socket, const_name)))

RESULTS:
icmp ->  1 (socket.IPPROTO_ICMP =  1)
 udp -> 17 (socket.IPPROTO_UDP  = 17)
 tcp ->  6 (socket.IPPROTO_TCP  =  6)
'''

#10 socket getaddrinfo() for get server address

import socket

'''
def get_constants(prefix):
    """Make a dict"""
    return {
            getattr(socket, n): n
            for n in dir(socket)
            if n.startswith(prefix)
    }

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('www.python.org', 'http'):

    # Unpack tuple answer
    family, socktype, proto, canonname, sockaddr = response

    print('Family        :', families[family])
    print('Type          :', types[socktype])
    print('Protocol      :', protocols[proto])
    print('Canonical name:', canonname)
    print('Socket address:', sockaddr)
    print()

RESULTS:
Traceback (most recent call last):
  File "<stdin>", line 260, in <module>
  File "/usr/lib/python3.10/socket.py", line 955, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno -3] Temporary failure in name resolution

shell returned 1

EXPECTED RESULTS:
Family         : AF_INET
Type           : SOCK_DGRAM
Protocol       : IPPROTO_UDP
Canonical name :
Socket address : ('151.101.32.223', 80)

Family         : AF_INET
Type           : SOCK_STREAM
Protocol       : IPPROTO_TCP
Canonical name :
Socket address : ('151.101.32.223', 80)

Family         : AF_INET6
Type           : SOCK_DGRAM
Protocol       : IPPROTO_UDP
Canonical name :
Socket address : ('2a04:4e42:8::223', 80, 0, 0)

Family         : AF_INET6
Type           : SOCK_STREAM
Protocol       : IPPROTO_TCP
Canonical name :
Socket address : ('2a04:4e42:8::223', 80, 0, 0)
'''

#11 socket getaddrinfo extra args

import socket

'''
def get_constants(prefix):
    """Make a dict."""
    return {
            getattr(socket, n): n
            for n in dir(socket)
            if n.startswith(prefix)
    }

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

responses = socket.getaddrinfo(
        host='www.python.org',
        port='http',
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
        proto=socket.IPPROTO_TCP,
        flags=socket.AI_CANONNAME,
)

for response in responses:
    # Unpack tuple answer
    family, socktype, proto, canonname, sockaddr = response

    print('Family        :', families[family])
    print('Type          :', types[socktype])
    print('Protocol      :', protocols[proto])
    print('Canonical name:', canonname)
    print('Socket address:', sockaddr)
    print()

RESULTS:
Traceback (most recent call last):
  File "<stdin>", line 324, in <module>
  File "/usr/lib/python3.10/socket.py", line 955, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno -3] Temporary failure in name resolution

shell returned 1

EXPECTED RESULTS:

Family        : AF_INET
Type          : SOCK_STREAM
Protocol      : IPPROTO_TCP
Canonical name: prod.python.map.fastlylb.net
Socket address: ('151.101.32.223', 80)
'''

#12 socket address packing

import binascii
import socket
import struct
import sys

'''
for string_address in ['192.168.1.1', '127.0.0.1']:
    packed = socket.inet_aton(string_address)
    print('Original:', string_address)
    print('Packed  :', binascii.hexlify(packed))
    print('Unpacked:', socket.inet_ntoa(packed))
    print()

RESULTS:
Original: 192.168.1.1
Packed  : b'c0a80101'
Unpacked: 192.168.1.1

Original: 127.0.0.1
Packed  : b'7f000001'
Unpacked: 127.0.0.1
'''

#13 socket ipv6 address packing
