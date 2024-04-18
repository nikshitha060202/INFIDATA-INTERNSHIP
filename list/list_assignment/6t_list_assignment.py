print("interchange the first and last element in the list")
ls=[2,4,5,7,1]
print(ls)
t=ls[0]
ls[0]=ls[len(ls)-1]
ls[len(ls)-1] = t
print(ls)