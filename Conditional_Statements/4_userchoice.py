n1=int(input("enter n1"))
n2=int(input("enter n2"))
ch=int(input("enter ur choice 1:add,2:sub,3:mul,4:div,5:mod"))
if(ch==1):
    res=n1+n2
    print("add of {0) and {1} is {2}".format(n1,n2,res))
elif(ch==2):
    res=n1-n2
    print("sub of{0} and {1} is {2}".format(n1,n2,res))
elif(ch==3):
    res=n1*n2
    print("mul of {0} and {1} is {2}".format(n1,n2,res))
elif(ch==4):
    res = n1 / n2
    print("div of {0} and {1} is {2}".format(n1,n2,res))
elif(ch==5):
    res = n1 % n2
    print("mod of {0} and {1} is {2}".format(n1,n2,res))
else:
    print("invalid choice")



