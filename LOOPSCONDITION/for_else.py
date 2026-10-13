#wap which will accept dynamic number of values in a lst and sort the in ascending and descending orders

n=int(input("enter number:"))
if(n<=0):
    print("invalid number".format(n))
else:
    lst=[]
    for i in range(0,n):
        m=float(input())
        lst.append(m)
    else:
        print("given list elements:\n{}".format(lst))
        lst.sort()
        print("list elements in ascending order:\n{}".format(lst))
        print("*"*30)
        lst.reverse()
        print("list elements in descending orders:{}".format(lst))