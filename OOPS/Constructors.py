#program for demonstrating class and objects without using constructors

class Student:
    def setstudvals(self):
        self.sno=10
        self.sname="sai"


#main program

s=Student() #object creation
print("content of s=",s.__dict__) # {}--empty
s.setstudvals() #for setting the values in objects s--we are calling a method explicitly
print("content of s=",s.__dict__)