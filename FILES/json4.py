#program fro loading json file data into dict data

import json
try:
    fp=open("jstudent.json","r")
    d=json.load(fp)

    for key,value in d.items():
       print("\t{}--->{}".format(key,value))
except FileNotFoundError:
                        print("file not exist")