#python program which will accept list of numerical values and find their  sum of average by using functions
def readvalues():
    print("Enter list of values and press any special symbols to stop:")
    lst=[]
    while(True):
        val=input()
        if(not val.isalnum()) and (val.__contains__("."))  or (val.__contains__("-")):
            break
        else:
            lst.append(float(val))
    return lst

#main program
lst=readvalues() #function cal

print("content of lst=",lst)