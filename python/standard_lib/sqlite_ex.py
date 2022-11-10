"""sqlite about."""

'''
#1 cratedb

import os
import sqlite3

db_filename = 'todo.db'

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

if db_is_new:
    print('Need to create schema')
else:
    print('Databae exists; assume schema does, too.')

conn.close()
'''
#2 create schema

import os
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Inserting initial data')

        conn.executescript("""
        insert into project (name, description, deadline)
        values ('pymotw', 'Python Module of the Week',
                '2016-11-02');

        insert into task (details, status, deadline, project)
        values ('write about select', 'done', '2016-04-25',
                'pymotw');

        insert into task (details, status, deadline, project)
        values('write about random', 'waiting', '2016-08-28',
              'pymotw');

        insert into task (details, status, deadline, project)
        values ('write about sqlite3', 'active', '2017-07-31',
                'pymotw');
        """)
    else:
        print('Database exists, assume schema does, too.')

'''RESULTS: from scheme for db in todo_schema.sql
$ rm -f todo.db
$ python3 sqlite_ex.py
Creating schema
Inserting initial data
$ sqlite3 todo.db 'select * from task'
1|1|write about select|done|2016-04-25||pymotw
2|1|write about random|waiting|2016-08-28||pymotw
3|1|write about sqlite3|active|2017-07-31||pymotw
'''

#3 make a cursor for read value from db

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select id, priority, details, status, deadline from task
    where project = 'pymotw'
    """)
    
    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))

'''RESULTS:
 1 [1] write about select        [done    ] (2016-04-25)
 2 [1] write about random        [waiting ] (2016-08-28)
 3 [1] write about sqlite3       [active  ] (2017-07-31)
'''

#4 fetchone() and fetchmany() for get data 

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select name, description, deadline from project
    where name = 'pymotw'
    """)
    name, description, deadline = cursor.fetchone()

    print('Project details for {} ({})\n due {}'.format(
        description, name, deadline))

    cursor.execute("""
    select id, priority, details, status, deadline from task
    where project = 'pymotw' order by deadline
    """)

    print('\nNext 5 tasks:')
    for row in cursor.fetchmany(5):
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))

'''RESULTS:
Project details for Python Module of the Week (pymotw)
 due 2016-11-02

Next 5 tasks:
 1 [1] write about select        [done    ] (2016-04-25)
 2 [1] write about random        [waiting ] (2016-08-28)
 3 [1] write about sqlite3       [active  ] (2017-07-31)
'''

#4 cursor description

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select * from task where project = 'pymotw'
    """)

    print('Task table has these columns:')
    for colinfo in cursor.description:
        print(colinfo)

'''RESULTS:
Task table has these columns:
('id', None, None, None, None, None, None)
('priority', None, None, None, None, None, None)
('details', None, None, None, None, None, None)
('status', None, None, None, None, None, None)
('deadline', None, None, None, None, None, None)
('completed_on', None, None, None, None, None, None)
('project', None, None, None, None, None, None)
'''

#5 positional arguments - <?>, for safe

'''
import sqlite3
import sys

db_filename = 'todo.db'
project_name = sys.argv[1]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """
    select id, priority, details, status, deadline from task
    where project = ?
    """
    cursor.execute(query, (project_name,))

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))

EXPECTED RESULTS: After write in CLI: python3 sqlite_ex.py pymotw
1 [1] write about select    [done    ] (2011-04-27)
2 [1] write about random    [waiting ] (2016-08-22)
3 [1] write about sqlite3
'''

#6 named arguments - <:>, for safe

'''
import sqlite3
import sys

db_filename = 'todo.db'
project_name = sys.argv[1]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """
    selct id, priority, details, status, deadline from task
    where project = :project_name
    order by deadline, priority
    """

    cursor.execute(query, {'project_name': project_name})

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))

EXPECTED RESULTS: Afer write in CLI: $ python3 sqlite_ex.py pymotw
1 [1] write about select    [done    ] (2011-04-27)
2 [1] write about random    [waiting ] (2016-08-22)
3 [1] write about sqlite3
'''

#7  update argument

'''
import sqlite3
import sys

db_filename = 'todo.db'
id = int(sys.argv[1])
status = sys.argv[2]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    query = "update task set status = :status where id = :id"
    cursor.execute(query, {'status': status, 'id': id})

EXPEDTED RESULTS: write: $ python3 sqlite_ex.py 2 done
                         $ python3 sqlite_ex.py pymotw

1 [1] write about select    [done    ] (2011-04-27)
2 [1] write about random    [waiting ] (2016-08-22)
3 [1] write about sqlite3
'''

#8 executemany(), load from csv

'''
import csv
import sqlite3
import sys

db_filename = 'todo.db'

data_filename = sys.argv[1]

SQL = """
insert into task (details, priority, status, deadline, project)
values (:details, :priority, 'active', :deadline, :project)
"""

with open(data_filename, 'rt') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.executemany(SQL, csv_reader)
        
EXPECTED RESULTS: After write in CLI: $ python3 sqlite_ex.py tasks.csv
                                         $ python3 sqlite_ex.py pymotw
                              # need use code from #6 in different file
1 [1] write about select          [done    ] (2029-04-11)
5 [2] revise chapter intros       [active  ] (1010-09-99)
2 [1] write about random          [done    ] (9999-99-99)
6 [1] subtitle                    [active  ] (9999-99-99)
4 [2] finish reviewing markup     [acitve  ] (9999-99-99)
3 [1] write about swlite3         [active  ] (9999-99-99)
'''

#9 data types for SQLite from sqlite3

import sqlite3
import sys

db_filename = 'todo.db'

sql = "select id, details, deadline from task"

def show_deadline(conn):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    for col in ['id', 'details', 'deadline']:
        print('  {:<8}  {!r:<26} {}'.format(
            col, row[col], type(row[col])))
    return

print('Without type detection:')
with sqlite3.connect(db_filename) as conn:
    show_deadline(conn)

print('\nWith type detection:')
with sqlite3.connect(db_filename,
                     detect_types=sqlite3.PARSE_DECLTYPES,
                     ) as conn:
    show_deadline(conn)

'''RESULTS:
Without type detection:
  id        1                          <class 'int'>
  details   'write about select'       <class 'str'>
  deadline  '2016-04-25'               <class 'str'>

With type detection:
  id        1                          <class 'int'>
  details   'write about select'       <class 'str'>
  deadline  datetime.date(2016, 4, 25) <class 'datetime.date'>
'''

#10 custom types
'''
import pickle
import sqlite3

db_filename = 'todo.db'

def adapter_func(obj):
    """Change data from memory to view for db."""
    print('adapter_func({})\n'.format(obj))
    return pickle.dumps(obj)

def converter_func(data):
    """Change data from db to view for memory."""
    print('convert_func({!r})\n'.format(data))
    return pickle.loads(data)


class MyObj:

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return 'MyObj({!r})'.format(self.arg)

# Registration functions for change types
sqlite3.register_adapter(MyObj, adapter_func)
sqlite3.register_converter("MyObj", converter_func)

# Make objects for save. Use lists of tuples for muve it to executemany().
to_save = [
        (MyObj('this is a value to save'),),
        (MyObj(42),),
]

with sqlite3.connect(
        db_filename,
        detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    conn.execute("""
create table if not exists obj (
id    integer primary key autoincrement not null,
data  MyObj
)
""")
    cursor = conn.cursor()

    # Insert objects into db
    cursor.executemany("insert into obj (data) values (?)",
                       to_save)
    # Show objects saved in db in this time
    cursor.execute("select id, data from obj")
    for obj_id, obj in cursor.fetchall():
        print('Retrieved', obj_id, obj)
        print('  with type', type(obj))
        print()

RESULTS:
Traceback (most recent call last):
  File "<stdin>", line 362, in <module>
sqlite3.OperationalError: database is locked

shell returned 1
'''

#11 custom column type

'''
import pickle
import sqlite3

db_filename = 'todo.db'

def adapter_func(obj):
    """Change data from memory to view for db."""
    print('adapter_func({})\n'.format(obj))
    return pickle.dumps(obj)

def converter_func(data):
    """Change data from db to view for memory."""
    print('converter_func({!r})\n'.format(data))
    return pickle.loads(data)


class MyObj:

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return 'MyObj({!r})'.format(self.arg)

# Registeration
sqlite3.register_adapter(MyObj, adapter_func)
sqlite3.register_converter("MyObj", converter_func)

# Make objects for save. list of tuples for executemany()
to_save = [
        (MyObj('this is a value to save'),),
        (MyObj(42),),
]

with sqlite3.connect(
        db_filename,
        detect_types=sqlite3.PARSE_COLNAMES) as conn:
    conn.execute("""
    create table if not exists obj2 (
    id   integer primary key autoincrement not null,
    data text
    )
    """)

    cursor = conn.cursor()

    # Insert objects in db
    cursor.executemany("insert into obj2 (dat) values (?)", to_save)

    # Get obj
    cursor.execute(
            'select id, data as "pickle [MyObj]" from obj2',
    )
    for obj_id, obj in cursor.fetchall():
        print('Retrived', obj_id, obj)
        print('  with type', type(obj))
        print()

   RESULTS:
Traceback (most recent call last):
  File "<stdin>", line 426, in <module>
sqlite3.OperationalError: database is locked

shell returned 1
'''

#12 transaction commit


