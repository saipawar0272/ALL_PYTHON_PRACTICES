#wap which will display multilplication  table for various selected values

n=int(input('enter number:'))

if(n<=0):
        print("invalid value",n)
else:
    lst=list()
for n in range(1,n+1):
        print("enter the number for which mul table u want:")
        v=int(input())
        lst.append(v)
else:
        print("mul table u want",lst)
for n in lst:
        print("mul table for:{}".format(n))

for i in range(1,11):
        print("\t{}*{}={}".format(i,n,i*n))