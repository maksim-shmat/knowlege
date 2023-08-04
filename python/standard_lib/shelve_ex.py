"""shelve keep data long time as db."""

'''
#1 Potential trap

import shelve

s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c']
s['x'].append('d')
print(s['x'])  # ['a', 'b', 'c'] but not 'd'

#2 Use temporary variable

temp = s['x']
temp.append('d')
s['x'] = temp
print(s['x'])  # ['a', 'b', 'c', 'd']
'''
#3 Database with shelve

import sys, shelve

def store_person(db):
    """Query user for data and store it in the shelf object."""
    pid = input('Enter unique ID number: ')
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone number: ')
    db[pid] = person

def lookup_person(db):
    """Query user for ID and desired field, and fetch the corresponding
    data from the shelf object.
    """
    pid = input('Enter ID number: ')
    field = input('What would you like to know? (name, age, phone)')
    field = field.strip().lower()
    print(field.capitalize() + ':', db[pid][field])

def print_help():
    print('The available commands are: ')
    print('store: Stores information about a person')
    print('lookup: Looks up a person from ID number')
    print('quit: Save changes and exit')
    print('?: Print this message')

def enter_command():
    cmd = input('Enter command(? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('/home/jack/django2/knowlege/python/database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()
if __name__ == '__main__':
    main()

#4 create
'''
import shelve

with shelve.open('test_shelf.db') as s:
    s['key1'] = {
            'int': 10,
            'float': 9.5,
            'string': 'Sample data',
    }

#5 existing

import shelve

with shelve.open('test_shelf.db') as s:
    existing = s['key1']

print(existing)

   RESULTS from #4 and then #5:
{'string': 'Sample data', 'int': 10, 'float': 9.5}

'''

#6 shelve writeback for autorewrite db

import shelve
import pprint

with shelve.open('test_shelf.db', writeback=True) as s:
    print('Initial data:')
    pprint.pprint(s['key1'])

    s['key1']['new_value'] = 'this was not here befor'
    print('\nModified:')
    pprint.pprint(s['key1'])
with shelve.open('test_shelf.db', writeback=True) as s:
    print('\nPreserved:')
    pprint.pprint(s['key1'])

#7 writeback by defolt is False beacause eat memory

with shelve.open('shelf2.shelve', writeback=True) as db:
    db['a_list'] = [11, 13, 17]
    db['a_list'].append(19)
    print(db['a_list'])  # [11, 13, 17, 19]

#8
