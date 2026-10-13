#program to generate all even numbers within n to 1
n=int(input("Enter even number:"))
if(n%2!=0):
    print("can,t print {} odd number please enter even number".format(n))
else:
    for i in range(n,0,-2):
        print("{}".format(i))