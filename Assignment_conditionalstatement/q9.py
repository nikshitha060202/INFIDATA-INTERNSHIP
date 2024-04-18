age=int(input("enter age:"))
gender=input("enter gender(M/F):").upper()
days=int(input("enter number of days:"))
if(age>18 and age<=40):
    if(gender=='M'):
        if(age<30):
            wages=700*days
        else:
            wages=800*days
    elif(gender=='F'):
        if(age<30):
            wages=750*days
        else:
            wages=850*days
    print("wages: $",wages)
else:
    print("invalid")
