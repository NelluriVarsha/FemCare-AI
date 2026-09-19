import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS health_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    sleep_hours REAL,
    water_intake REAL,
    exercise_minutes INTEGER,
    stress_level INTEGER,
    symptoms TEXT,
    health_score INTEGER,
    pcos_risk TEXT
)
""")

conn.commit()
conn.close()
cursor.execute("""
CREATE TABLE IF NOT EXISTS menstrual_logs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    last_period_date TEXT,
    cycle_length INTEGER,
    period_duration INTEGER,
    cycle_type TEXT
)
""")