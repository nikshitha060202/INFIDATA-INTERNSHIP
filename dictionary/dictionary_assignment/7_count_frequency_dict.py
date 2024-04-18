l1=['a','b','c','d','c','c','c']
frequency={}
for item in l1:
    if(item in frequency):
        frequency[item]+=1
    else:
        frequency[item]=1
for key,value in frequency.items():
    print("%s->%d"%(key,value))