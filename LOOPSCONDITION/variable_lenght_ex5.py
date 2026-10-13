#wap which will find sum and avg of variable number of numerical values

def sumavg(sname,place,*n,crs='python'):
    print("name=",sname)
    print("place=",place)
    print("course=",crs)

    s=0
    for val in n:
        print("\t{}".format(val))
        s=s+val
    else:
        print("sum={}".format(s))
        print("average={}".format(s/len(n)))

#main program

sumavg("Dileep","hyd",10,20,30)
print("-------------------")
sumavg("naveen","AP",78,63,45,41,87)
print("------------------------------")
sumavg("ramesh","MH",78,56,26,74,55)