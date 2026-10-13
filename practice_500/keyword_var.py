
def show(**n): #type dict
    print("key/value")
    for k,v in n.items():
        print("{}\t{}".format(k,v))

#main program

show(sno=56,sname='ramesh')
show(sno=89,sname='ganesh',)