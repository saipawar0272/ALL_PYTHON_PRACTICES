
#program for defining instance data member

class Student:pass

#main program
s1=Student()  #here s1 is an object
s2=Student() #here s2 is an objct
print("*"*50)
print("id of s1=",id(s1))
print("id of s2=",id(s2))
print("*"*50)

#Add the students details to s1 ---instance data members
s1.sno=55
s1.sname="vishal"
s1.marks=78.35  #here sno,sname.smarks are called instance data members

#add students details to s2--instace data member
s2.sno=56
s2.sname="sai"
s2.marks=89.85

print("*"*50)
print("number of  s1",s1.sno)
print("name of s1=",s1.sname)
print("marks of s1=",s1.marks)
print("*"*50)

print("number of s2=",s2.sno)
print("name of s2=",s2.sname)
print("marks of s2=",s2.marks)


