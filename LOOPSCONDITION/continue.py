#program for deonstrating continue statment
s="PYTHON"
for ch in s:
    print("{}".format(ch))
else:
    print("i am from else part of for loop")
    print("_______________________________")

for ch in s:
    if(ch=="H") or (ch=="Y"):
        continue
    else:
        print("{}".format(ch))
