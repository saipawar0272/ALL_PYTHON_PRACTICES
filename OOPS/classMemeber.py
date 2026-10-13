#

class Student:
    crs="Python"

s1=Student()
s2=Student()

print("content of s1=",s1.__dict__)
print("content of s2=",s2.__dict__)
#here crs is not part of s1 and s2
#here we are accessing class level data member with respect to Class name
print("S1 content as s1",Student.crs)
print("s2 content as=s2",Student.crs)

     #OR
#herer we are accessing class level data member w.r.t to object name
print("s1 content as s1=",s1.crs)
print("s2 content as =",s2.crs)