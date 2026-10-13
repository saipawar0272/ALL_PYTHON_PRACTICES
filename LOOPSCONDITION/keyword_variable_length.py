#keyword variable length example

def show(**n): # here **n is called keyword variable lenght parameter and whose type is dict
    print("key/value")
    for k,v in n.items():
        print("{} \t {}".format(k,v))

#main program
show(sno=12,sname='sai')
show(sno=56,sname='soma',smarks=26)
show(sno=78,sname='ganesh',sub='java')
show(smarks=52.32,crs='python')