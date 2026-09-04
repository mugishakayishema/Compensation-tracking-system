from employee import Employee

class SalariedEmployee(Employee):
   

    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.__monthly_salary = monthly_salary
        self.set_monthly_salary(monthly_salary)

    def set_monthly_salary(self, salary):
        if salary > 0:
            self.__monthly_salary = salary
        else:
            self.__monthly_salary = 0

    def get_monthly_salary(self):
        return self.__monthly_salary

    def calculate_weekly_pay(self):
        return self.__monthly_salary / 4
   



        




