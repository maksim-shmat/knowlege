"""Date and time about."""

######1 datetime now()

from datetime import datetime

datetime_1 = datetime.now()
print(str(datetime_1))

######2 datetime now() with timezone argument

from datetime import datetime
import pytz

tz = pytz.timezone('US/Pacific')
datetime_1 = datetime.now(tz)
print(str(datetime_1))

######3 Format Datetime in python

from datetime import datetime

dt = datetime.now()

print(dt)
print('\nDirectives\n----------------')
print(dt.strftime('Weekday short version : %a'))
print(dt.strftime('Weekday full version  : %A'))
print(dt.strftime('Weekday as a number   : %w'))
print(dt.strftime('Day of month          : %d'))
print(dt.strftime('Month Name short ver  : %b'))
print(dt.strftime('Month Name full ver   : %B'))
print(dt.strftime('Month as a number     : %m'))
print(dt.strftime('Year short version    : %y'))
print(dt.strftime('Year full version     : %Y'))
print(dt.strftime('Hour (00-23)          : %H'))
print(dt.strftime('Hour (00-11)          : %I'))
print(dt.strftime('AM/PM                 : %p'))
print(dt.strftime('Minute                : %M'))
print(dt.strftime('Second                : %S'))

print('\nFormatted Date String\n-----------------')
print(dt.strftime('%a %d-%m-%Y'))
print(dt.strftime('%a %d/%m/%Y'))
print(dt.strftime('%a %d/%m/%y'))
print(dt.strftime('%A %d-%m-%y'))
print(dt.strftime('%A %d-%m-%Y, %H:%M:%S'))
print(dt.strftime('%X %x'))

######4
