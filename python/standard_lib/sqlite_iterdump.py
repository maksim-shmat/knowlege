"""Work with memory for sqlite."""

import sqlite3

schema_filename = 'todo_schema.sql'

with sqlite3.connect(':memory:') as conn:
    conn.row_factory = sqlite3.Row
    
    print('Creating schema')
    with open(schema_filename, 'rt') as f:
        schema = f.read()
    conn.executescript(schema)

    print('Inserting initial data')
    conn.execute("""
    insert into project (name, description, deadline)
    values ('pymotw', 'Python Module of the Week',
            '2020-11-11')
    """)
    data = [
            ('write about select', 'done', '2010-10-03',
                'pymotw'),
            ('write about random', 'waiting', '2010-10-10',
                'pymotw'),
            ('write about sqlite3', 'active', '2010-10-10',
                'pymotw'),
    ]
    conn.executemany("""
    insert into task (details, status, deadline, project)
    values(?, ?, ?, ?)
    """, data)

    print('Dumping:')
    for text in conn.iterdump():
        print(text)

'''RESULTS:
    Creating schema
Inserting initial data
Dumping:
BEGIN TRANSACTION;
CREATE TABLE project (
	name        text primary key,
	description text,
	deadline    date
);
INSERT INTO "project" VALUES('pymotw','Python Module of the Week','2020-11-11');
CREATE TABLE task (
	id           integer primary key autoincrement not null,
	priority     integer default 1,
	details text,
	status text,
	deadline date,
	completed_on date,
	project text not null references project(name)
);
INSERT INTO "task" VALUES(1,1,'write about select','done','2010-10-03',NULL,'pymotw');
INSERT INTO "task" VALUES(2,1,'write about random','waiting','2010-10-10',NULL,'pymotw');
INSERT INTO "task" VALUES(3,1,'write about sqlite3','active','2010-10-10',NULL,'pymotw');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('task',3);
COMMIT;
'''
