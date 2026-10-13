#wap which will accep list of elements dynamically in list and find the sum and average of the elements

list=[]

n=int(input("enter number:"))

for i in range(0,n):
    m=float(input())
    list.append(m)
    print("list elements are:{}".format(list))
    s=0
    i=0
    while(i<len(list)):
        print("\t{}".format(list[i]))
        s=s+list[i]
        i=i+1
    else:
        print("sum={}".format(s))
        avg=s/n
        print("avg of given elements:{}".format(avg))
