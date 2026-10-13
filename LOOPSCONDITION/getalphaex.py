#program to find only alphabets from given data
#line="45python558878(^*%"
line=input("Enter line of text:")
print("given line:{}".format(line))
for ch in line:
    if(ch.isalpha()):
        print("{}".format(ch))