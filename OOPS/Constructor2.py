from pickletools import stringnl_noescape
from sys import stdlib_module_names


class Student:
  def __init__(self,sno,sname):
    print("i am from constructor")
    self.sno=sno
    self.sname=sname
    print("Srudent Number:{}".format(self.sno))
    print("student name:{}".format(self.sname))


#main program

s1=Student(100,"maha lakshmi") #object creation --PVM Calls Constructor
s2=Student(200,"swathi") #
print(s1.__dict__)
print(s2.__dict__)