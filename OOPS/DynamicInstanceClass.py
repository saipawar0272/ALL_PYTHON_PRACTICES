
class Student :
    crs="java"
    city="hyd"

s1=Student()
s2=Student()

s1.sno=int(input("Enter no of student"))
s1.sname=input("enter name of student")
s1.marks=float(input("enter marks"))
print("*"*50)
s2.sno=int(input("enter sno"))
s2.sname=input("enter name")
s2.marks=float(input("enter marks"))
print("*"*50)
print("s1 no=".format(s1.sno))
print("s1 name=".format(s1.sname))
print("s1 marks",s1.marks)
print("*"*50)

print("s2 no=",s2.sno)
print("s2 name=",s2.sname)
print("s2 marks=",s2.marks)