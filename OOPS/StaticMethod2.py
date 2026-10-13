#program to demonstrate static method using class

class Student:
    def getstuddet(self):
       self.sno=int(input("Enter number:"))
       self.sname=input("enter name:")
       self.marks=float(input("enter marks:"))

class Employee:
    def getempdet(self):
        self.eno=int(input("Employee no:"))
        self.ename=input("employee name:")
        self.esal=float(input("employee salary:"))

class Teacher:
    def getteachdet(self):
        self.tno=int(input("enter no:"))
        self.tname=input("teacher name:")
        self.tsub=input("teacher subject:")

class Hyd:
        @classmethod
        def getobjdata(cls,objdata,objinfo):
            #callling static method from class level method w.r.t cls
            cls.dispobjectdata(objdata,objinfo)


        @staticmethod
        def dispobjdata(objdata,objinfo):
            print("{} information".format(objinfo))
            print(objdata.__dict__)
            for key,value in objdata.__dict__.items():
                print("\t{}---->{}".format(key,value))




#main program
s=Student()
e=Employee()
t=Teacher()

print("content of s",s.__dict__)
print("content of e",e.__dict__)
print("content of t",t.__dict__)
s.getstuddet()
e.getempdet()
t.getteachdet()

print("content of s",s.__dict__)
print("content of e",e.__dict__)
print("content of t",t.__dict__)

Hyd.getobjdata(s,Student)
Hyd.getobjdata(e,Employee)
Hyd.getobjdata(t,Teacher)

