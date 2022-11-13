"""sqlite3 and statistics."""

import sqlite3
import collections

db_filename = 'todo.db'


class Mode:

    def __init__(self):
        self.counter = collections.Counter()

    def step(self, value):
        print('step({!r})'.format(value))
        self.counter[value] += 1

    def finalize(self):
        result, count = self.counter.most_common(1)[0]
        print('finalize() -> {!r} ({} times)'.format(
            result, count))
        return result

with sqlite3.connect(db_filename) as conn:
    conn.create_aggregate('mode', 1, Mode)

    cursor = conn.cursor()
    cursor.execute("""
    select mode(deadline) from task where project = 'pymotw'
    """)
    row = cursor.fetchone()
    print('mode(deadline) is:', row[0])

'''RESULTS:
step('2016-04-25')
step('2016-08-28')
step('2017-07-31')
finalize() -> '2016-04-25' (1 times)
mode(deadline) is: 2016-04-25
'''
