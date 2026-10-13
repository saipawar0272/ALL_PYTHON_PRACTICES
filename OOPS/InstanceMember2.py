#
class Student:pass

s1=Student()
s2=Student()

#main program
s1.sno=56
s1.sname="ramesh"
s1.marks=96

print("*"*59)

s2.sno=23
s2.sname="ganesh"
s2.marks=74

print("marks of s1=",s1.sno)
print("name of student",s1.sname)
print("marks of s1=",s1.marks)

print("*"*50)
print("no of s2",s2.sno)
print("name of s2=",s2.sname)
print("marks of s2=",s2.marks)

for idmn,idv in s1.__dict__.items():
   print("\t{}----->{}".format(idmn,idv))
   print("*"*50)
for idmn,idv in s2.__dict__.items():
   print("\t{}----->{}".format(idmn,idv))