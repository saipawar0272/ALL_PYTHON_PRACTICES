def dispstudinfo(sno,sname,smarks,crs1='python',crs2='java'): #func definition
    print("{}\t{}\t{}\t{}\t{}".format(sno,sname,smarks,crs1,crs2))

#main program
dispstudinfo(45,'sai',89)    #here sno,sname are positional parameters
dispstudinfo(12,'ganesh',69) #and crs1=,cr2= are default parameters
dispstudinfo(20,'soma',96)
dispstudinfo(sname='amesh',sno=89,smarks=85)
dispstudinfo(56,'shiva',96,crs1='R',crs2='AI')
dispstudinfo(sname='katik',sno=45,smarks=56.32)
