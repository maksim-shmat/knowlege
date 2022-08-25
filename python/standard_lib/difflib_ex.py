"""difflib() about."""

import difflib
from difflib_data import *

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print('\n'.join(diff))

#2 unified_diff()

import difflib
from difflib_data import *

diff = difflib.unified_diff(  # or difflib.context_diff
        text1_lines,
        text2_lines,
        lineterm='',
)

print('\n'.join(list(diff)))

#3 ignore spaces or punctuation in differents files with SequenceMatcher()

from difflib import SequenceMatcher

def show_results(match):
    print(' a = {}'.format(match.a))
    print(' b = {}'.format(match.b))
    print(' size = {}'.format(match.size))
    i, j, k = match
    print(' A[a:a+size] = {!r}'.format(A[i:i + k]))
    print(' B[b:b+size] = {!r}'.format(B[j:j + k]))

A = " abcd"
B = "abcd abcd"

print('A = {!r}'.format(A))
print('B = {!r}'.format(B))

print('\nWithout junk detection:')
s1 = SequenceMatcher(None, A, B)
match1 = s1.find_longest_match(0, len(A), 0, len(B))
show_results(match1)

print('\nTreat spaces as junk:')
s2 = SequenceMatcher(lambda x: x == " ", A, B)

match2 = s2.find_longest_match(0, len(A), 0, len(B))
show_results(match2)

#4 Work with hashable types for difflib.get_opcodes()
# 'replace'  change a[i1:i2] to b[j1:j2]
# 'delete'   delete a[i1:i2]
# 'insert'   insert b[j1:j2] into a[i1:i2]
# 'equal'  

import difflib

s1 = [1, 2, 3, 5, 6, 4]
s2 = [2, 3, 5, 4, 6, 1]

print('Initial data:')
print('s1 = ', s1)
print('s2 = ', s2)
print('s1 == s2: ', s1 == s2)
print()

matcher = difflib.SequenceMatcher(None, s1, s2)
for tag, i1, i2, j1, j2 in reversed(matcher.get_opcodes()):
    if tag == 'delete':
        print('Remove {} from positions [{}:{}]'.format(
            s1[i1:i2], i1, i2))
        print(' before = ', s1)
        del s1[i1:i2]

    elif tag == 'equal':
        print('s1[{}:{}] and s2[{}:{}] are the same'.format(
            i1, i2, j1, j2))
        
    elif tag == 'insert':
        print('Insert {} from s2[{}:{}] into s1 at {}'.format(
            s2[j1:j2], j1, j2, i1))
        print(' before =', s1)
        s1[i1:i2] = s2[j1:j2]

    elif tag == 'replace':
        print(('Replace {} from s1[{}:{}] '
               'with {} from s2[{}:{}]').format(
                   s1[i1:i2], i1, i2, s2[j1:j2], j1, j2))
        print(' before = ', s1)
        s1[i1:i2] = s2[j1:j2]
    print(' after = ', s1, '\n')
print('s1 == s2: ', s1 == s2)

#
