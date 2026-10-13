#program for accepting list of values and find their sum
def readvalues():
    nov=int(input("enter how many values you want:"))
    if(nov<=0):
        return[]
    else:
        lst=[]
        for i in range(1,nov+1):
            val=float(input("Enter {} values ".format(i)))
            lst.append(val)
        return lst

def findsumavg(lst):
    if(len(lst==0)):
        print("list is empty can't find sum and avg")
    else:
        s=0
        for val in lst:
            print("\t{}".format(val))
            s=s+val
        else:
            print("sum={}".format(s))
            print("avg={}".format(s/len(lst)))

#main program
lst=readvalues() #function call
findsumavg(lst)


