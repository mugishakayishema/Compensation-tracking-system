import sqlite3

conn = sqlite3.connect("payroll.db")

cursor = conn.cursor()

name = input("Enter employee name: ")

cursor.execute(
    "SELECT * FROM employees WHERE name = ?",
    (name,)
)

rows = cursor.fetchall()

print("\n--- Search Results ---")


for row in rows:
    print(row)

else:

    print("Employee not found!")

conn.close() 