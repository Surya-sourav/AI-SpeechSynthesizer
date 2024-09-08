import sqlite3

conn = sqlite3.connect('tts.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT ,text TEXT NOT NULL)''')

cursor.execute("INSERT INTO tasks (text) VALUES(?)",("Hello how are you ?", ))

conn.commit()

cursor.execute("SELECT * FROM tasks")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

