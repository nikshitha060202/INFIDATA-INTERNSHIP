def create_account():
    global cname,cid,branch,bal
    cname=(input("enter ur name:"))
    cid=int(input("enter ur id:"))
    branch=(input("enter ur branch"))
    bal=float(input("enter ur balance"))
def deposit():
    global bal,deposit
    deposit=int(input("enter the amount to deposit"))
    bal=bal+deposit
    print("total amount is",bal)
def withdraw():
    global bal,withdraw
    withdraw = int(input("enter the amount for withdraw "))
    if(bal>=withdraw):
        bal=bal-withdraw
        print("withdraw is possible",bal)
    else:
        print("insufficient balance to withdraw")
def display():
    print(cname)
    print(cid)
    print(branch)
    print(bal)
print("welcome to online banking")
while(True):
    choice=int(input("enter your choice 1:create_account , 2:deposit , 3:withdraw , 4:display , 5:exit"))
    if choice == 1:
        create_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice ==4:
        display()
    elif choice == 5:
        print("exit")
    else:
        print("invalid")






