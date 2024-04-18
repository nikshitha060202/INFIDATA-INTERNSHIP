n1=int(input("enter first number"))
n2=int(input("enter second number"))
l1=[4,5,6,7,8]
print("list l1 is:",l1)
try:
    div=n1/n2
    print("res of div:",div)
    print("l1[2]:",l1[2])
    print("l1[5]:",l1[5])
except ZeroDivisionError as e:
    print("u r trying to dived to integer num by zero ")
    print("e value:",e)
except Exception as e:
    print("i am at generalised exception block")
    print("e value:",e)
print("end")