"""CSV about."""

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

with open('jill.csv') as fp:
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

results:
    0 ONE
    1 TWO
    3 THREE

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

