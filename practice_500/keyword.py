#demonstrate the concept of keyword arguments


def disp(stno,stname,stmarks,stclg):
    print("{},{},{},{}".format(stno,stname,stmarks,stclg))

#main program

disp(stno=56,stmarks=99,stclg='datt',stname='sai')
disp(stname='bugu',stmarks=35,stclg='symbiosis',stno=10)
disp(56,'sai',stmarks=63,stclg='dy patil') #positional arguments
disp(66,'sinhgad',55,stclg='sangli') #must define positional argument first