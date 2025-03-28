import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO assignments (name) VALUES (?)",
            ('First Assignment')
            )

cur.execute("INSERT INTO assignments (name) VALUES (?)",
            ('Second Assignment')
            )

connection.commit()
connection.close()