import sqlite3
import os

# Create db folder if not exists
os.makedirs("db", exist_ok=True)

# Connect to (or create) the SQLite database
conn = sqlite3.connect("db/student_db.sqlite3")
cursor = conn.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hallticket TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    dob TEXT,
    address TEXT,
    branch TEXT,
    year TEXT,
    doj TEXT,
    tenth_htno TEXT,
    tenth_result TEXT,
    twelfth_htno TEXT,
    twelfth_result TEXT,
    profile_pic TEXT,
    password TEXT,

    sem_1_1 TEXT,
    sem_1_2 TEXT,
    sem_2_1 TEXT,
    sem_2_2 TEXT,
    sem_3_1 TEXT,
    sem_3_2 TEXT,
    sem_4_1 TEXT,
    sem_4_2 TEXT,

    s11_1 TEXT, s11_2 TEXT, s11_3 TEXT, s11_4 TEXT, s11_5 TEXT, s11_6 TEXT, s11_7 TEXT, s11_8 TEXT, s11_9 TEXT,
    credits_s11 REAL, sgpa_s11 REAL,

    s12_1 TEXT, s12_2 TEXT, s12_3 TEXT, s12_4 TEXT, s12_5 TEXT, s12_6 TEXT, s12_7 TEXT, s12_8 TEXT,
    credits_s12 REAL, sgpa_s12 REAL,

    s21_1 TEXT, s21_2 TEXT, s21_3 TEXT, s21_4 TEXT, s21_5 TEXT, s21_6 TEXT, s21_7 TEXT, s21_8 TEXT, s21_9 TEXT,
    credits_s21 REAL, sgpa_s21 REAL,

    s22_1 TEXT, s22_2 TEXT, s22_3 TEXT, s22_4 TEXT, s22_5 TEXT, s22_6 TEXT, s22_7 TEXT, s22_8 TEXT, s22_9 TEXT,
    credits_s22 REAL, sgpa_s22 REAL,

    s31_1 TEXT, s31_2 TEXT, s31_3 TEXT, s31_4 TEXT, s31_5 TEXT, s31_6 TEXT, s31_7 TEXT, s31_8 TEXT,
    s31_9 TEXT, s31_10 TEXT, s31_11 TEXT,
    credits_s31 REAL, sgpa_s31 REAL,

    s32_1 TEXT, s32_2 TEXT, s32_3 TEXT, s32_4 TEXT, s32_5 TEXT, s32_6 TEXT, s32_7 TEXT, s32_8 TEXT, s32_9 TEXT, s32_10 TEXT,
    credits_s32 REAL, sgpa_s32 REAL,

    s41_1 TEXT, s41_2 TEXT, s41_3 TEXT, s41_4 TEXT, s41_5 TEXT, s41_6 TEXT, s41_7 TEXT, s41_8 TEXT,
    credits_s41 REAL, sgpa_s41 REAL,

    s42_1 TEXT,
    credits_s42 REAL, sgpa_s42 REAL
);
""")

conn.commit()
conn.close()
print("✅ Database created at db/student_db.sqlite3")
