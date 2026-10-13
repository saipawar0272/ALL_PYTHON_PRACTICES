#write python program which will read list of values fron keyboard  and display those values

nov=int(input("enter number:"))
if(nov<=0):
    print("invalid number {}".format(nov))
else:
    lst=[] #create an empty list for adding values
    for i in range(1,nov+1):
        val=float(input("enter {} value:".format(i)))
        lst.append(val)
    else:
        print("list of values={}".format(lst))