#wap program which will display keyword variable no of values

#keyword variable lenght example

def show(**n): #here n is called keyword variable lenght parameter and whose type is dict
    print("-----------------")
    print("key\tvalue")
    print("-----------------------")
    for k,v in n.items():
        print("{}\t{}".format(k,v))
        print("--------------------")

#main program

show(sno=89,sname='sai')
show(sno=85,sname='ganesh',place='hyd',marks=89,crs='python')
show(sno=85,smarks=99,sname='rameh',place='hyd',crs='go lang',research='fundamentals')
