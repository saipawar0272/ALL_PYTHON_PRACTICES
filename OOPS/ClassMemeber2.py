#program to demonstrate class level  data member and istance level data member

class Student:
  crs="Java"
  city="hyd" #here crs and city class level data members

#main program
s1=Student()
s2=Student()

s1.sno=65
s1.sname="sakshi"
s1.marks=85

s2.sno=56
s2.sname="somesh"
s2.marks=96

print("student no=",s1.sno)
print("student name=",s1.sname)
print("student marks=",s1.marks)
print("studet crs=",Student.crs)
print("student city=",Student.city)

print("*"*50)

print("s2 no=",s2.sno)
print("s2 name=",s2.sname)
print("s2 marks=",s2.marks)
print("s2 crs=",Student.crs)
print("student city",s2.city)