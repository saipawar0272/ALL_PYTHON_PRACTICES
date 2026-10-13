#write python program which will accept numerical values and seprare them with positive values and negative values

nov=int(input("enter how many values you want to enter:"))
if(nov<=0):
    print("{} is invalid input".format(nov))
else:
    lst=[]
    for i in range(1,nov+1):
        val=float(input("enter {} value:".format(i)))
        lst.append(val)
    else:
        print("list of values={}".format(lst))
        #obtaining list of +values
        pslist=[]
        for val in lst:
            if(val<=0):
                continue
                pslist.append(val)
            else:
                print("list of +ve values=",pslist)

                #code for obtaining negative values
                nvlist=list()
                for val in lst:
                    if(val>=0):
                        continue
                        nvlist.append(val)
                    else:
                        print("list of -ve values=",nvlist)