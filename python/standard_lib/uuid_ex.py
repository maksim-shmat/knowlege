"""uuid about."""

#1 uuid getnode

import uuid

'''
print(hex(uuid.getnode()))

RESULTS:
0x998981cf0510
'''

#2 uuid uuid1

import uuid

'''
u = uuid.uuid1()

print(u)
print(type(u))
print('bytes    :', repr(u.bytes))
print('hex      :', u.hex)
print('int      :', u.int)
print('urn      :', u.urn)
print('variant  :', u.variant)
print('version  :', u.version)
print('fields   :', u.fields)
print('  time_low             :', u.time_low)
print('  time_mid             :', u.time_mid)
print('  time_hi_version      :', u.time_hi_version)
print('  clock_seq_hi_variant :', u.clock_seq_hi_variant)
print('  clock_seq_low        :', u.clock_seq_low)
print('  node                 :', u.node)
print('  time                 :', u.time)
print('  clock_seq            :', u.clock_seq)

RESULTS:
938b3766-8aec-11ed-85b2-998981cf0510
<class 'uuid.UUID'>
bytes    : b'\x93\x8b7f\x8a\xec\x11\xed\x85\xb2\x99\x89\x81\xcf\x05\x10'
hex      : 938b37668aec11ed85b2998981cf0510
int      : 196119368300514074164578286082425029904
urn      : urn:uuid:938b3766-8aec-11ed-85b2-998981cf0510
variant  : specified in RFC 4122
version  : 1
fields   : (2475374438, 35564, 4589, 133, 178, 168815867397392)
  time_low             : 2475374438
  time_mid             : 35564
  time_hi_version      : 4589
  clock_seq_hi_variant : 133
  clock_seq_low        : 178
  node                 : 168815867397392
  time                 : 138919912210642790
  clock_seq            : 1458
'''

#3 uuid uuid4

import uuid

'''
for i in range(3):
    print(uuid.uuid4())
'''
