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

#5 tzset()

import time
import os

def show_zone_info():
    print('  TZ    :', os.environ.get('TZ', '(not set)'))
    print('  tzname:', time.tzname)
    print('  Zone  : {} ({})'.format(
        time.timezone, (time.timezone / 3600)))
    print('  DST   :', time.daylight)
    print('  Time  :', time.ctime())
    print()

print('Default:')
show_zone_info()

ZONES = [
        'GMT',
        'Europe/Amsterdam',
]

for zone in ZONES:
    os.environ['TZ'] = zone
    time.tzset()
    print(zone, ':')
    show_zone_info()

'''RESULTS:
Default:
  TZ    : (not set)
  tzname: ('+03', '+03')
  Zone  : -10800 (-3.0)
  DST   : 0

GMT :
  TZ    : GMT
  tzname: ('GMT', 'GMT')
  Zone  : 0 (0.0)
  DST   : 0

Europe/Amsterdam :
  TZ    : Europe/Amsterdam
  tzname: ('CET', 'CEST')
  Zone  : -3600 (-1.0)
  DST   : 1
'''

#6 strptime() strftime() string to/from time

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

now = time.ctime(11663721415.843331)
print('Now:', now)

parsed = time.strptime(now)
print('\nParsed:')
show_struct(parsed)

print('\nFormatted:',
        time.strftime('%a %b %H:%M:%S %Y', parsed))

'''RESULTS:
rsed:
  tm_year : 2339
  tm_mon  : 8
  tm_mday : 11
  tm_hour : 20
  tm_min  : 36
  tm_sec  : 55
  tm_wday : 4
  tm_yday : 223
  tm_isdst: -1

Formatted: Fri Aug 20:36:55 2339
'''

#7 datetime

import datetime

t = datetime.time(1, 2, 3)
print(t)
print('hour        :', t.hour)
print('minute      :', t.minute)
print('second      :', t.second)
print('microsecond :', t.microsecond)
print('tzinfo      :', t.tzinfo)

'''RESULTS:
hour        : 1
minute      : 2
second      : 3
microsecond : 0
tzinfo      : None
'''

#8 datetime time minmax

import datetime

print()
print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)

'''RESULTS:
Earliest  : 00:00:00
Latest    : 23:59:59.999999
Resolution: 0:00:00.000001
'''

#9 today()

import datetime

today = datetime.date.today()
print(today)
print('ctime  :', today.ctime())
tt = today.timetuple()
print('tuple  : tm_year  =', tt.tm_year)
print('         tm_mon   =', tt.tm_mon)
print('         tm_mday  =', tt.tm_mday)
print('         tm_hour  =', tt.tm_hour)
print('         tm_min   =', tt.tm_min)
print('         tm_sec   =', tt.tm_sec)
print('         tm_wday  =', tt.tm_wday)
print('         tm_yday  =', tt.tm_yday)
print('         tm_isdst =', tt.tm_isdst)
print('ordinal:', today.toordinal())
print('Year   :', today.year)
print('Mon    :', today.month)
print('Day    :', today.day)

'''RESULTS:
2022-09-22
ctime  : Thu Sep 22 00:00:00 2022
tuple  : tm_year  = 2022
         tm_mon   = 9
         tm_mday  = 22
         tm_hour  = 0
         tm_min   = 0
         tm_sec   = 0
         tm_wday  = 3
         tm_yday  = 265
         tm_isdst = -1
ordinal: 738420
Year   : 2022
Mon    : 9
Day    : 22
'''

#10 fromordinal() fromtimestamp()

import datetime
import time

o = 733114
print('o:', o)
print('fromordinal(o):', datetime.date.fromordinal(o))
t = time.time()
print('t:', t)
print('fromtimestamp(t):', datetime.date.fromtimestamp(t))

'''RESULTS:
o: 733114
fromordinal(o): 2008-03-13
t: 1663811501.3569252
fromtimestamp(t): 2022-09-22
'''

#11 datetime date min max

import datetime

print()
print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)

'''RESULTS:
Earliest  : 0001-01-01
Latest    : 9999-12-31
Resolution: 1 day, 0:00:00
'''

#12 replace()
