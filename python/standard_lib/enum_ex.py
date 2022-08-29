"""enum() about."""

#1 enum create
import enum

class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

print('\nMember name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))
'''RESULTS:
Member name: wont_fix
Member value: 4
'''
#2 enum iterate

incomplete = 6
new = 7
wont_fix = 4
invalid = 5
fix_committed = 2
in_progress = 3
fix_released = 1

for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))
'''RESULTS:
    new             = 7
incomplete      = 6
invalid         = 5
wont_fix        = 4
in_progress     = 3
fix_committed   = 2
fix_released    = 1
'''

#3 enum comparison
#import enum

class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print('Equality:',
       actual_state == desired_state,
       actual_state == BugStatus.wont_fix)

print('Identity:',
        actual_state is desired_state,
        actual_state is BugStatus.wont_fix)

print('Ordered by value:')
try:
    print('\n'.join('  ' + s.name for s in sorted(BugStatus)))
except TypeError as err:
    print('  Cannot sort: {}'.format(err))
'''RESULTS:
    Equality: False True
Identity: False True
Ordered by value:
  Cannot sort: '<' not supported between instances of 'BugStatus' and 'BugStatus'

Equality: False True
Identity: False True
Ordered by value:
  Cannot sort: '<' not supported between instances of 'BugStatus' and 'BugStatus'
'''
#4 IntEnum for integer elements
import enum

class BugStatus(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

print('Ordered by value:')
print('\n'.join('  ' + s.name for s in sorted(BugStatus)))

'''RESULTS:
    Ordered by value:
  fix_released
  fix_committed
  in_progress
  wont_fix
  invalid
  incomplete
  new
'''

#5 enum pragrammatic create

import enum

BugStatus = enum.Enum(
        value = 'BugStatus',
        names = ('fix_released fix_committed in_progress '
            'wont_fix invalid incomplete new'),
)

print('Member: {}'.format(BugStatus.new))
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))

'''RESULTS:
    Member: BugStatus.new
fix_released    = 1
fix_committed   = 2
in_progress     = 3
wont_fix        = 4
invalid         = 5
incomplete      = 6
new             = 7
'''

#6  enum with tuple or dict

import enum

BugStatus = enum.Enum(
        value = 'BugStatus',
        names = [
            ('new', 7),
            ('incomplete', 6),
            ('invalid', 5),
            ('wont_fix', 4),
            ('in_progress', 3),
            ('fix_committed', 2),
            ('fix_released', 1),
        ],
)

print('All members:')
for status in BugStatus:
    print('{:15} {}'.format(status.name, status.value))

'''RESULTS:
    All members:
new             7
incomplete      6
invalid         5
wont_fix        4
in_progress     3
fix_committed   2
fix_released    1
'''

#7 values as are tuples

import enum

class BugStatus(enum.Enum):
    new = (7, ['incomplete',
               'invalid',
               'wont_fix',
               'in_progress'])
    incomplete = (6, ['new', 'wont_fix'])
    invalid = (5, ['new'])
    wont_fix = (4, ['new'])
    in_progress = (3, ['new', 'fix_committed'])
    fix_commited = (2, ['in_progress', 'fix_released'])
    fix_released = (1, ['new'])

    def __init__(self, num, transitions):
        self.num = num
        self.transitions = transitions

    def can_transition(self, new_state):
        return new_state.name in self.transitions

print('Name:', BugStatus.in_progress)
print('Value:', BugStatus.in_progress.value)
print('Custom attribute:', BugStatus.in_progress.transitions)
print('Using attribute:',
        BugStatus.in_progress.can_transition(BugStatus.new))

'''RESULTS:
    Name: BugStatus.in_progress
Value: (3, ['new', 'fix_committed'])
Custom attribute: ['new', 'fix_committed']
Using attribute: True
'''

#8 values as are dicts

import enum

class BugStatus(enum.Enum):
    new = {
            'num': 7,
            'transitions': [
                'incomplete',
                'invalid',
                'wont_fix',
                'in_progress',
            ],
    }
    incomplete = {
            'num': 6,
            'transitions': ['new', 'wont_fix'],
    }
    invalid = {
            'num': 5,
            'transitions': ['new'],
    }
    wont_fix = {
            'num': 4,
            'transitions': ['new'],
    }
    in_progress = {
            'num': 3,
            'transitions': ['new', 'fix_committed'],
    }
    fix_committed = {
            'num': 2,
            'transitions': ['in_progress', 'fix_released'],
    }
    fix_released = {
            'num': 1,
            'transitions': ['new'],
    }

    def __init__(self, vals):
        self.num = vals['num']
        self.transitions = vals['transitions']

    def can_transition(self, new_state):
        return new_state.name in self.transitions

print('Name:', BugStatus.in_progress)
print('Value:', BugStatus.in_progress.value)
print('Custom attribute:', BugStatus.in_progress.transitions)
print('Using attribute:',
        BugStatus.in_progress.can_transition(BugStatus.new))

'''RESULTS:
    Name: BugStatus.in_progress
Value: {'num': 3, 'transitions': ['new', 'fix_committed']}
Custom attribute: ['new', 'fix_committed']
Using attribute: True
'''
