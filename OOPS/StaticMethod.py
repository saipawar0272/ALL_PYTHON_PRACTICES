#program to demonstrate static method

class Student:
    def getstuddet(self):
        self.sno=int(input("enter student no:"))
        self.sname=input("Enter name:")
        self.marks=float(input("Enter marks"))

class Employee:
    def getempdet(self):
        self.eno=int(input("Enter employee number:"))
        self.ename=input("enter name:")
        self.esal=float(input("enter salary:"))

class Teacher:
    def getteachdet(self):
        self.tno=int(input("Enter teacher no:"))
        self.tname=input("teacher name:")
        self.expr=float(input("enter experience:"))
        self.subject=input("Enter subject")

class Hyd:
    @staticmethod
    def dispobjectdata(objdata,objinfo):
        print("{} information".format(objinfo))
        print(type(objdata))
        print(objdata.__dict__)
        print("*"*48)
        for key,value in objdata.__dict__.items():
            print("\t{}---->{}".format(key,value))

#main program

s=Student()
e=Employee()
t=Teacher()

print("content of students=",s.__dict__)
print("content of employee=",e.__dict__)
print("content of teacher",t.__dict__)
s.getstuddet()
e.getempdet()
t.getteachdet()
print("content of s=",s.__dict__)
print("content of e=",e.__dict__)
print("content of t=",t.__dict__)

#today our requirementis to display any object content by single method
#this type of single method is called static method

Hyd.dispobjectdata(s,"Student")
Hyd.dispobjectdata(e,"Employee")
Hyd.dispobjectdata(t,"Teacher")

