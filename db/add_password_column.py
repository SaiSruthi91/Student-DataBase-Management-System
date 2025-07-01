import sqlite3
conn = sqlite3.connect('db/student_db.sqlite3')
cur = conn.cursor()
cur.execute("ALTER TABLE students ADD COLUMN password TEXT")
conn.commit()
conn.close()
print("✅ 'password' column added successfully.")