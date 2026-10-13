#program to demonstrate decorator

def getval():  #hereg etval ,every function name is one type of object
    return float(input("enter number:"))

def square(kvr): #outer function
    def operation(): #inner function
        n=kvr() #local
        res=n**2 #local
        return  res
    return operation

#main program
op=square(getval)   #here  function call is taking another function call and is called as decorator

result=op()
print("type of op=",type(op))
print("result=",result)