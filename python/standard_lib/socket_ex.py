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

import binascii
import socket
import struct
import sys

'''
string_address = '2002:ac10:10a:1234:21e:52ff:fe74:40e'
packed = socket.inet_pton(socket.AF_INET6, string_address)

print('Original:', string_address)
print('Packed  :', binascii.hexlify(packed))
print('Unipacked:', socket.inet_ntop(socket.AF_INET6, packed))

RESULTS:
Original: 2002:ac10:10a:1234:21e:52ff:fe74:40e
Packed  : b'2002ac10010a1234021e52fffe74040e'
Unipacked: 2002:ac10:10a:1234:21e:52ff:fe74:40e
'''

#14 socket echo server

import socket
import sys

'''
# Create socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Get data little by little and send it backward
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        connection.close()
'''

#15 socket echo client

import socket
import sys

'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    message = b'This is the message. It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received <amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
'''

#16 socket echo client easy

import socket
import sys

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

sock = socket.create_connection(('localhost', 10000))

print('Family  :', families[sock.family])
print('Type    :', types[sock.type])
print('Protocol:', protocols[sock.proto])
print()

try:
    # Send data
    message = b'This is the message. It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
'''

#17 socket echo server explicit
# $ host hubert.hellfly.net
# $ netstat -an | grep 10000
# $ python3 socket_echo_server_explicit.py hubert.hellfly.net

import socket
import sys

'''
# Create socket for address
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to address
server_name = sys.argv[1]
server_address = (server_name, 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address)
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
'''

#18 socket echo client explicit
# $ hostname
# $ python3 ./socket_echo_client_explicit.py hubert.hellfly.net
import socket
import sys


'''
# Create socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect socket to port on the server
server_address = (sys.argv[1], 10000)

print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    message = b'This is the message. It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    sock.close()
'''

#19 socket echo server any
# netstat -an

import socket
import sys

'''
# Create TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket
server_address = ('', 10000)
sock.bind(server_address)
print('starting up on {} port {}'.format(*sock.getsockname()))
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address)
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
'''

#20 socket echo server dgram gor UDP

import socket
import sys

'''
# Create socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind socket to the port
server_address = ('lockalhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(
        len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('send {} bytes back to {}'.format(
            sent, address))
'''

#21 socket echo client dgram

import socket
import sys

'''
# Create socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is the message. It will be repeated.'

try:
    # Send data
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # Get answer
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))
    
finally:
    print('closing socket')
    sock.close()
'''

#22 socket echo server UDS

import socket
import sys
import os

'''
server_address = './uds_socket'

# Check what socket exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Create socket UDS
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind socket to address
print('starting up on {}'.format(server_address))
sock.bind(server_address)

# Listen 
sock.listen(1)

while True:
    # Wait connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Get data as little chunks and send it backward
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()
'''

#23 socket echo client UDS
# Permission access
# $ ls -l ./uds_socket
# srwxr-xr-x 1 dhelmann dhellmann 0 Aug 22 11:20 uds_socket
# $ sudo chown root ./uds_socket
# $ ls -l ./uds_socket
# srwxr-xr-x 1 root dhelman 0 Aug 22 11:20 uds_socket

import socket
import sys

'''
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './uds_socket'
print('connecting to {}'.format(server_address))
try:
    sock.connect(server_address)
except socket.error as msg:
    print(msg)
    sys.exit(1)

try:
    message = b'This is the message. It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.slose()
'''    

#24 socket socketpair

import socket
import os

'''
parent, child = socket.socketpair()

pid = os.fork()

if pid:
    print('in parent, sending message')
    child.close()
    parent.sendall(b'ping')
    response = parent.recv(1024)
    print('response from child:', response)
    parent.close()

else:
    print('in child, waiting for message')
    parent.close()
    message = child.recv(1024)
    print('message from parent:', message)
    child.sendall(b'pong')
    child.close()

RESULTS:
in parent, sending message
in child, waiting for message
message from parent: b'ping'
response from child: b'pong'
'''

#25 socket multicast sender

import socket
import struct
import sys

'''
message = b'very important data'
multicast_group = ('224.3.29.71', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.2)
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, multicast_group)

    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timed out, no more responses')
            break
        else:
            print('received {!r} from {}'.format(
                data, server))
finally:
    print('closing socket')
    sock.close()
'''

#26 socket multicast receiver

import socket
import struct
import sys

'''
multicast_goup = '224.3.29.71'

server_address = ('', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(server_address)

goup = socket.inet_aton(multicast_goup)
mreq = struct.pack('4sL', goup, socket.INADDR_ANY)
sock.setsockopt(
        socket.IPPROTO_IP,
        socket.IP_ADD_MEMBERSHIP,
        mreq)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)

    print('received {} bytes from {}'.format(
        len(data), address))
    print(data)

    print('sending acknowlegement to', address)
    sock.sendto(b'ack', address)
'''

#27 socket binary client

import binascii
import socket
import struct
import sys

'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.connect(server_address)

values = (1, b'ab', 2.7)
packer = struct.Struct('I 2s f')
packed_data = packer.pack(*values)

print('values =', values)

try:
    print('sending {!r}'.format(binascii.hexlify(packed_data)))
    sock.sendall(packed_data)
finally:
    print('closing socket')
    sock.close()
'''

#28 socket binary server

import binascii
import socket
import struct
import sys


'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

unpacker = struct.Struct('I 2s f')

while True:
    print('\nwaiting for a connection')
    connection, client_address = sock.accept()
    try:
        data = connection.recv(unpacker.size)
        print('received {!r}'.format(binascii.hexlify(data)))

        unpacked_data = unpacker.unpack(data)
        print('unpacked:', unpacked_data)
        
    finally:
        connection.close()
'''
