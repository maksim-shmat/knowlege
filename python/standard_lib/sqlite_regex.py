"""REGEXP for sqlite3 from Python."""

import re
import sqlite3

db_filename = 'todo.db'


def regexp(pattern, input):
    return bool(re.match(pattern, input))

with sqlite3.connect(db_filename) as conn:
    conn.row_factory = sqlite3.Row
    conn.create_function('regexp', 2, regexp)
    cursor = conn.cursor()
    pattern = '.*[wW]rite [aA]bout.*'

    cursor.execute(
            """
            select id, priority, details, status, deadline from task
            where details regexp :pattern
            order by deadline, priority
            """,
            {'pattern': pattern},
    )

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))

'''RESULTS:
 1 [1] write about select        [done    ] (2016-04-25)
 2 [1] write about random        [waiting ] (2016-08-28)
 3 [1] write about sqlite3       [active  ] (2017-07-31)
'''
