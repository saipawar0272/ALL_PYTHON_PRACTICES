def sumavg(sname,place,*n,crs="python"):
    print("names=",sname)
    print("place",place)
    print("crs",crs)
    s=0
    for val in n:
        print("\t{}".format(val))
        s=s+val
    else:
        print("sum={}".format(s))
        print("average={}".format(s/len(n)))

#main program
sumavg("dileep",'hyd',10,20)
sumavg('sai','mum',56,85,56,48,78)
sumavg('ganesh','rajstan',96,78,2,34,52,63)
