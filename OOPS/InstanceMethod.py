#
class Student:
    def readstudvalues(self):
        self.sno=int(input("enter student number:"))
        self.sname=input("Enter name:")
        self.marks=float(input("enter marks"))
        print("*"*50)

    def dispstudvalues(self):
        print("\tstudent namuber=",self.sno)
        print("\tstudent name=",self.sname)
        print("\tstudent marks",self.marks)

    def dispstudvalues(self):
        print("\t student number=",self.sno)
        print("\t student name=",self.sname)
        print("\t student marks",self.marks)





s1=Student()
s2=Student()
#read the data automatically for s1 from keyboard through instance method
s1.readstudvalues()
s2.readstudvalues()
print("*"*59)
print("first student details")
s1.dispstudvalues()
s2.dispstudvalues()
print("content of s1",s1.__dict__)
print("content of s2",s2.__dict__)