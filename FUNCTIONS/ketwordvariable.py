#program to demonstrate keyword variable length arguments
def disvalues(**kvr):  # here **param is kwd var length parameter whose type is dict
    print(kvr,type(kvr))

disvalues(eno=200,ename="sharayu",marks=56) #function call-1 with 3-keyword arguments
disvalues(sid=30,stname="EA",hb1="eating",hb2="sleeping",hb3="chatting",hb4="roaming")
disvalues(sname="ramesh",sno=45,marks=89)
disvalues()



