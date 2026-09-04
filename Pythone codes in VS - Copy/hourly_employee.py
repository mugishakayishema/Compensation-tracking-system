from  employee import Employee

class HourlyEmployee(Employee):
    

    def __init__(self, name, emp_id, hourly_rate, hours_worked):
      super().__init__(name, emp_id)
      self.__hourly_rate = hourly_rate
      self.__hours_worked = hours_worked
      self.sethourly_rate(hourly_rate)

      self.sethours_worked(hours_worked)

      def set_hourly_rate(self,rate):
         if rate > 0:

          self.hourly_rate = rate
         else:
          self.__hourly_rate = 0 

         def set__hours_worked(self,hours):
            if hours>= 168:
             self.hours_worked = hours
            else:
             self.__hours_worked = 0
         def get_hourly_rate (self):
            return self.__hourly_rate
         
         def get_hours_worked(self):
            return self.__hours_worked
         
         def calculate_weekly_pay(self):
            if self. hours_worked <=40:
               return self. hourly_rate*self.hours_worked
            overtime = self.__hours_worked-40
            return (
               (40* self.__hourly_rate)+(overtime* self.__hourly_rate* 1.5)
            )

         


            


