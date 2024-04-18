d1={"x":10,"y":8}
d2={"a":6,"b":4}
def merge(d1,d2):
    for i in d2.keys():
        d1[i]=d2[i]
    return d1
d3=merge(d1,d2)
print(d3)