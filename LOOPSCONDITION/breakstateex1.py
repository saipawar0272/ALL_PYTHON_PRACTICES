#program to demonstrate break key word
s="python"
print("by using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("i am from else part of the loop")
    print("-----------------")

    for ch in s:
        if(ch=="o"):
            break
        else:
            print(ch, end="")