print("calculate charge for library")
days=int(input("enter the number of days"))
if days <=5:
    charge = days * 2
elif days>=6 and days<=10:
    charge = days * 3
elif days >=11 and days<=15:
    charge = days * 4
elif  days>=15:
    charge = days * 5
print(charge)

