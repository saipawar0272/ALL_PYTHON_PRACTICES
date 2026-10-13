#program to demonstrate converting json file string format data into dict data

import json
jsonstr='{"100":"Python","200":"java","300":".net","400":"javascript"}'
print( jsonstr,type(jsonstr))

#convert json str format into dict format we use load()
d=json.loads(jsonstr)
for key,val in d.items():
    print("\t{}--->{}".format(key,val))
    print("*"*59)

