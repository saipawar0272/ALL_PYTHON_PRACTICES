#program to generate multiplication table of number
n=int(input("enter the number:"))
if(n<=0):
    print("invalid input{}".format(n))
else:
    print(" multiplicaton table for :{}".format(n))
    i=1 #initialization
while(i<=10): #condition
    print("{}*{}={}".format(n,i,n*i))
    i=i+1 #updation
else:
    print("other statement")