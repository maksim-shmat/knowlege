"""Sqlite3 about."""

######1 Create table only if it does not exist

import sqlite3

# create a connection object using sqlite3
conn = sqlite3.connect('jill.db')

# use connect object to get cursor to the database
c = conn.cursor()

# create table
c.execute('''CREATE TABLE IF NOT EXISTS students
        (rollno real, name text, class real)''')

# commit the changes to db
conn.commit()
# close the connection
conn.close()

######2 Check if table exists in sqlite3 database

import sqlite3

conn = sqlite3.connect('mysqlite.db')
c = conn.cursor()

# get the count of tables with the name
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='students1' ''')  # for check in memory(RAM) change for sqlite_temp_master

# if the count is 1, then table exists
if c.fetchone()[0]==1 :
    print('Table exists.')
else:
    print('Table does not exist.')

# commit the changes to dg
conn.commit()
# close the connection
conn.close()

######3 Insert Row in sqlite3 table and check if insertion is successful

import sqlite3

conn = sqlite3.connect('jill.db')
c = conn.cursor()

# create table
c.execute('''CREATE TABLE IF NOT EXISTS students
        (rollno real, name text, class real)''')

c.execute('''INSERT INTO students
        VALUES(1, 'Glen', 8)''')

print(c.lastrowid)  # if you see non-zero, then data inserted

conn.commit()
conn.close()

<<<<<<< HEAD
######4 Insert multimple rows into sqlite table
=======
######4 Select rows from sqlite3 table
>>>>>>> fb847ebcd397dbe6bd0f0a9612bb1f916f881f71

import sqlite3

conn = sqlite3.connect('jill.db')
c = conn.cursor()

<<<<<<< HEAD
records = [(1, 'Glen', 8),
           (2, 'Elliot', 9),
           (3, 'Bob', 7)]

c.executemany('INSERT INTO students VALUES(?,?,?);',records);
print('We have inserted', c.rowcount, 'records to the table.')
=======
c.execute('''SELECT * FROM students;''')

rows = c.fetchall()
for row in rows:
    print(row)
>>>>>>> fb847ebcd397dbe6bd0f0a9612bb1f916f881f71

conn.commit()
conn.close()

<<<<<<< HEAD
=======
### Select from sqlite3 table with WHERE clause
import sqlite3

conn = sqlite3.connect('jill.db')
c = conn.cursor()

c.execute('''SELECT * FROM students WHERE name="Elliot";''')

rows = c.fetchall()

for row in rows:
    print(row)
conn.commit()
conn.close()

>>>>>>> fb847ebcd397dbe6bd0f0a9612bb1f916f881f71
######5
