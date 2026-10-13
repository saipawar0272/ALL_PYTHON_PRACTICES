
class employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def display(self):
        print(self.name)
        print(self.__salary)


emp = employee('sai',597646)
print(emp.name)
#print(emp.__salary) #can't access private method outside of the class

emp.display()

