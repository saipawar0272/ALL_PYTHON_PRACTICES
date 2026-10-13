#program using continue while statement
s="PYTHON"
i=0
while(i<len(s)):
    print("{}".format(s[i]))
    i=i+1
else:
    print("subject")
    i=0
    while(i<len(s)):
         if(s[i]=="H"):
             continue
             print("{}".format(s[i]),end="")
             i=i+1


