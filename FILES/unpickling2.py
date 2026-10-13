#

import pickle
with open("emp.pic","rb") as fp:
    print("*"*40)
    while(True):
        try:
            record=pickle.load(fp)
            for val in record:
                print("\t{}".format(val),end="\t")
                print()
        except EOFError:
            print("*"*60)
            break
