print("select a food category 1:veg,2:non_veg")
choice=int(input())
if(choice==1):
    print("you have selected veg category")
    menu=int(input("select menu 1:meals 2:idli 3:dosa"))
    if(menu==1):
        print("you have selected meals")
    elif(menu==2):
        print("you have selected idli")
    elif(menu==3):
        print("you have selected dosa")
    else:
        print("menu not avialable")
elif(choice==2):
    print("you have selected nonveg")
    menu=int(input("select menu 1:chikken 2:kabhab 3:fish"))
    if (menu == 1):
        print("you have selected chikken")
    elif (menu == 2):
        print("you have selected kabhab")
    elif (menu == 3):
        print("you have selected fish")
else:
    print("invalid category")
