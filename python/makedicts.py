# make list of tuples notes in lixt of dicts

def makedicts(cursor, query, params=()):
    cursor.execute(query, params)
    colnames = [desc[0] for desc in cursor.description]
    rowdicts = [dict(zip(colnames, row)) for row in cursor.fetchall()]
    return rowdicts

if __name__ == '__main__':
    import sqlite3
    conn = sqlite3.connect('dbase1')
    cursor = conn.cursor()
    query = 'select name, pay from people where pay < ?'
    lowpay = makedicts(cursor, query, [70000])
    for rec in lowpay: print(rec)

"""
>from makedicts import makedicts
from sqlite3 import connect
conn = connect('dbase1')
curs = conn.cursor()
curs.execute('select * from people')
curs.fetchall()

rows = makedicts(curs, "select name from people where job = 'mus'")
rows

query = 'select name, pay from people where job = ? order by name'
musicinans = makedicts(curs, query, ['mus'])
for row in musicians: print(row)
"""
