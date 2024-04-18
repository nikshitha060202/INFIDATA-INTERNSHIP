presence=int(input("enter the number of working days"))
absence=int(input("enter the number of days absense"))
percentage=(presence-absence)/presence*100
print("presence of class attended is:",percentage)
if(percentage<75):
    print("not able to exam")
else:
    print("able to exam")