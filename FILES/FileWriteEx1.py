#program for demonstrating writing data to the file

sno=900
sname="sumesh"
smarks=223.89
#"perform write operations"
with open("student.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname +"\t")
    fp.write(str(smarks)+'\n')
    print("data writeen ti the file")