#remove a particular item in a dictionary by using the pop()method
# this method remove ana item with the provided key and return the value
#popitem() method can be used to remove and return an arbitrary (key,value)
# item pair from the dictionary
#all the item can be removed at once,using clear()method
# we can also use the del keyword to remove individual item or the entire dictionary itself

d1={1:1,2:4,3:9,4:16,5:25,6:36}
print(d1)

print("pop value is:",d1.pop(2))
print("update dictionary is:",d1)

print("pop item is:",d1.popitem()) # remove an arbitrary item,return(key,value)
print("update dictionary is:",d1)

d1.clear() # remove all item
print("update dictionary is:",d1)

del d1 # delete the dictionary itself
print(d1)# error