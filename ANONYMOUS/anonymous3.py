#program which will accept threee numerical values and find max of them by using anonymoues function and check for equality
#program which will acceot numerical value and check whether it is palindrome or not

palindrome=lambda x: "palindrome" if str(x)==str(x)[::-1] else "not palindrome"


#main program
n=int(input("Enter number:"))
res=palindrome(n)
print("{} is {}".format(n,res))