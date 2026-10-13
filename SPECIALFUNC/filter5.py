#program which will accept list of words and filter those words which will contain atleast one vowel
#program which will obtain alpha,symbol,digits

value = "P2yt$1545@#$%*"
alphas=list(filter(lambda ch:ch.isalpha(),value))
print("alphas=",alphas)
digits=tuple(filter(lambda ch:ch.isnumeric(),value))
print("nums={}".format("".join(digits)))
alphanum=set(filter(lambda ch:ch.isalnum(),value))
print("alphanumeric={}".format("".join(alphanum)))
spcl=tuple(filter(lambda  ch:not ch.isalnum(),value))
print("spcl={}".format("".join(spcl)))