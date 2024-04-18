l1=[6,7,8,9]
print("list l1 is:",l1)
try:
    print("l1[2]:",l1[2])
    print("l1[5]:",l1[5])
except IndexError as e:
    print("i am at IndexError except block,e value is:",e)
finally:  #  finaly block is also executed after exception handling  we use proper exception handling before finally block then continue and print "end"
    print("i am at finally block")
    print("executing at finally")
print("end")
