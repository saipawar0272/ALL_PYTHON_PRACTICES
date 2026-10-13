#searching for all except upper alphabets

import re
letter=re.finditer("[^A-Z,a-z,0-9]", "dhdhwSHAJDKSJKSJKSJD782@@#2")
for res in letter:  #here res is an object of <class,re.match class>
    print("start index:{} End index:{} value:{}".format(res.start(), res.end(), res.group()))