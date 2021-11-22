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

######2
