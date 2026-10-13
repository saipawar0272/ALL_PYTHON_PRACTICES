#wap program which will demonstrate the default parameter

def dispinfo(stno,stname,stmarks,stcname,crs1='java',crs2='python'):
    print("{}\t{}\t{}\t{}\t{}\t{}".format(stno,stname,stmarks,stcname,crs1,crs2))

#main program
print("stno\tstname\tstmarks\tstcname\tcrs1\tcrs2")

dispinfo(stno=96,stmarks=89,stname='sau',stcname='datt')
dispinfo(stno=26,stcname='symbiosis',stname='ram',stmarks=85,crs1='golang')
dispinfo(stcname='mit',stmarks=88,stno=87,stname='shyam',crs2='intelligence')
