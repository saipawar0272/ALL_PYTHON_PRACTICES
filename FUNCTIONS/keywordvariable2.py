#program to demonstrate keyword variable lem=ngth arguments

def dispvalues(**kvr):
    print("*"*50)
    print("number of values=",len(kvr))
    for k,v in kvr.items():
        print("\t{}---->{}".format(k,v))
        print("*"*50)

#main program
dispvalues(sno=45,sname="ramesh",marks=56)
dispvalues(eno=10,ename="Ganesh", contact=7846497445)

dispvalues(cno=23,cname="daud",cexp=52312)