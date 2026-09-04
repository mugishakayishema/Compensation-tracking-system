import sqlite3

conn = sqlite3.connect("payroll.db")

cursor = conn.cursor()

try:

    emp_id = int(
        input("Enter employee ID to delete: ")
    )

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (emp_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Employee deleted successfully!")

    else:
        print("Employee not found!")

except ValueError:

    print("Invalid ID! Please enter integers only.")

finally:

    conn.close()