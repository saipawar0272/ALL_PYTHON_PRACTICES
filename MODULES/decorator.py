#non-decor
def getval():
    return 5

def square():
    n=getval()
    res=n**2
    print("square({})={}".format(n,res))

def cube():
    n=getval()
    res=n**3
    print("cube of({})={}".format(n,res))

def sqrroot():
    n=getval()
    res=n**0.5
    print(" squareroot of({})={}".format(n,res))
getval()
square()
cube()
sqrroot()