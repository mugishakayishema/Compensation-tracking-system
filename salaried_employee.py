from employee import Employee

class SalariedEmployee(Employee):

    def __init__(self, name, emp_id, monthly_salary):
        # CALL PARENT CONSTRUCTOR
        super().__init__(name, emp_id)

        self.__monthly_salary = monthly_salary

    def calculate_weekly_pay(self):
        return self.__monthly_salary / 4