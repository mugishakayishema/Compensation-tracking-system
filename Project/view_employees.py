import sqlite3

# CONNECT DATABASE
conn = sqlite3.connect("payroll.db")

# CREATE CURSOR
cursor = conn.cursor()

# GET ALL EMPLOYEES
cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

print("\n--- Employees in Database ---")

for row in rows:
    print(row)

# CLOSE DATABASE
conn.close()