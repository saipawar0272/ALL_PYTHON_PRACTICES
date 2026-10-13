#import sys,time
from email.encoders import encode_noop
from logging import getLevelName

import sys,time
class Employee:
    def __init__(self,eno,ename): #constructor
       self.eno=eno
       self.ename=ename
       print("employee name={}".format(self.eno))
       print("employee name={}".format(self.ename))

    def __del__(self): #destructor definition
         global memspace
         memspace=memspace-sys.getsizeof(self)
         print(" available memspace of= ",memspace)

#main program
eo1=Employee(45,"sai")  #object creation==pvm call parametrized constructor
eo2=eo1  #deep copy
eo3=eo2
print(eo1.__dict__)
print(eo2.__dict__)
print(eo3.__dict__)

memspace=sys.getsizeof(eo1)+sys.getsizeof(eo2)+sys.getsizeof(eo3)
print("calculate memsapce=",memspace)
time.sleep(10)