import sqlite3
conn = sqlite3.connect("payroll.db")
cursor = conn.cursor()

from salaried_employee import SalariedEmployee

from hourly_employee import HourlyEmployee


employees = []

n = int(input("Enter number of employees: "))

for i in range(n):

    print(f"\nEmployee {i + 1}")

    name = input("Enter name: ")
    emp_id = int(input("Enter ID: "))

    emp_type = int(
        input("Select type (1 = Salaried, 2 = Hourly): ")
    )

    if emp_type == 1:

        salary = float(input("Enter monthly salary: "))

        emp = SalariedEmployee(name, emp_id, salary)

        employees.append(emp)

         # SAVE TO DATABASE
        cursor.execute(
            "INSERT INTO employees VALUES (?, ?, ?, ?)",
            (
                emp_id,
                name,
                "Salaried",
                emp.calculate_weekly_pay()
            )
        )

    elif emp_type == 2:

        rate = float(input("Enter hourly rate: "))
        hours = float(input("Enter hours worked: "))

        emp = HourlyEmployee(name, emp_id, rate, hours)

        employees.append(emp)
 # SAVE TO DATABASE
        cursor.execute(
            "INSERT INTO employees VALUES (?, ?, ?, ?)",
            (
                emp_id,
                name,
                "Hourly",
                emp.calculate_weekly_pay()
            )
        )
    else:
        print("Invalid employee type!")

# POLYMORPHISM
total_payroll = 0

print("\n--- Payroll Report ---")

for emp in employees:

    pay = emp.calculate_weekly_pay()

    print(
        f"{emp.get_name()} "
        f"(ID: {emp.get_emp_id()}) "
        f"Weekly Pay: {pay}"
    )

    total_payroll += pay

print(f"\nTotal Payroll: {total_payroll}")

conn.commit()
conn.close()