

#write argument must be string not literal
# so that's why we have to use writelines here

L = ['hii \n', 'i am pawar saiprasad \n ' ,'i am here to study \n', 'hello all bwt students \n', 'sai']

f = open('sample.txt','w')
f.writelines(L)
f.close()