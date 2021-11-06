"""CSV about."""

######1 Read csv vile using python csv package

import csv

with open('jill.csv', 'r') as csvfile:
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

######2 Read csv file using python pandas library

#import pandas as pd

#df = pd.read_csv("jill.csv")
#print(df)

######3 Read csv file using for loop and string split operation

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

######4
