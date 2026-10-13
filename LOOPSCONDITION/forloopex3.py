#program to generate all odd numbers within n
n=int(input("Enter number:"))
if(n%2==0):
        print("{} is even number can't print".format(n))
else:
    for i in range(n,1,-2):
        print("\t{}".format(i))
        if(n<=0):
            print("invalid number{}".format(n))
    else:
        print("thank you")