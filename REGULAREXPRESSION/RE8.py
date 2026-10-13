#seraches for all alphanumeric values

import re

letter=re.finditer(r"\w","dhsjhsd#&@**(@))E@(SAIPAQAWEfkdjkf5674842265") #here w is used for search all alpha-numeric values
for word in letter:
    print("start index:{}, end index:{} value:{}".format(word.start(),word.end(),word.group()))
