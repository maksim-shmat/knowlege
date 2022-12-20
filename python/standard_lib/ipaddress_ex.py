"""ipaddress about."""

#1 ipaddresses

import binascii
import ipaddress

'''
ADDRESSES = [
        '10.9.0.6',
        'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]

for ip in ADDRESSES:
    addr = ipaddress.ip_address(ip)
    print('{!r}'.format(addr))
    print('    IP version:', addr.version)
    print('    is private:', addr.is_private)
    print('   packed form:', binascii.hexlify(addr.packed))
    print('       integer:', int(addr))
    print()

RESULTS:
IPv4Address('10.9.0.6')
    IP version: 4
    is private: True
   packed form: b'0a090006'
       integer: 168361990

IPv6Address('fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa')
    IP version: 6
    is private: True
   packed form: b'fdfd87b5b4755e3eb1bce121a8eb14aa'
       integer: 337611086560236126439725644408160982186
'''

#2 ipaddress networks

import ipaddress

'''
NETWORKS = [
        '10.9.0.0/24',
        'fdfd:87b5:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    print('    is private:', net.is_private)
    print('     broadcast:', net.broadcast_address)
    print('    compressed:', net.compressed)
    print('  with netmask:', net.with_netmask)
    print(' with hostmask:', net.with_hostmask)
    print(' num addresses:', net.num_addresses)
    print()

RESULTS:
IPv4Network('10.9.0.0/24')
    is private: True
     broadcast: 10.9.0.255
    compressed: 10.9.0.0/24
  with netmask: 10.9.0.0/255.255.255.0
 with hostmask: 10.9.0.0/0.0.0.255
 num addresses: 256

IPv6Network('fdfd:87b5:b475:5e3e::/64')
    is private: True
     broadcast: fdfd:87b5:b475:5e3e:ffff:ffff:ffff:ffff
    compressed: fdfd:87b5:b475:5e3e::/64
  with netmask: fdfd:87b5:b475:5e3e::/ffff:ffff:ffff:ffff::
 with hostmask: fdfd:87b5:b475:5e3e::/::ffff:ffff:ffff:ffff
 num addresses: 18446744073709551616
'''

#3 ipaddress network iterate

import ipaddress

'''
NETWORKS = [
        '10.9.0.0/24',
        'fdfd:87b5:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    for i, ip in zip(range(3), net):
        print(ip)
    print()

RESULTS:
IPv4Network('10.9.0.0/24')
10.9.0.0
10.9.0.1
10.9.0.2

IPv6Network('fdfd:87b5:b475:5e3e::/64')
fdfd:87b5:b475:5e3e::
fdfd:87b5:b475:5e3e::1
fdfd:87b5:b475:5e3e::2
'''

#4 ipaddress network iterate hosts

import ipaddress

'''
NETWORKS = [
        '10.9.0.0/24',
        'fdfd:87b5:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    for i, ip in zip(range(3), net.hosts()):
        print(ip)
    print()

RESULTS:
IPv4Network('10.9.0.0/24')
10.9.0.1
10.9.0.2
10.9.0.3

IPv6Network('fdfd:87b5:b475:5e3e::/64')
fdfd:87b5:b475:5e3e::1
fdfd:87b5:b475:5e3e::2
fdfd:87b5:b475:5e3e::3
'''

#5 ipaddress network membership

import ipaddress

'''
NETWORKS = [
        ipaddress.ip_network('10.9.0.0/24'),
        ipaddress.ip_network('fdfd:87b5:b475:5e3e::/64'),
]

ADDRESSES = [
        ipaddress.ip_address('10.9.0.6'),
        ipaddress.ip_address('10.7.0.31'),
        ipaddress.ip_address(
            'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa'
        ),
        ipaddress.ip_address('fe80::3840:c439:b25e:63b0'),
]

for ip in ADDRESSES:
    for net in NETWORKS:
        if ip in net:
            print('{}\nis on {}'.format(ip, net))
            break
    else:
        print('{}\nis not on a known network'.format(ip))
    print()

RESULTS:
10.9.0.6
is on 10.9.0.0/24

10.7.0.31
is not on a known network

fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa
is on fdfd:87b5:b475:5e3e::/64

fe80::3840:c439:b25e:63b0
is not on a known network
'''

#6 ipaddress interfaces

import ipaddress

'''
ADDRESSES = [
        '10.9.0.6/24',
        'fdfd:87d5:b475:5e3e:b1bc:e121:a8eb:14aa/64',
]

for ip in ADDRESSES:
    iface = ipaddress.ip_interface(ip)
    print('{!r}'.format(iface))
    print('network:\n ', iface.network)
    print('ip:\n ', iface.ip)
    print('IP with prefixlen:\n ', iface.with_prefixlen)
    print('netmask:\n ', iface.with_netmask)
    print('hostmask:\n ', iface.with_hostmask)
    print()

RESULTS:
IPv4Interface('10.9.0.6/24')
network:
  10.9.0.0/24
ip:
  10.9.0.6
IP with prefixlen:
  10.9.0.6/24
netmask:
  10.9.0.6/255.255.255.0
hostmask:
  10.9.0.6/0.0.0.255

IPv6Interface('fdfd:87d5:b475:5e3e:b1bc:e121:a8eb:14aa/64')
network:
  fdfd:87d5:b475:5e3e::/64
ip:
  fdfd:87d5:b475:5e3e:b1bc:e121:a8eb:14aa
IP with prefixlen:
  fdfd:87d5:b475:5e3e:b1bc:e121:a8eb:14aa/64
netmask:
  fdfd:87d5:b475:5e3e:b1bc:e121:a8eb:14aa/ffff:ffff:ffff:ffff::
hostmask:
  fdfd:87d5:b475:5e3e:b1bc:e121:a8eb:14aa/::ffff:ffff:ffff:ffff
'''
