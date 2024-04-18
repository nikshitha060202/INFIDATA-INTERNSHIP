salary=float(input("enter your salary:"))
year_of_service=int(input("enter your year of service:"))
if(year_of_service>10):
    bonus_percentage = 0.10
elif(6<=year_of_service<=10):
    bonus_percentage = 0.08
else:
    bonus_percentage= 0.05
bonus_amount=salary*bonus_percentage
print(f"your bonus amount is:{bonus_amount:2f}")
