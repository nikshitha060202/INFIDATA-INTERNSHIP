l=int(input("enter length:"))
b=int(input("enter breadth:"))
h=int(input("enter height:"))
while(True):
    choice=int(input("enter ur choice 1:Area,2:volume,3:exit"))
    if(choice==1):
        area=l*b
        print("area of rectangle",area)
    elif(choice==2):
        vol=l*b*h
        print("volume of rectangle",vol)
    elif(choice==3):
        exit(0)
    else:
        print("invalid")