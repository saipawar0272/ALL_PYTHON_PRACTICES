#seraching for exactly one K

import re
letter=re.finditer("K","SajjejkkkKKKK")
for word in letter:
    print("start index:{} end index:{} value:{}".format(word.start(), word.end(),word.group()))