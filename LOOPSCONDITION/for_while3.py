#wap which will accep list of elements dynamically in list and find the sum and average of the elements

n=int(input("enter number:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=list() #create empty
    print("enter {} values".format(n))
    for v in range(1,n+1):
        val=float(input())
        lst.append(val)
        #logic for sum and average
        s=0
        print("elements of list:")
        for val in lst:
            print("\t{}".format(val))
            s=s+val
            print("sum={}".format(s))
            print("average={}".format(s/len(lst)))