gender=input("enter ur gender(M/F):").upper()
age=int(input("enter ur age"))
num_of_days=int(input("enter num of days"))
if(age >= 18 and age <30):
    if(gender=='M'):
        wages = 700 * num_of_days
    elif(gender=='F'):
        wages =750
elif( age>=30 and age<=40):
    if (gender == 'M'):
        wages = 800 * num_of_days
    elif (gender == 'F'):
        wages = 850

print("wages",wages)

