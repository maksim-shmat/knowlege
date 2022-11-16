"""CSV about."""

'''
#1 Read csv vile using python csv package

import csv


filename = '/home/jack/django2/knowlege/python/jill.csv'
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.__next__()
    print('Field Names\n--------------')
    for field in fields:
        print("%8s"%field, end='')
    print('\nRows\n-------------------')
    for row in csvreader:
        for col in row:
            print("%8s"%col, end='')
        print('\n')

#2 Read csv file using python pandas library

#import pandas as pd

#df = pd.read_csv("jill.csv")
#print(df)

#3 Read csv file using for loop and string split operation

with open('/home/jack/django2/knowlege/python/jill.csv'
) as fp:
    print('Field Names\n------------------')
    fields = fp.readline()
    for field in fields.split(','):
        print("%8s"%field, end='')

    print('Rows\n-----------------------------')
    for line in fp:
        chunks = line.split(',')
        for chunk in chunks:
            print("%8s"%chunk, end='')

#4 Read csv with indexes of headers

import csv


filename = '/home/jack/django2/knowlege/python/jill.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    print(header_row)

#5 Read header and then tail

import csv

filename = '/home/jack/django2/knowlege/python/apple.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    for row in reader:
        high = float(row[3])
        highs.append(high)
print(highs)

#5 csv_writer.py

import csv
import sys

unicode_chars = 'a¤Ç'

with open(sys.argv[1], 'wt') as f:
    writer = csv.writer(f)  # or writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)  for add quotew to output (QUOTE_ALL, QUOTE_MINIMAL, QUOTE_NONNUMERIC, QUOTE_NONE)
    writer.writerow(('Title 1', 'Title 2', 'Title 3', 'Title 4'))
    for i in range(3):
        row = (
                i + 1,
                chr(ord('a') + i),
                '08/({:02d}/07'.format(i + 1),
                unicode_chars[i],
        )
        writer.writerow(row)

print(open(sys.argv[1], 'rt').read())

#6 dialects: excel/LibreOffice, unix
# make yourself dialect

import csv

csv.register_dialect('pipes', delimiter='|')

with open('testdata.pipes', 'r') as f:
    reader = csv.reader(f, dialect='pipes')
    for row in reader:
        print(row)
'''
#7 csv dialect variations

import csv
import sys

csv.register_dialect('escaped',
                     escapechar='\\',
                     doublequote=False,
                     quoting=csv.QUOTE_NONE,
                     )
csv.register_dialect('singlequote',
                     quotechar="'",
                     quoting=csv.QUOTE_ALL,
                     )

quoting_modes = {
        getattr(csv, n): n
        for n in dir(csv)
        if n.startswith('QUOTE_')
}

TEMPLATE = """\
        Dialect: "{name}"

        delimiter   = {dl!r:<6}    skipinitialspace = {si!r}
        doublequote = {dq!r:<6}    quoting          = {qu}
        quotechar   = {qc!r:<6}    lineterminator   = {lt!r}
        escapechar  = {ec!r:<6}
    """

for name in sorted(csv.list_dialects()):
    dialect = csv.get_dialect(name)

    print(TEMPLATE.format(
        name=name,
        dl=dialect.delimiter,
        si=dialect.skipinitialspace,
        dq=dialect.doublequote,
        qu=quoting_modes[dialect.quoting],
        qc=dialect.quotechar,
        lt=dialect.lineterminator,
        ec=dialect.escapechar
    ))

    writer = csv.writer(sys.stdout, dialect=dialect)
    writer.writerow(
            ('coll', 1, '10/01/2020',
             'Special chars: " \' {} to parse'.format(
                 dialect.delimiter))
    )
    print()

'''RESULTS:

       Dialect: "escaped"

       delimiter    = ','       skipinitialspace = 0
       doublequote  = 0         qouting          = QUOTE_NONE
       quotechar    = '"'       lineterminator   = '\r\n'
       escapechar   = '\\'

coll,1,10/01/2020,Special chars: \" ' \, to parse

       Dialect: "excel"

        delimiter   = ','       skipinitialspace = False
        doublequote = True      quoting          = QUOTE_MINIMAL
        quotechar   = '"'       lineterminator   = '\r\n'
        escapechar  = None  
    
coll,1,10/01/2020,"Special chars: "" ' , to parse"

        Dialect: "excel-tab"

        delimiter   = '\t'      skipinitialspace = False
        doublequote = True      quoting          = QUOTE_MINIMAL
        quotechar   = '"'       lineterminator   = '\r\n'
        escapechar  = None  
    
coll	1	10/01/2020	"Special chars: "" ' 	 to parse"

        Dialect: "singlequote"

        delimiter   = ','       skipinitialspace = False
        doublequote = True      quoting          = QUOTE_ALL
        quotechar   = "'"       lineterminator   = '\r\n'
        escapechar  = None  
    
'coll','1','10/01/2020','Special chars: " '' , to parse'

        Dialect: "unix"

        delimiter   = ','       skipinitialspace = False
        doublequote = True      quoting          = QUOTE_ALL
        quotechar   = '"'       lineterminator   = '\n'
        escapechar  = None  
    
"coll","1","10/01/2020","Special chars: "" ' , to parse"
'''

#8 csv dialect sniffer

import csv
from io import StringIO
import textwrap

csv.register_dialect('escaped',
                     escapechar='\\',
                     doublequote=False,
                     quoting=csv.QUOTE_NONE)
csv.register_dialect('singlequote',
                     quotechar="'",
                     quoting=csv.QUOTE_ALL)

# Generate data for all accesed dialects
samples = []
for name in sorted(csv.list_dialects()):
    buffer = StringIO()
    dialect = csv.get_dialect(name)
    writer = csv.writer(buffer, dialect=dialect)
    writer.writerow(
            ('coll', 1, '20/02/2020',
             'Special chars " \' {} to parse'.format(
                 dialect.delimiter))
    )
    samples.append((name, dialect, buffer.getvalue()))

# check dialect for sample
sniffer = csv.Sniffer()
for name, expected, sample in samples:
    print('Dialect: "{}"'.format(name))
    print('In: {}'.format(sample.rstrip()))
    dialect = sniffer.sniff(sample, delimiters=',\t')
    reader = csv.reader(StringIO(sample), dialect=dialect)
    print('Parsed:\n  {}\n'.format(
          '\n  '.join(repr(r) for r in next(reader))))

'''RESULTS:
Dialect: "escaped"
In: coll,1,20/02/2020,Special chars \" ' \, to parse
Parsed:
  'coll'
  '1'
  '20/02/2020'
  'Special chars \\" \' \\'
  ' to parse'

Dialect: "excel"
In: coll,1,20/02/2020,"Special chars "" ' , to parse"
Parsed:
  'coll'
  '1'
  '20/02/2020'
  'Special chars " \' , to parse'

Dialect: "excel-tab"
In: coll	1	20/02/2020	"Special chars "" ' 	 to parse"
Parsed:
  'coll'
  '1'
  '20/02/2020'
  'Special chars " \' \t to parse'

Dialect: "singlequote"
In: 'coll','1','20/02/2020','Special chars " '' , to parse'
Parsed:
  'coll'
  '1'
  '20/02/2020'
  'Special chars " \' , to parse'

Dialect: "unix"
In: "coll","1","20/02/2020","Special chars "" ' , to parse"
Parsed:
  'coll'
  '1'
  '20/02/2020'
  'Special chars " \' , to parse'
'''
#9 csv dictreader, use strings as dicts

import csv
import sys

with open('testdata.pipes', 'rt') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

#10 csv dictwriter

import csv
import sys

fieldnames = ('Title 1', 'Title 2', 'Title 3', 'Title 4')
headers = {
        n: n
        for n in fieldnames
}
unicode_chars = 'áḃć'

with open('test.pipes', 'wt') as f:

    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(3):
        writer.writerow({
            'Title 1': i + 1,
            'Title 2': chr(ord('a') + i),
            'Title 3': '08/{:02d}/07'.format(i + 1),
            'Title 4': unicode_chars[i],
        })

print(open('test.pipes', 'rt').read())

