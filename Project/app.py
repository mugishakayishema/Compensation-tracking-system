from flask import (
    Flask,
    jsonify,
    render_template
)

import sqlite3

app = Flask(__name__)

# FRONTEND PAGE
@app.route("/")
def home():

    return render_template(
        "index.html"
    )

# API
@app.route("/employees")
def get_employees():

    conn = sqlite3.connect(
        "payroll.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM employees"
    )

    rows = cursor.fetchall()

    employees = []

    for row in rows:

        employee = {
            "id": row[0],
            "name": row[1],
            "type": row[2],
            "weekly_pay": row[3]
        }

        employees.append(employee)

    conn.close()

    return jsonify(employees)

if __name__ == "__main__":

    app.run(debug=True)