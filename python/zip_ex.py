"""zip() about."""

######1

list_a = [0, 1, 2]
list_b = ['zero', 'one', 'two']
list_c = ['adzin', 'djva', 'tsiri']
zizi = list(zip(list_a, list_b, list_c))
print(zizi)
print()
for a, b, c in zip(list_a, list_b, list_c):
    print(f'{a} is {b} in English and {c} in Murmurians.')

######2 write self zip

def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    res = []
    while all(seqs):
        res.append(tuple(s.pop(0) for s in seqs))

def mymapPad(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    res = []
    while any (seqs):
        res.append(tuple((s.pop(0) if s else pad) for s in seqs))
    return res

s1, s2 = 'abc', 'xyz123'
print(myzip(s1, s2))
print(mymapPad(s1,s2))
print(mymapPad(s1, s2, pad=99))

#1 copmpression zip

from zipfile import ZipFile


with ZipFile('example.zip', 'w') as zp:
    zp.write('content1.txt')
    zp.write('content2.txt')
    zp.write('subfolder/content3.txt')
    zp.write('subfolder/content4.txt')

with ZipFile('example.zip') as zp:
    zp.extract('content1.txt', 'extract_zip')
    zp.extract('subfolder/content3.txt', 'extract_zip')

#2
