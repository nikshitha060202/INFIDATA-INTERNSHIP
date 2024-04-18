weight=int(input("enter your current earth weight"))
planets=int(input("enter planets 1:venus 2:mars 3:jupiter 4:saturn 5:uranus 6:naptune"))
if(planets==1):
    pounds=weight*0.78
    print("your weight would be",pounds)
elif(planets==2):
    pounds = weight * 0.39
    print("your weight would be", pounds)
elif(planets==3):
    pounds = weight * 2.65
    print("your weight would be", pounds)
elif(planets==4):
    pounds = weight * 1.17
    print("your weight would be", pounds)
elif(planets==5):
    pounds = weight * 1.05
    print("your weight would be", pounds)
elif(planets==6):
    pounds = weight * 1.23
    print("your weight would be", pounds)


