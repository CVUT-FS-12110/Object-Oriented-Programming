import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS temperature(id integer primary key autoincrement, value)''')

cursor.execute(f"INSERT INTO temperature VALUES (NULL, 25)")

res = cursor.execute("SELECT * FROM temperature")
print(res.fetchall())

conn.commit()

conn.close()
