"""Statistics about."""

#1 mean()

from statistics import *

data = [1, 2, 2, 5, 10, 12]

print('{:0.2f}'.format(mean(data)))

'''RESULTS:
5.33
'''

#2 mode()

from statistics import *

#data = [1, 2, 2, 5, 10, 12]
data = ['jill', 'clare', 'clare', 'jain', 'ada', 'felicia', 'gortenzia']

print(mode(data))

'''RESULTS:
#2
clare
'''

#3 median()

from statistics import *

data = [1, 2, 2, 5, 10, 12]

print('median      : {:0.2f}'.format(median(data)))
print('low         : {:0.2f}'.format(median_low(data)))
print('high        : {:0.2f}'.format(median_high(data)))

'''RESULTS:
median      : 3.50  # 2+5=7, 7/2=3.5
low         : 2.00
high        : 5.00  # bigger from 2 and 5
'''

#4  median_grouped()

from statistics import *

data = [10, 20, 30, 40]

print('1: {:0.2f}'.format(median_grouped(data, interval=1)))
print('2: {:0.2f}'.format(median_grouped(data, interval=2)))
print('3: {:0.2f}'.format(median_grouped(data, interval=3)))

'''RESULTS:
1: 29.50
2: 29.00
3: 28.50
'''

#5 variance()
