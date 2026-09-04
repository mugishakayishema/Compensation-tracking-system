from abc import ABC, abstractmethod

#Abstract class
class Employee(ABC):
    def __init__ (self, name, emp_id):
        self.__emp_id = emp_id 
        self.__name = name
    

    #Getters

        def get_name (self):
            return self.__name
        
        def get_emp_id(self):
            return self.__emp__id
        
        #setters

        def set_name (self, name):
            self._name = name

@abstractmethod
def calcaculate_weekly_pay(self):
    pass







    

    

