#wap which will dmonstrate the keyword argument use

def disp(stno,stname,stmarks,stcname):
    print("{}\t{}\t{}\t{}".format(stno,stname,stmarks,stcname))

#main program

print("number\tName\tMarks\tcollege")

disp(stname='sai',stmarks=85,stcname='datt',stno=96)
disp(stcname='symbiosis',stmarks=99,stname='kamal',stno=55)
disp(stname=85,stno='sai',stmarks=85,stcname='datt')