"""Sqlite3 and threading."""

import sqlite3
import sys
import threading
import time


db_filename = 'todo.db'
isolation_level = None

def reader(conn):
    print('Starting thread')

    try:
        cursor = conn.cursor()
        cursor.execute('select * from task')
        cursor.fetchall()
        print('results fetched')
    except Exception as err:
        print('ERROR:', err)

if __name__ == '__main__':
    with sqlite3.connect(db_filename,
                         isolation_level=isolation_level,
                         ) as conn:
        t = threading.Thread(name='Reader 1',
                             target=reader,
                             args=(conn,),
                             )
        t.start()
        t.join()

# both threads useless
'''RESULTS:
Starting thread
ERROR: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 140587427512768 and this is thread id 140587421877824.
'''
