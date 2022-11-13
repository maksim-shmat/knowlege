"""Authorization in sqlite."""

import sqlite3

db_filename = 'todo.db'

def authorizer_func(action, table, column, sql_locationn, ignore):
    print('\nauthorizer_func({}, {}, {}, {}, {})'.format(
        action, table, column, sql_location, ignore))

    response = sqlite3.SQLITE_OK  # OK by default

    if action == sqlite3.SQLITE_SELECT:
        print('requesting permission to run a select statement')
        response = sqlite3.SQLITE_OK

    elif action == sqlite3.SQLITE_READ:
        print('requesting  access to column {}.{} from {}'.format(
            table, column, sql_location))
        if column == 'details':
            print('  ignoring details column')
            response = sqlite3.SQLITE_IGNORE
        elif column == 'priority':
            print('  preventing access to priority column')
            response = sqlite3.SQLITE_DENY

    return response


with sqlite3.connect(db_filename) as conn:
    conn.row_factory = sqlite3.Row
    conn.set_authorizer(authorizer_func)

    print('Using SQLITE_IGNORE to mask a column value:')
    cursor = conn.cursor()
    cursor.execute("""
    select id, details from task where project = 'pymotw'
    """)
    for row in cursor.fetchall():
        print(row['id'], row['details'])

    print('\nUsing SQLITE_DENY to dent access to a column:')
    cursor.execute("""
    select id, priority from task where project = 'pymotw'
    """)
    for row in cursor.fetchall():
        print(row['id'], row['details'])

'''RESULTS:
Using SQLITE_IGNORE to mask a column value:
Traceback (most recent call last):
  File "<stdin>", line 36, in <module>
sqlite3.DatabaseError: not authorized

shell returned 1
'''
