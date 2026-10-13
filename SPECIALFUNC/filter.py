#program using filter

def pos(val):
    if(val>0):
        return True
    else:
        return False

def neg(val):
    if(val<0):
        return True
    else:
        return False

#main program
lst=[10,-45,56,23,-89]
kvr=filter(pos,lst)
kvr=filter(neg,lst)
print("type of kvr=",type(kvr))
#convert filter object kvr into list object
pslist=list(kvr)
nslist=list(kvr)
print("Given list:{}".format(lst))
print("Postitve list:{}".format(pslist))
print("negative values:{}".format(nslist))
