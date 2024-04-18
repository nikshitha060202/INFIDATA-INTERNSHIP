gender=input("enter your gender(M/F):").upper()
fname=input("enter your first name")
lname=input("enter your last name")
age=int(input("enter your age"))
if(gender=='F'):
    if(age>=20):
        married=input("are you married?(y/n):").lower()
        if(married=='y'):
            print("Mrs"+fname+""+lname)
        elif(married=='n'):
            print("Ms",fname)
elif(gender=='M'):
    if(age>=20):
        married = input("are you married(y OR n?:").lower()
        if (married=='y'):
            print("Mrs" + fname + "" + lname)
        elif(married=='n'):
            print("Mr",fname)



