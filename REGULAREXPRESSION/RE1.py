
import re
gd="Python is an oop language.Python is also fun prog language"
sp="a"
words=re.findall(sp,gd)
print(words)
print("number of times {} found={}".format(sp,len(words)))