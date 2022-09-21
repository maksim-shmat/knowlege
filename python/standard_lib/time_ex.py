"""Time about."""

#1 time()

import time

print('The time is:', time.time())

'''RESULTS:
The time is: 1663721415.8433313  # from midnight Jan 1 1970
'''

#2 ctime()

import time

print('The time is      :', time.ctime())
later = time.time() + 15
print('15 secs from now :', time.ctime(later))

'''RESULTS:
The time is      : Wed Sep 21 03:54:10 2022
15 secs from now : Wed Sep 21 03:54:25 2022
'''

#3 monotonic()

import time

start = time.monotonic()
time.sleep(0.1)
end = time.monotonic()
print('start : {:>9.2f}'.format(start))
print('end   : {:>9.2f}'.format(end))
print('span  : {:>9.2f}'.format(end - start))

'''RESULTS:
start : 878571.97
end   : 878572.07
span  :      0.10
'''

#4 struct_time

import time

def show_struct(s):
    print('  tm_year :', s.tm_year)
    print('  tm_mon  :', s.tm_mon)
    print('  tm_mday :', s.tm_mday)
    print('  tm_hour :', s.tm_hour)
    print('  tm_min  :', s.tm_min)
    print('  tm_sec  :', s.tm_sec)
    print('  tm_wday :', s.tm_wday)
    print('  tm_yday :', s.tm_yday)
    print('  tm_isdst:', s.tm_isdst)

print('gmtime:')
show_struct(time.gmtime())
print('\nlocaltime:')
show_struct(time.localtime())
print('\nmktime:', time.mktime(time.localtime()))

'''RESULTS:
gmtime:
 tm_year : 2022
  tm_mon  : 9
  tm_mday : 21
  tm_hour : 1
  tm_min  : 57
  tm_sec  : 48
  tm_wday : 2
  tm_yday : 264
  tm_isdst: 0

localtime:
  tm_year : 2022
  tm_mon  : 9
  tm_mday : 21
  tm_hour : 4
  tm_min  : 57
  tm_sec  : 48
  tm_wday : 2
  tm_yday : 264
  tm_isdst: 0

mktime: 1663725468.0
'''

#5 
