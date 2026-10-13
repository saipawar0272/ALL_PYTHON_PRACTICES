#program for demonstrating saving dict data into json data

import json
d={"100":"Python","200":"java","300":".net","400":"javascript"}
print(d,type(d))
#saving dict data into json file
with open("jstudent.json","a") as fp:
    json.dump(d,fp)
    print("dict data saved as record in json file")