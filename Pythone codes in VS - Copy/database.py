import sqlite3

# CONNECT DATABASE
conn = sqlite3.connect("payroll.db")

# CREATE CURSOR
cursor = conn.cursor()

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    emp_type TEXT,
    weekly_pay REAL
)
""")

conn.commit()

print("Database and table created successfully!")

conn.close()