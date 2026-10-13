#program to obtain sallist and commision list
sallist=[100,200,300,400]
commlist=[10,20,30,40]
totsal=list(map(lambda sal,comm:sal+comm, sallist,commlist))
print("*"*50)
print("salary\t\tcommision\t\ttotal salary")
print("="*50)
for sal,comm,tsal in zip(sallist,commlist,totsal):
    print("\t{}\t\t\t{}\t\t\t\t{}".format(sal,comm,tsal))
    print("*"*50)
