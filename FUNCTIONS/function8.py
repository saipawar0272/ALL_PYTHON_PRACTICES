#another way ro find simple intrest
def displayresult()
    p=float(input("Enter principle amount:"))
    t=float(input("Enter time:"))
    r=float(input("Enter rate of interest:"))
    return p,t,r
def calsimpleint():
    p,t,r=takevalues() #function with multiline assignment
    si=(p*t*r)/100
    totamt=p+si
    return p,t,r,si,totamt
def displayresult():
    p,t,r,si,totamt=calsimpleint() #function with multiline assignment
    print("+"*50)
    print("principle amount:{}".format(p))
    print("time period:{}".format(t))
    print("rate of interest:{}".format(r))
    print("simole interest:{}".format(si))
    print("total amount to pay :{}".format(totamt))
    print("+"*50)
    #main program
    displayresult() #function call