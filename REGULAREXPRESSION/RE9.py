
#seraches for all special values

import re

letter=re.finditer(r"\W","dhsjhsd&@**(@))E@(SAIPAQAWEfkdjkf5674842265") #here W is used for search all special values
for word in letter:
    print("start index:{}, end index:{} value:{}".format(word.start(),word.end(),word.group()))
