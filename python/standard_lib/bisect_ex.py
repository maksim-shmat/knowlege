"""bisect it is sort."""

#1 keep sorted positions
import bisect

values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New Pos Contents')
print('--- --- --------')

l = []
for  i in values:
    position = bisect.bisect(l, i)
    bisect.insort(l, i)
    print('{:3} {:3}'.format(i, position), l)

'''RESULTS:
New Pos Contents
--- --- --------
 14   0 [14]
 85   1 [14, 85]
 77   1 [14, 77, 85]
 26   1 [14, 26, 77, 85]
 50   2 [14, 26, 50, 77, 85]
 45   2 [14, 26, 45, 50, 77, 85]
 66   4 [14, 26, 45, 50, 66, 77, 85]
 79   6 [14, 26, 45, 50, 66, 77, 79, 85]
 10   0 [10, 14, 26, 45, 50, 66, 77, 79, 85]
  3   0 [3, 10, 14, 26, 45, 50, 66, 77, 79, 85]
 84   9 [3, 10, 14, 26, 45, 50, 66, 77, 79, 84, 85]
 77   8 [3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]
  1   0 [1, 3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]
'''

#2 repeated values keep to right with insort_right() == insort(), or keep
# to the left with insort_left()
import bisect

values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New Pos Contents')
print('--- --- --------')

l = []
for i in values:
    position = bisect.bisect_left(l, i)
    bisect.insort_left(l, i)
    print('{:3} {:3}'.format(i, position), l)

'''RESULTS:
New Pos Contents
--- --- --------
 14   0 [14]
 85   1 [14, 85]
 77   1 [14, 77, 85]
 26   1 [14, 26, 77, 85]
 50   2 [14, 26, 50, 77, 85]
 45   2 [14, 26, 45, 50, 77, 85]
 66   4 [14, 26, 45, 50, 66, 77, 85]
 79   6 [14, 26, 45, 50, 66, 77, 79, 85]
 10   0 [10, 14, 26, 45, 50, 66, 77, 79, 85]
  3   0 [3, 10, 14, 26, 45, 50, 66, 77, 79, 85]
 84   9 [3, 10, 14, 26, 45, 50, 66, 77, 79, 84, 85]
 77   7 [3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]  # 77 on the left
  1   0 [1, 3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]
'''
