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

# Insert data into the employees table. The db.commit() line saves the changes
cursor.execute("""INSERT INTO employees(id,name,dept,salary)
        VALUES("1","Bob","Sales","25000")""")
db.commit()

# Allows a user to enter new data which is then inserted into the table
newID = input("Enter ID number: ")
newName = input("Enter name: ")
newDept = input("Enter department: ")
newSalary = input("Enter salary: ")
cursor.execute("""INSERT INTO employees(id,name,dept,salary)
        VALUES(?,?,?,?)""",(newID,newName,newDept,newSalary))
db.commit()

# Display all the data from the employees table.
cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

# This must be the last line in the program to close the database.
db.close()
###############
# Display all the data from the employees table and display each record on
# a separate line.

cursor.execute("SELECT * FROM employees")
for x in cursor.fetchall():
    print(x)
    # sqlite3.ProgrammingError: Cannot operate on a closed database.
###
# Selects all the data from the employees table, sorted by name, and 
# displays each record on a separate line.
cursor.execute("SELECT * FROM employees ORDER BY name")
for x in cursor.fetchall():
    print(x)
###
# Select all the data from the employees table where the salary is over 20,000
cursor.execute("SELECT * FROM employees WHERE salary>20000")
###
# Selects all the data from the employees table where the department is "Sales".
cursor.execute("SELECT * FROM employees WHERE dept='Sales'")
###
# Select th ID and name fields from the employees table and the manager field
# from the department table if the salary is over 20,000
cursor.execute("""SELECT * FROM employees.id,employees.name,dept.manager
        FROM employees,dept WHERE employees.dept=dept.dept
        AND employees.salary >20000""")
###
# Selects the ID, name and salary fields from the employees table.
cursor.execute("SELECT id,name,salary FROM employees")
###
# Allows the user to type in a department and displays the records of all
# the employees in that department.
whichDept = input("Enter a department: ")
cursor.execute("SELECT * FROM employees WHERE dept=?", [whichDept])
for x in cursor.fetchall():
    print(x)
###
# Selects the ID and name fields from the employees table and the manager
# field from the department table, using the dept fields to link the data.
# If you do not specify how the tables are linked, Python will assume every
# employee works in every department and you will not get the results you
# are expecting.
cursor.execute("""SELECT employees.id,employees.name,dept.manager
        FROM employees,dept WHERE employees.dept=dept.dept""")
###

