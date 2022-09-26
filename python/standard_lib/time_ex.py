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
print()
'''RESULTS:
Earliest  : 0001-01-01
Latest    : 9999-12-31
Resolution: 1 day, 0:00:00
'''

#12 replace()

import datetime

d1 = datetime.date(2038, 3, 29)
print('d1:', d1.ctime())

d2 = d1.replace(year=2028)
print('d2:', d2.ctime())
print()

'''RESULTS:
d1: Mon Mar 29 00:00:00 2038
d2: Wed Mar 29 00:00:00 2028
'''

#13 timedelta()

import datetime

print('microseconds:', datetime.timedelta(microseconds=1))
print('milliseconds:', datetime.timedelta(milliseconds=1))
print('seconds     :', datetime.timedelta(seconds=1))
print('minutes     :', datetime.timedelta(minutes=1))
print('hours       :', datetime.timedelta(hours=1))
print('days        :', datetime.timedelta(days=1))
print('weeks       :', datetime.timedelta(weeks=1))

'''RESULTS:
microseconds: 0:00:00.000001
milliseconds: 0:00:00.001000
seconds     : 0:00:01
minutes     : 0:01:00
hours       : 1:00:00
days        : 1 day, 0:00:00
weeks       : 7 days, 0:00:00
'''

#14 datetime math

import datetime

today = datetime.date.today()
print('Today    :', today)

one_day = datetime.timedelta(days=1)
print('One day  :', one_day)

yesterday = today - one_day
print('Yesterday:', yesterday)

tomorrow = today + one_day
print('Tomorrow :', tomorrow)

print()
print('tomorrow - yesterday:', tomorrow - yesterday)
print('yesterday - tomorrow:', yesterday - tomorrow)
print()
'''RESULTS:
Today    : 2022-09-23
One day  : 1 day, 0:00:00
Yesterday: 2022-09-22
Tomorrow : 2022-09-24

tomorrow - yesterday: 2 days, 0:00:00
yesterday - tomorrow: -2 days, 0:00:00
'''

#15 float days

import datetime

one_day = datetime.timedelta(days=1)
print('1 day     :', one_day)
print('5 days    :', one_day * 5)
print('1.5 days  :', one_day * 1.5)
print('1/4 day   :', one_day / 4)

# Keep one hour for lunch
work_day = datetime.timedelta(hours=7)
meeting_length = datetime.timedelta(hours=1)
print('meetings per day :', work_day / meeting_length)

'''RESULTS:
1 day     : 1 day, 0:00:00
5 days    : 5 days, 0:00:00
1.5 days  : 1 day, 12:00:00
1/4 day   : 6:00:00
meetings per day : 7.0
'''

#16 Comparing

import datetime
import time

print()
print('Times:')
t1 = datetime.time(12, 55, 0)
print(' t1:', t1)
t2 = datetime.time(13, 5, 0)
print(' t2:', t2)
print('t1 < t2:', t1 < t2)
print()
print('Dates:')
d1 = datetime.date.today()
print('d1:', d1)
d2 = datetime.date.today() + datetime.timedelta(days=1)
print(' d2:', d2)
print(' d1 > d2:', d1 > d2)
print()
'''RESULTS:
Times:
 t1: 12:55:00
 t2: 13:05:00
t1 < t2: True

Dates:
d1: 2022-09-23
 d2: 2022-09-24
 d1 > d2: False
'''

#17 datetime it is date and time

import datetime

print('Now    :', datetime.datetime.now())
print('Today  :', datetime.datetime.today())
print('UTC Now:', datetime.datetime.utcnow())
print()

FIELDS = [
        'year', 'month', 'day',
        'hour', 'minute', 'second',
        'microsecond',
]

d = datetime.datetime.now()
for attr in FIELDS:
    print('{:15}: {}'.format(attr, getattr(d, attr)))

'''RESULTS:
Now    : 2022-09-23 03:42:45.478778
Today  : 2022-09-23 03:42:45.478801
UTC Now: 2022-09-23 01:42:45.478821

year           : 2022
month          : 9
day            : 23
hour           : 3
minute         : 42
second         : 45
microsecond    : 478843
'''

#18 combine()

import datetime

t = datetime.time(1, 2, 3)
print('t:', t)

d = datetime.date.today()
print('d:', d)

dt = datetime.datetime.combine(d, t)
print('dt:', dt)
print()
'''RESULTS:
t: 01:02:03
d: 2022-09-23
dt: 2022-09-23 01:02:03
'''

#19 strftime()

import datetime

format = "%a %b %d %H:%M:%S %Y"

today = datetime.datetime.today()
print('ISO:', today)
 
s = today.strftime(format)
print('strftime:', s)

d = datetime.datetime.strptime(s, format)
print('strptime:', d.strftime(format))

'''RESULTS:
ISO: 2022-09-23 03:53:44.883965
strftime: Fri Sep 23 03:53:44 2022
strptime: Fri Sep 23 03:53:44 2022
'''

#20 format()

import datetime

today = datetime.datetime.today()
print('ISO :', today)
print('format(): {:%a %b %d %H:%M:%S %Y}'.format(today))

'''RESULTS:
ISO : 2022-09-26 03:05:53.863057
format(): Mon Sep 26 03:05:53 2022
'''

#21 timezone

import datetime

print()
min6 = datetime.timezone(datetime.timedelta(hours=-6))
plus6 = datetime.timezone(datetime.timedelta(hours=6))
d = datetime.datetime.now(min6)

print(min6, ':', d)
print(datetime.timezone.utc, '      :', d.astimezone(datetime.timezone.utc))
print(plus6, ':', d.astimezone(plus6))

d_system = d.astimezone()
print(d_system.tzinfo, '     :', d_system)

