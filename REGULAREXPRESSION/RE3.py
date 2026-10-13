from RE2 import re
gf="Python is an oop language, with independency and support robust applications"
cd="ython"
matres=re.finditer(cd,gf) #here matres is an object of <class, 'callable_iterator>
for res in matres:  #here res is an object of <class, re.match class>
    print("Start index:{} End Index:{} Value:{}".format(res.start(),res.end(),res.group()))