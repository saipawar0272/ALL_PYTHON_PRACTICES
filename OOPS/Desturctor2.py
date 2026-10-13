#program for demonstrating with destructor
import time
import sys
class Employee:
    def __init__(self,eno,ename):
        print("*"*50)
        self.eno=eno
        self.ename=ename
        print("Employee number:{}".format(self.eno))
        print("employee number:{}".format(self.ename))
        print("___________________"*48)
    def __del__(self): #destructor definition
            global memspace
            print("GC calls__del__() for removing the memory space of current object")
            memspace=memspace-sys.getsizeof(self)
            print("\tavailable memory space is=",memspace)


#main program
eo1=Employee(100,"gani") #object creation
print("no longe needed")
eo1=None #gc calls destructor forcefully to remove an object
eo2=Employee(232,"sai")
eo3=Employee(45,"ramesh")
#calculate the memory space of eo1,eo2,eo3
memspace=sys.getsizeof(eo1)+sys.getsizeof(eo2)+sys.getsizeof(eo3)
print("memory space of eo1=",memspace)
time.sleep(10)
#here gc call destructor at the end of program exceution and this type of GC is called automatic garbage collector
