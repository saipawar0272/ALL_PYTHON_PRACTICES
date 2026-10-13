#wap which fill find marks of various students who are studying diff subjects ,whose cls are diff

def findtotalmarks(sname,scls,**marks):
    tot=0
    print("student name:{}".format(sname))
    print("student cls={}".format(scls))
    for k,v in marks.items():
        print("{}\t{}".format(k,v))
        tot=tot+v
        print("---------------")
        print("total marks={}".format(tot))

#main program

findtotalmarks("sai","x",eng=89,hindi=85,sci=78,comp=99)
findtotalmarks('soma','ix',sci=89,math=99,comp=98,hinfi=85,eng=85,python=99)
findtotalmarks("ganesh",'iv',math=78,eng=85,sci=85,tech=74,comp=85,python=56,java=45)
findtotalmarks("shv",'v')