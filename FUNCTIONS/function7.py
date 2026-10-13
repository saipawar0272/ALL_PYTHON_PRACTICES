#pythton code for simple interest 

def simpleint():
    p=float(input("Enter principle Amount:"))
    t=float(input("Enter time period:"))
    r=float(input("enter rate of interest:"))
    #cal si and totamt to pay
    si=(p*t*r)/100
    totamt=p+si
    print("+"*50)
    print("principle amount:{}".format(p))
    print("time{}".format(t))
    print("rate{}".format(r))
    print("simple interest{}".format(si))
    print("total amount to pay {}".format(totamt))
    print("+"*50)
    #main program
simpleint() #function call