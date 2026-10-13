#searching for all upper case letters

import re

letter=re.finditer("[A-Z]","dsjhffjkSAIjkjdfjJAGDISH5676@#$")
for res in letter:
    print("start index:{} End Index:{} Value:{}".format(res.start(),res.end(),res.group()))