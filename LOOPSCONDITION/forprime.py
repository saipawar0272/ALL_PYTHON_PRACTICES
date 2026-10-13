#python program which will generate prime numbers within the given numbers
n=int(input("enter number:"))
if(n<=2):
    print("invalid input")
else:
    print("prime numbers")
    for num in range(2,n+1): #outer loop supply the numbers
        res=True
        for i in range(2,num): #inner loop
            if(num%i==0):
                res=False
                break
        if(res):
                    print("\t{}".format(num))



