""" sqlite 3 have own site."""

import sqlite3
'''
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
# Updates the data in the table(overwriting the original data) to change the
# name to "Tony" for employee ID1.
cursor.execute("UPDATE employees SET name = 'Tony' WHERE id=1")
###
cursor.execute("DELETE employees WHERE id=1")
###########

# 139
# Create an SQL database called PhoneBook that contains a table called Names
# with the following data:
# ID    First Name    Surname    Phone Number

import sqlite3
with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(
        id integer PRIMARY KEY,
        firstname text,
        surname text,
        phonenumber text); """)

cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
        VALUES("1","Simon","Howels","01223 349752")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
        VALUES("2","Karen","Phillips","01954 295773")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
        VALUES("3","Darren","Smith","01583 749012")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
        VALUES("4","Anne","Jones","01323 567322")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
        VALUES("5","Mark","Smith","01223 855534")""")
db.commit()

db.close()

# 140
# Using the PhoneBook database from program 139, write a program that will
# display the following menu.  Main Menu
# 1) View phone book
# 2) Add to phone book
# 3) Search for surname
# 4) Delete person from phone book
# 5) Quit
# Enter you selection:
# If the user selects 1, they should be able to view the entire phonebook. If
# they select 2, it should allow them to add a new person to the phonebook. If
# they select 3, it should ask them for a surname and then display only the
# records of people with the same surname. If they select 4, it should ask for
# an ID and then delete that select 5, it should end the program. Finally, it 
# should display a suitable message if they enter an incorrect selection from
# the menu. They should return to the menu after each action, until they 
# select 5.

import sqlite3

def viewphonebook():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

def addtophonebook():
    newid = int(input("Enter ID: "))
    newfname = input("Enter first name: ")
    newsname = input("Enter surname: ")
    newpnum = input("Enter phone number: ")
    cursor.execute("""INSERT INTO Names (id,firstname,surname,phonenumber)
VALUES (?,?,?,?)""",(newid,newfname,newsname,newpnum))
    db.commit()

def selectname():
    selectsurname = input("Enter a surname: ")
    cursor.execute("SELECT * FROM Names WHERE surname = ?", [selectsurname])
    for x in cursor.fetchall():
        print(x)

def deletedata():
    selectid = int(input("Ente ID: "))
    cursor.execute("DELETE FROM Names WHERE id = ?", [selectid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

def main():
    again = "y"
    while again == "y":
        print()
        print("Main Menu")
        print()
        print("1) View phone book")
        print("2) Add to phone book")
        print("3) Search for surname")
        print("4) Delete person from phone book")
        print("5) Quit")
        print()
        selection = int(input("Enter your selection: "))
        print()
        
        if selection == 1:
            viewphonebook()
        elif selection == 2:
            addtophonebook()
        elif selection == 3:
            selectname()
        elif selection == 4:
            deletedata()
        elif selection == 5:
            again = "n"
        else:
            print("Incorrect selection entered")

main()
db.close()

# 141
# Create a new SQL database called Bookinfo that will store a list of authors
# and the books they wrote. It will have two tables. The first one should be
# called Authors and contain the following data:
# Name                Place of Birth
# Agatha Christie     Torquay
# The second should be called Books and contain the following data;
# ID    Title    Author    Date Published

import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Authors(
        Name text PRIMARY KEY,
        PlaceofBirth text); """)

cursor.execute(""" INSERT INTO Authors(Name,PlaceofBirth)
        VALUES("Agatha Christie","Torquay")""")
db.commit()

cursor.execute(""" INSERT INTO Authors(Name,PlaceofBirth)
        VALUES("Cecelia Ahern","Dublin")""")
db.commit()

cursor.execute(""" INSERT INTO Authors(Name,PlaceofBirth)
        VALUES("J.K. Rowling","Bristol")""")
db.commit()

cursor.execute(""" INSERT INTO Authors(Name,PlaceofBirth)
        VALUES("Oscar Wilde","Dublin")""")
db.commit()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Books(
        ID integere PRIMARY KEY,
        Title text,
        Author text,
        DatePublished integer); """)

cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished)
        VALUES("1","De Profundis","Oscar Wilde","1905")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished)
        VALUES("2","Harry Potter and the chamber of sectets","J.K. Rowling","1998")""")
db.commit()
cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished)
        VALUES("3","Harry Potter and the prisoner of Azkaban","J.K. Rowling","1999")""")

cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished)
        VALUES("4","Lyrebird","Cecelia Ahern","2017")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished)
        VALUES("5","Murder on the Orient Express","Agatha Christe","1934")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished)
        VALUES("6","Perfect","Cecelia Ahern","2017")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished)
        VALUES("7","The marble collector","Cecelia Ahern","2016")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished)
        VALUES("8","The murder on the links","Agatha Christie","1923")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished)
        VALUES("9","The picture of Dorian Gray","Oscar Wilde","1890")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished)
        VALUES("10","The secret asversary","Agatha Christie","1929")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished)
        VALUES("11","The seven dials mystery","Agatha Christie","1929")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID,Title,Author,DatePublished)
        VALUES("12","The year I met you","Cecelia Ahern","2014")""")
db.commit()

db.close()

# 142
# Using the Bookinfo database from program 141, display the list of authors
# and their place of birth. Ask the user to enter a place of birth and then
# show the title, date published and author's name for all the books by
# authors who were born in the location they selected.

import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)
print()
location = input("Enter a place of birth: ")
print()

cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.Author
        FROM Books,Authors WHERE Authors.Name=Books.Author AND Authors.PlaceofBirth=?""",[location])
for x in cursor.fetchall():
    print(x)

db.close()
'''
# 143
# Using the BookInfo database, ask the user to enter a year and display all
# the books published after that year, sorted by the year they were published.

import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

selectionyear = int(input("Enter a year: "))
print()

cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.Author
        FROM Books WHERE DatePublished>? ORDER BY DatePublished""",[selectionyear])
for x in cursor.fetchall():
    print(x)

db.close()

# 144
