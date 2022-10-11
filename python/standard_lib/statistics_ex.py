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

from statistics import *
import subprocess

def get_line_lengths():
    cmd = 'wc -l ../[a-z]*/*.py'
    out = subprocess.check_output(
            cmd, shell=True).decode('utf-8')
    for line in out.splitlines():
        parts = line.split()
        if parts[1].strip().lower() == 'total':
            break
        nlines = int(parts[0].strip())
        if not nlines:
            continue
        yield (nlines, parts[1].strip())


data = list(get_line_lengths())

lengths = [d[0] for d in data]
sample = lengths[::2]

print('Basic statistics:')
print('  count      : {:3d}'.format(len(lengths)))
print('  min        : {:6.2f}'.format(min(lengths)))
print('  max        : {:6.2f}'.format(max(lengths)))
print('  mean       : {:6.2f}'.format(mean(lengths)))

print('\nPopulation variance:')
print('  pstdev     : {:6.2f}'.format(pstdev(lengths)))
print('  pvariance  : {:6.2f}'.format(pvariance(lengths)))

print('\nEstimated variance for sample:')
print('  count      : {:3d}'.format(len(sample)))
print('  stdev      : {:6.2f}'.format(stdev(sample)))
print('  variance   : {:6.2f}'.format(variance(sample)))

'''RESULTS:
Basic statistics:
  count      : 177
  min        :   1.00
  max        : 818.00
  mean       :  89.92

Population variance:
  pstdev     : 143.48
  pvariance  : 20587.07

Estimated variance for sample:
  count      :  89
  stdev      : 151.79
  variance   : 23040.89
'''
