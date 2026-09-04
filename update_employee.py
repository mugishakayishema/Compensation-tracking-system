import sqlite3

conn = sqlite3.connect("payroll.db")

cursor = conn.cursor()

try:

    emp_id = int(
        input("Enter employee ID to update: ")
    )

    new_pay = float(
        input("Enter new weekly pay: ")
    )

    cursor.execute(
        """
        UPDATE employees
        SET weekly_pay = ?
        WHERE id = ?
        """,
        (new_pay, emp_id)
    )

    conn.commit()

    # CHECK IF EMPLOYEE EXISTS
    if cursor.rowcount > 0:

        print("Employee updated successfully!")

    else:

        print("Employee not found!")

except ValueError:

    print("Invalid input!")

finally:

    conn.close()
    