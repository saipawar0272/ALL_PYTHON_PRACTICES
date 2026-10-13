#program to demonstrate decorator

def cube(kvr):
    def operation():
        n,sqres==kvr()
        cbres=n**3
        return n,sqres,cbres
    return operation

def square(gv):
    def calculation():
        n=gv()
        res=n**2
        return n,res
    return calculation
@cube
@square #programmer defined decorator
def getval():  #function call
    return  float(input("Enter number:"))

#main program
x,y,z=getval() #normal function call
print("square({})={}".format(x,y))
print("cube of({})={}".format(x,y,z))