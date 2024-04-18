name = input("enter the name")
cid = int(input("enter the id"))
unites = int(input("enter the unites:"))
if(unites<=100):
    bill = 0
elif(unites>100 and unites<200):
    bill = unites * 5
    print("the amount is res",bill)
elif(unites>=200):
    bill = unites * 10
    print("the bill is res",bill)

