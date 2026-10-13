#searching for all digits

import re
letter=re.finditer(r"\d","aSHFadhifkweie349439@#$#$*&") #here r works as raw material and d is digits
for res in letter:   #here res is an object of <class,re.match class>
    print("start index:{} end index:{} value:{}".format(res.start(), res.end(), res.group()))
    