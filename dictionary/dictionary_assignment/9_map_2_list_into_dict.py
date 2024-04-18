t1_keys=["python","java","web"]
t1_values=[101,102,103]
print("original key list is:"+str(t1_keys))
print("original value list is:"+str(t1_values))
# to convert list to dictionary
res={}
for key in t1_keys:
    for value in t1_values:
        res[key]=value
        t1_values.remove(value)
        break
print("resultant dictionary is:"+str(res))