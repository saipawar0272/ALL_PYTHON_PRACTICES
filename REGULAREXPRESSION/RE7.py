#searches for all except digits

import re
letter=re.finditer(r"\D","adjdfh#@^%&*457454DSDHS") #here D works as except digit search all
for res in letter: #here res is an object of <class,re.match class>
    print("start index:{} end index:{} value:{}".format(res.start(),res.end(),res.group()))