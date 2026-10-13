#python program for obtain only special symbol
line=input("enter text:")
print("given text: {}".format(line))
for ch in line:
    if(ch.isalnum()):
        print("{}".format(ch))