#another way to define and call variable length argunments by callinh immidiately
def dispno(a,b,c,d,e):
    print("\t{}\t{}\t{}\t{}\t{}".format(a,b,c,d,e))
dispno(10,20,30,40,50)

def dispno(a,b,c,d):
    print("\t{}\t{}\t{}\t{}".format(a,b,c,d))
dispno(10,30,40,50)

def dispno(a,b,c): #function def
    print("\t{}\t{}\t{}".format(a,b,c,))
dispno(23,89,56)  #function call
def dispno(a,b):
    print("\t{}\t{}".format(a,b))
dispno(20,10)

def dispno(a):
    print("\t{}".format(a))
dispno(10)
