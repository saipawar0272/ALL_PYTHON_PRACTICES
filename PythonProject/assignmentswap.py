#swapping of two integers
a,b=int(input("Enter integer value of a:")),int(input("Enter integer value of b:"))
print("\tOriginal Value of a:{}".format(a))
print("\tOriginal Value of b:{}".format(b))
print("*"*50)
a=a+b
b=a-b
a=a-b
print("\tSwapped Value of a:{}".format(a))
print("\tSwapped Value of b:{}".format(b))
print("*"*50)