#program for demonstrating default arguments/ parameters
def studinfo(sno, sname, smarks, crs="python",city="hyd"): #here sno,sname are called positional parametersand crs is default parameter
 print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,smarks,crs,city))
#main program
print("*"*50)

print("\tSTNO\tNAME\tMARKS\tCOURSE\tCITY")
print("*"*50)
studinfo(100,"Rs",  34.56) #function call positional arguments
studinfo(200,"sai", 88)
studinfo(300,"jayu",45)
studinfo(44, "rmesh",75)
studinfo(12,"triumph",45,city="USA")
print("#"*50)


