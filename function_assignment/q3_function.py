print("factorial of a number")
def fact(n):
    if n<0:
        print("factorial of negative number does not exit")
    elif n == 0:
        return 1
    else:
         return n * fact(n-1)
n=int(input("enter the value of n"))
result=fact(n)
print("factorial of",n,"is",result)
