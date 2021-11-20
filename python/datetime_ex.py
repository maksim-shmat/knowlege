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

######4 Check if one date-time is compare other date-time

import datetime

# date and time in yyyy/mm/dd hh:mm:ss format
d1 = datetime.datetime(2020, 5, 13, 22, 50, 55)
d2 = datetime.datetime(2020, 8, 13, 22, 50, 55)
d3 = datetime.datetime(2020, 7, 13, 22, 50, 55)

print(d1 > d2)
print(d2 > d3)
print(d1 < d2)
print(d1 == d3)
print(d1.date() == d2.date())  # only dates of date-time objects
print(d1.time() == d2.time())  # only time of date-time objects

######5 Convert date and time string to datetime object

from datetime import datetime

dt1 = datetime.fromisoformat('2020-11-18')
print(type(dt1), dt1)

dt2 = datetime.fromisoformat('2020-11-18T00:-05:23')
print(type(dt2), dt2)

dt3 = datetime.fromisoformat('2020-11-18 00:05:23.283')
print(type(dt3), dt3)

dt4 = datetime.fromisoformat('2020-11-18 00:05:23.283+00:00')
print(type(dt4), dt4)

dt5 = datetime.fromisoformat('2020-11-18T00:05:23+04:00')
print(type(dt5), dt5)

### access the individual parts

from datetime import datetime

dt = datetime.fromisoformat('2020-11-18 17:05:23.283')

# print hours
print(dt.strftime("%H"))

# print weekday
print(dt.strftime("%A"))

######6 Convert date string to date object

from datetime import date

# convert string to date object
dateStr = '2020-11-18'
date1 = date.fromisoformat(dateStr)

# access date object
print(date1)
print(date1.strftime('%Y'))  # year
print(date1.strftime('%B'))  # month name
print(date1.strftime('%d'))  # day of month

######7 Convert Time String to time object

from datetime import time

time2 = time.fromisoformat('17:15:23')
print(type(time2), time2)

time3 = time.fromisoformat('17:15:23.283')
print(type(time3), time3)

time4 = time.fromisoformat('17:15:23.283+00:00')
print(type(time4), time4)

time5 = time.fromisoformat('17:15:23+04:00')
print(type(time5), time5)

######8 Convert datetime to string

import datetime

# get current date and time
x = datetime.datetime.now()

# convert date and time to string
dateTimeStr = str(x)

# print the date and time string
print(dateTimeStr)

# print the type of dateTimeStr
print(type(dateTimeStr))

# get the date from datetime string using index slicing
print(dateTimeStr[:10])

### convert to string with isoformat

import datetime

x = datetime.datetime(2020, 1, 1, 12, 30, 59, 0)

# convert the datetime object to string
datetimeStr = str(x)
print(datetimeStr)

# print the iso format of datetime object
print(x.isoformat(' '))

### Format datetime string

import datetime

x = datetime.datetime(2020, 1, 1, 12, 30, 59, 0)

# convert the datetime object to string of specific format
datetimeStr = x.strftime("%Y %B, %A %w, %H hours %M minutes")
print(datetimeStr)

######9 Get month as number

import datetime

d = datetime.datetime.now()
print(d)
print(d.strftime("%m"))

### get month number of specfic date

import datetime

d = datetime.datetime(2019, 8, 12)
print(d)
print(d.strftime("%m"))

######10 Get month name full version of current date

import datetime

# get current time
d = datetime.datetime.now()

# print date
print(d)

# get month name full vetsion
print(d.strftime("%B"))

### get month name full vetrsion of specific date

import datetime

# set specific date

d = datetime.datetime(2019, 8, 12)

# print date
print(d)

# get month name full vetsion
print(d.strftime("%B"))

######11
