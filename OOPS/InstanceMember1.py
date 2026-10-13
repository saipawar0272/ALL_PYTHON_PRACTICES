#program to demonstrate instance data type

class Student:pass
s1=Student()
s2=Student()

#main program
s1.sno=56
s1.sname="rajesh"
s1.marks=99
print("------------------")
s2.sno=52
s2.sname="ganesh"
s2.marks=63

print("*"*50)
print("marks of s1=",s1.sno)
print("name of s1=",s1.sname)
print("marks of s1=",s1.marks)

print("*"*50)
print("number of s2=",s2.sno)
print("name of s2=",s2.sname)
print("marks of s2=",s2.marks)
print("*"*50)

print("initial Content of s1={} and \nno of values={}".format(s1.__dict__,len(s1.__dict__)))
print("initial content of s2={} and \nno of values={}".format(s2.__dict__,len(s2.__dict__)))
