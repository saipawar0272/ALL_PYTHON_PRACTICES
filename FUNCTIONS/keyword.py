#program to demonstrate keyword arguments
def dispstudinfo(sno,sname,marks,crs="python",cnt="india"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#main program
print("*"*50)
print("\tSNO\tSNAME\tMARKS\tCRS\t\tCNT")
print("*"*50)
dispstudinfo(200,"shyam", 89,crs="java",cnt="dubai")
dispstudinfo(300,"ramesh",85) #function call with positional arguments
dispstudinfo(sname="ganesh",sno=400,marks=35) #function call with keyword arguments