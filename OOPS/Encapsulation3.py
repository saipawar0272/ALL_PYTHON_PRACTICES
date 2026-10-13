
class Employee:
    def __init__(self):
        self.__salary = 50000
    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if type(salary) == int:
           self.__salary = self.__salary + salary
        else:
            print("salary must be integer")



emp = Employee()
print(emp.get_salary())

v_salary =  int(input("enter salary : "))

emp.set_salary(v_salary)
print(emp.get_salary())


