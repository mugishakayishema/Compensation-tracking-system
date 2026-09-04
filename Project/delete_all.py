import sqlite3

conn = sqlite3.connect("payroll.db")

cursor = conn.cursor()

print("WARNING: This will delete ALL employees!")

confirm = input(
    "Type DELETE ALL to continue: "
)

if confirm == "DELETE ALL":

    cursor.execute(
        "DELETE FROM employees"
    )

    conn.commit()

    print("All employees deleted successfully!")

else:

    print("Operation cancelled.")

conn.close()