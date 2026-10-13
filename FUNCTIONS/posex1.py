#program for demonstrating positional arguments
def studinfo(sno, sname, smarks,crs ):  #here sno,sname are called positional parameters
    print("\t{}\t{}\t{}\t{}".format(sno, sname, smarks, crs))

#main program
print("+"*50)
print("\tSTNO\tSNAME\tMARKS\tcrs")
print("+"*50)
studinfo(sno=45, sname='atif', smarks=78, crs="python") #function call----here atif,78,python are called positional arguments
studinfo(sno=12, sname='sai',  smarks=88.,crs= "java") #function call
studinfo(sno=10, sname='sakshi',smarks=35,crs="python") #functon call
print("+"*50)


