#program which will read the records from employee file where emplotee records are present by using unpickling process

import pickle
try:
    with open("emp.pic","rb") as fp:
        while(True):
            record=pickle.load(fp)
            print(record,type(record))
        else:
            print(" ")
except EOFError:
    print("All file exceeds")

