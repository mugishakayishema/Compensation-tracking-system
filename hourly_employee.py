from employee import Employee

class HourlyEmployee(Employee):

    def __init__(
        self,
        name,
        emp_id,
        hourly_rate,
        hours_worked
    ):

        super().__init__(name, emp_id)

        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def calculate_weekly_pay(self):

        if self.__hours_worked <= 40:

            return (
                self.__hourly_rate *
                self.__hours_worked
            )

        overtime = self.__hours_worked - 40

        return (
            (40 * self.__hourly_rate)
            +
            (overtime * self.__hourly_rate * 1.5)
        )