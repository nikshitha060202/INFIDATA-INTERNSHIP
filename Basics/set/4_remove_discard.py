s1={10,20,30,30,10,40,50}
print("s1 is:",s1)
s1.remove(30)
print("after remove(20)",s1)

# if we use discard() then again remove which element is removed by discard ,using remove()  --- output is keyerror
# if we use remove() ,then we use discard() to discard the element by which elemenet is removed using remove() ---> output not effected /output will be come
s1.discard(10)
print("after discard(10):",s1)
