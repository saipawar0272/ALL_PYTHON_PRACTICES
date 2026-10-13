#program to convert dict data into json file strinf format data i

import json
jsonstr={"100":"Python","200":"java","300":".net","400":"javascript"}
print(jsonstr,type(jsonstr))
#convert dict type data into json str data
jsonstrdata=str(jsonstr)
print(jsonstrdata,type(jsonstrdata))