from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, emp_id):

        self.__name = name
        self.__emp_id = emp_id

    # GET NAME
    def get_name(self):
        return self.__name

    # GET ID
    def get_emp_id(self):
        return self.__emp_id

    # SET NAME
    def set_name(self, name):
        self.__name = name

    @abstractmethod
    def calculate_weekly_pay(self):
        pass