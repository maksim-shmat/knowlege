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

######3
