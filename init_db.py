import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('This one?', 'First animal')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Or this one?', 'Second animal')
            )

connection.commit()
connection.close()

