n=int(input("Enter number:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    for num in range(1,n+1): #outer for loop supply the number
        print("----------------------")
        print("mul table for {}".format(num))
        print("-----------------------")
        for i in range(1,11): #inner loop generates multiplication table
            print("\t{}*{}={}".format(num,i,num*i))
        else:
            print("----------------------")