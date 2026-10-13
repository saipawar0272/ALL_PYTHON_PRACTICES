#
sno=int(input("enter number:"))
sname=(input("enter name:"))
smarks=int(input("enter marks:"))
#perform write operations
with open("data.student","a") as kvr:
    kvr.write(str(sno)+"\t")
    kvr.write(sname+"\t")
    kvr.write(str(smarks)+"\n")
    print("data writeen to the list")