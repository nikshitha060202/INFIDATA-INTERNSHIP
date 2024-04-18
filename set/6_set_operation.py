# | union
# intersection
# - difference
#  ^ symmetric -difference

a={1,2,3,4,5}
b={4,5,6,7,8}
print("a|b:",a|b)  #OR
print("a.union(b)",a.union(b))

print("a.intersection(b)",a.intersection(b))
print("a&b",a&b)

print("a-b",a-b)    #OR
print("a.difference(b)",a.difference(b))

print("b-a",b-a)   #OR
print("b.difference(a)",b.difference(a))

print("a^b",a^b)   #OR
print("a.symmetric_difference(b)",a.symmetric_difference(b))