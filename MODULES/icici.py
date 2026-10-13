#icici.py
from ctypes import HRESULT

bname="ICICI"
addr="HYD"   #here name and addr are called global variables
def simpleint(): #function defn
    p =float(input("Enter principle Amount:"))
    t =float(input("Enter time:"))
    r =float(input("Enter rate of interest:"))
    #cal si and totamt
    si = (p*t*r)/100
    totamt = p+si
    #display the result
    print("*"*50)
    print("\t\tResult of simple interest")
    print("*"*50)
    print("\t\tPrinciple Amount:{}".format(p))
    print("*"*50)
    print("\t\t Time:{}".format(t))
    print("\t\tRate of interest:{}".format(r))
    print("\t\tsimple interest:{}".format(si))
    print("\t\tTotal amount to PAY:{}".format(totamt))
    print("*"*50)
