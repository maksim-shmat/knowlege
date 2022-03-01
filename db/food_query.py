"""That`s file with food.db."""

import sqlite3, sys

# If you import sys, that you trust their database, I mean sql-injection about.
conn = sqlite3.connect('food.db')
curs = conn.cursor()
query = 'SELECT * FROM food WHERE ' + sys.argv[1]
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print('{}: {}'.format(*pair))
    print()
