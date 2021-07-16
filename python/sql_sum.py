# make db and shedules
>curs = conn.cursor()
tblcmd = 'create table people (name char(30), job char(10), pay int(4))'
curs.execute(tblcmd)

# add note
>import sqlite3
conn = sqlite3.connect('dbase1')
curs = conn.cursor()
curs.execute('insert into people values (?, ?, ?)', ('Bob', 'dev', 5000))
curs.rowcount
sqlite3.paramstyle

# add more notes
>curs.executemany('insert into people values (?, ?, ?)',
        [('Sue', 'mus', '70000'),
          ('Ann', 'mus', '60000')])
curs.rowcount

# add in cicle
rows = [['Tom', 'mgr', 100000],
        ['Kim', 'adm', 30000],
        ['pat', 'dev', 90000]]

for row in rows:
    curs.execute('insert ito people values (?, ?, ?)', row)
conn.commit()

# make a call
# in cicle
curs.execute('select * from people')
for row in curs.fetchall():
    print(row) # or print(name, ':', pay)

# update
> import sqlite3
conn = sqlite3.connect('dbase1')
curs = conn.cursor()
curs.execute('select * from people')
curs.frtchall()


curse.execute('select * from people')
curs.fetchall()

curs.execute('select * from people')
curs.fetchall()

curs.execute('delete from people where name = ?', ['Bob'])
curs.execute('delete from people where pay >= ?', (90000,))
curs.execute('select * from people')
curs.fetchall()

conn.commit()

# construction dict notes
curs.execute('select * from people')
colnames = [desc[0] for desc in curs.description]
rowdicts = []
for row in curs.fetchall():
    newdict = {}
    for name, val in zip(colnames, row):
        newdicts[name] = val
    rowdicts.append(newdict)

for row in rowdicts: print(row)

# better
curs.execute('select * from people')
colnames = [desc[0] for desc in curs.description]
rowdicts = []
for row in curs.fetchall():
    rowdicts.append(dict(zip(colnames, row)))

rowdicts[0]

# and generator of lists
curs.execute('select * from people')
colnames = [desc[0] for desc in curs.decription]
rowdicts = [dict(zip(colnames, row)) for row in curs.fetchall()]
rowdicts[0]

