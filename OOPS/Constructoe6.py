#program for demonstrating without using constructor

class Employee:
    def __init__(self,eno,ename):
        print("*"*40)
        self.eno=eno
        self.ename=ename
        print("Employee number:{}".format(self.eno))
        print("employee name:{}".format(self.ename))

#main program
eo1=Employee(100,"sai") #object creation--PVM calls Parameterized constructor
eo2=Employee(200,"ganesh")


