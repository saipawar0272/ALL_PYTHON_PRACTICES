n=int(input("enter number"))
if(n<=0):
    print("invalid number",n)
else:
    list=[]
        for i in range(0,n):
        m=float(input())
        list.append(m)
    else:
        print("given list elements are:\n{}".format(list))
        list.sort()
        print("elements in ascending order \n{}".format(list))
        list.reverse()
        print("elements in descending order\n{}".format(list))