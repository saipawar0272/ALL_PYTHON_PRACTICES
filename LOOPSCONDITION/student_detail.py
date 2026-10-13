
## wap which will accept student detail from keyboard and display the sutdent result

sno=int(input("enter student no:"))
sname=input("enter student name:")
scls=int(input("enter student class:"))
smarks=float(input("enter student marks:"))
cname=input("enter college name:")

print("student_details:")
print("*"*40)

print("student number is",sno)
print("student name is",sname)
print("class is",scls)
print("student marks is{}".format(smarks))
print("college name is",cname)