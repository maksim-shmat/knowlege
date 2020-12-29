""" sqlite 3 have own site."""

import sqlite3

# Connects to the company database. If no such database exists, it will
# create one. The file will be stored in the same folder as teh program.
with sqlite3.connect("company.db") as db:
    cursor=db.cursor()


