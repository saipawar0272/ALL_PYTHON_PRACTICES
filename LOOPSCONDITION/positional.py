# wap program which will demonstrate the concept of positional parameter

def disp(stno,stname,stmarks,stcname) :  #function definition--are called parameters
    print("student number={}".format(stno))
    print("student name={}".format(stname))
    print("student marks={}".format(stmarks))
    print("student college={}".format(stcname))

#main program

stno=78
stname='sai'
stmarks=69
stcname='datt'
disp(stno,stname,stmarks,stcname)  #function call --are called arguments