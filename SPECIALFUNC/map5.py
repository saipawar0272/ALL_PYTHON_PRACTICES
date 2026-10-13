#program for salary and commission
print("enter list of salaries seprated by space:")
sallist=[float(sal) for sal in input().split()]
print("Enter lst of commisssion values sperated by space:")
commlist=[float(comm) for comm in input().split()]
#print("sal list=",sallist) #200 300 400
#print("comm list=",commlist)
if(len(sallist)>len(commlist)):
    for i in range(len(sallist)-len(commlist)):
        commlist.append(0)
elif(len(commlist)>len(sallist)):
    for i in range(len(commlist)-len(sallist)):
       sallist.append(0)
#compute total salary
totsal=list(map(lambda sal,comm:sal+comm,sallist,commlist))
print("*"*50)
for sal,comm,tsal in zip(sallist,commlist,totsal):
    print("\t{}\t\t\t{}\t\t\t\t{}".format(sal,comm,tsal))
    print("="*50)
       #print("sallist=",sallist)
       #rint("commlist=",commlist)

