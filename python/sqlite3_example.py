""" sqlite 3 have own site."""

import sqlite3

# Connects to the company database. If no such database exists, it will
# create one. The file will be stored in the same folder as teh program.
with sqlite3.connect("company.db") as db:
    cursor=db.cursor()

# Create a table called employees which has four fields(id, name, dept and
# salary). It specifies the data type for each field, defines which field is
# the primary key and which fields cannot be left blank. The triple speech
# marks allow the code to be split over several lines to make it easier to 
# read rather than having it all displayed in one line.

cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
        id integer PRIMARY KEY,
        name text NOT NULL,
        dept text NOT NULL,
        salary integer);""")

