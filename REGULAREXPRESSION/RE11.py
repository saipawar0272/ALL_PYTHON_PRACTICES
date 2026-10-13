#searching for all values

import re
word=re.finditer(".","shah37323JSJA@*#*@*")
for letter in word:
    print("start index:{} end index:{} value:{}".format(letter.start(), letter.end(), letter.group()))