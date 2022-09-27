"""calendar about."""

#1 prmonth()

import calendar

#c = calendar.TextCalendar(calendar.SUNDAY)  # for USA
c = calendar.TextCalendar()  # default start with Monday
c.prmonth(2017, 7)

'''RESULTS:
     July 2017
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

     July 2017
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
'''

#2 yeardays2calendar()

import calendar
import pprint

cal = calendar.Calendar()
cal_data = cal.yeardays2calendar(2017, 3)
print('len(cal_data)      :', len(cal_data))

top_months = cal_data[0]
print('len(top_months)    :', len(top_months))

first_month = top_months[0]
print('len(first_month)   :', len(first_month))

print('first_month:')
pprint.pprint(first_month, width=65)

'''RESULTS:
len(cal_data)      : 4
len(top_months)    : 3
len(first_month)   : 6
first_month:
[[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 6)],
 [(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)],
 [(9, 0), (10, 1), (11, 2), (12, 3), (13, 4), (14, 5), (15, 6)],
 [(16, 0), (17, 1), (18, 2), (19, 3), (20, 4), (21, 5), (22, 6)],
 [(23, 0), (24, 1), (25, 2), (26, 3), (27, 4), (28, 5), (29, 6)],
 [(30, 0), (31, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]]
'''

#3 formatyear()

import calendar

cal = calendar.TextCalendar()
print(cal.formatyear(2022, 2, 1, 1, 3))

'''RESULTS:
                          2022

      January               February               March
Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
                1  2      1  2  3  4  5  6      1  2  3  4  5  6
 3  4  5  6  7  8  9   7  8  9 10 11 12 13   7  8  9 10 11 12 13
10 11 12 13 14 15 16  14 15 16 17 18 19 20  14 15 16 17 18 19 20
17 18 19 20 21 22 23  21 22 23 24 25 26 27  21 22 23 24 25 26 27
24 25 26 27 28 29 30  28                    28 29 30 31
31

       April                  May                   June
Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
             1  2  3                     1         1  2  3  4  5
 4  5  6  7  8  9 10   2  3  4  5  6  7  8   6  7  8  9 10 11 12
11 12 13 14 15 16 17   9 10 11 12 13 14 15  13 14 15 16 17 18 19
18 19 20 21 22 23 24  16 17 18 19 20 21 22  20 21 22 23 24 25 26
25 26 27 28 29 30     23 24 25 26 27 28 29  27 28 29 30
                      30 31

        July                 August              September
Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
             1  2  3   1  2  3  4  5  6  7            1  2  3  4
 4  5  6  7  8  9 10   8  9 10 11 12 13 14   5  6  7  8  9 10 11
11 12 13 14 15 16 17  15 16 17 18 19 20 21  12 13 14 15 16 17 18
18 19 20 21 22 23 24  22 23 24 25 26 27 28  19 20 21 22 23 24 25
25 26 27 28 29 30 31  29 30 31              26 27 28 29 30

      October               November              December
Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
                1  2      1  2  3  4  5  6            1  2  3  4
 3  4  5  6  7  8  9   7  8  9 10 11 12 13   5  6  7  8  9 10 11
10 11 12 13 14 15 16  14 15 16 17 18 19 20  12 13 14 15 16 17 18
17 18 19 20 21 22 23  21 22 23 24 25 26 27  19 20 21 22 23 24 25
24 25 26 27 28 29 30  28 29 30              26 27 28 29 30 31
31
'''

#4 locale

import calendar

print()
c = calendar.LocaleTextCalendar(locale='en_US')
c.prmonth(2017, 7)

print()

c = calendar.LocaleTextCalendar(locale='fr_FR')
c.prmonth(2022, 8)

print()

c = calendar.LocaleTextCalendar(locale='be_BY')
c.prmonth(2023, 1)

print()

'''RESULTS:
     July 2017
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31

     août 2022
lu ma me je ve sa di
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

   студзеня 2023
Па Аў Ср Чц Пя Су Ня
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
'''

#5 monthcalendar()

import calendar

import pprint

print()
pprint.pprint(calendar.monthcalendar(2022, 10))
print()

'''RESULTS:
[[0, 0, 0, 0, 0, 1, 2],
 [3, 4, 5, 6, 7, 8, 9],
 [10, 11, 12, 13, 14, 15, 16],
 [17, 18, 19, 20, 21, 22, 23],
 [24, 25, 26, 27, 28, 29, 30],
 [31, 0, 0, 0, 0, 0, 0]]
'''

#6 if meeting in every !second thursday

import calendar
import sys

#year = int(sys.argv[1])

# Show every month
for month in range(1, 13):
    # count week
   # c = calendar.monthcalendar(year, month)
    c = calendar.monthcalendar(2022, month)
    first_week = c[0]
    second_week = c[1]
    third_week = c[2]

    if first_week[calendar.THURSDAY]:
        meeting_date = second_week[calendar.THURSDAY]
    else:
        meeting_date = third_week[calendar.THURSDAY]

    print('{:>3}: {:>2}'.format(calendar.month_abbr[month],
                                meeting_date))

'''RESULTS:
Jan: 13
Feb: 10
Mar: 10
Apr: 14
May: 12
Jun:  9
Jul: 14
Aug: 11
Sep:  8
Oct: 13
Nov: 10
Dec:  8
'''
