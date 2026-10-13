#program for extract only numbers from given data
line=input("enter line of number:")
print("given number:{}".format(line))
for int in line:
    if(int.isnumeric()):
        print("{}".format(int))