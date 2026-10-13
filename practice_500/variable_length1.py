#wap program which will find sum and avg of numbers

def sumavg(sname,splace,*n,crs='python'):
    print("sname:",sname)
    print("marks:",splace)
    print("course",crs)

    s=0
    for val in n:
        print("\t{}".format(val))
        s=s+val
    else:
        print("sum={}".format(s))
        print("average={}".format(s/len(n)))

#main program

sumavg("dileep",'hyd',10,20,30)
sumavg('sai','mumbai',23,56,99)
sumavg('ramesh','hyd',56,89,26,crs='java')