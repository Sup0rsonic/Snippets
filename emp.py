import sys
import os

EMPLOYEE_ID = 1000


class Employee:


    def __init__(self , emp_name, emp_salary, emp_id=EMPLOYEE_ID + 1):
        global EMPLOYEE_ID
        self.id = emp_id
        self.name = emp_name
        self._salary = emp_salary
        EMPLOYEE_ID += 1
        return

    def __add__(self, other):
        return [self.name, self._salary + other.salary]

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, val):
        self._salary = 1000 if val < 1000 else 50000 if val > 50000 else val

if __name__ == '__main__':
    emp = Employee('meow', 12345)
    emp1 = Employee('test' ,23333)
    print(emp.salary)
    print(emp.name)
    emp.salary = 100000
    print(emp.salary)
    emp.salary = 23333
    print(emp.salary)
    print(emp + emp1)
