"""dbm save data as data base, about."""

#1 make new db

import dbm

with dbm.open('/tmp/example.db', 'n') as db:
    db['key'] = 'value'
    db['today'] = 'Sunday'
    db['author'] = 'Boug'

#2 whichdb

import dbm

print(dbm.whichdb('/tmp/example.db'))

'''RESULTS:
dbm.gnu
'''

#3 dbm existing

import dbm

with dbm.open('/tmp/example.db', 'r') as db:
    print('keys():', db.keys())
    for k in db.keys():
        print('iterating:', k, db[k])
    print('db["author"] =', db['author'])

'''RESULTS:
keys(): [b'today', b'author', b'key']
iterating: b'today' b'Sunday'
iterating: b'author' b'Boug'
iterating: b'key' b'value'
db["author"] = b'Boug'
'''

#4 
