import time,sys

class Employee:
    def __init__(self,eno,ename):
        print("*"*49)
        self.eno=eno
        self.ename=ename
        print("employee name:{}".format(self.eno))
        print("employee number:{}".format(self.ename))

    def __del__(self): #destructor definition
        global memspace
        memspace=memspace-sys.getsizeof(self)
        print("\t available memory space=",memspace)



#main program
eo1=Employee(45,"sai")
del eo1 #used to dlt an object
eo2=Employee(45,"gani")
eo3=Employee(56,"ram")

memspace=sys.getsizeof(eo1)+sys.getsizeof(eo2)+sys.getsizeof(eo3)
print("calculate memory=",memspace)
time.sleep(10)