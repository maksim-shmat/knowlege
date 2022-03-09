"""Work with postgresql."""

import psycopg2

conn = psycopg2.connect('user=foo password=bar dbname=baz')
curs = conn.cursor()
reply_to = input('Reply to: ')
subject = input('Subject: ')
sender = input('Sender: ')
text = input('Text: ')
if reply_to:
    query = """
    INSERT INTO messages(reply_to, sender, subject, text)
    VALUES({}, '{}', '{}', '{}')""".format(sender, subject, text)
curs.execute(query)
conn.commit()
