n1=int(input("enter first number"))
n2=int(input("enter second number"))
try:
    div=n1/n2
    print("res of div:",div)
except ZeroDivisionError as e:
    print("u r trying to div an int num by zero")
    print("e value:",e)
print("end")